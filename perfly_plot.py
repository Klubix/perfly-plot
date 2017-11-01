import yaml
import os
import matplotlib.pyplot as plt
from datetime import datetime

class PerflyPlot(object):

    def __init__(self):
        self._dates_list = list()
        self._results_list = list()
        self._perlfy_plot_data = dict()

    def load_perfly_data(self):
        with open("perfly_data.yaml", 'r') as perfly_data_file:
            self._perfly_plot_data = yaml.load(perfly_data_file)

    def save_new_perfly_data(self, date_string, card_processing_avg):
        self._perfly_plot_data['perfly_results'][str(date_string)] = dict()
        self._perfly_plot_data['perfly_results'][str(date_string)]['card_processing_avg'] = \
            float(card_processing_avg)
        with open("perfly_data.yaml", 'w') as perfly_data_file:
            yaml.dump(self._perfly_plot_data, perfly_data_file)

    def prepare_axes_data(self):
        for perfly_result in self._perfly_plot_data['perfly_results']:
            perfly_date_time = datetime.strptime(str(perfly_result), "%Y%m%d%H%M")
            card_processing_avg_result = self._perfly_plot_data['perfly_results'][perfly_result]['card_processing_avg']
            self._dates_list.append(perfly_date_time)
            self._results_list.append(card_processing_avg_result)

    def create_plot(self):
        plt.clf()
        plt.figure(figsize=(20, 6))
        plt.plot(self._dates_list, self._results_list, 'ro', label="Card processing avg")
        plt.axhline(y=self._perfly_plot_data['card_processing_avg_limit'], label="AVG limit")
        # box = plt.get_position()
        # plt.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=2, fancybox=True)
        plt.title("PERFLY CARD PROCESSING AVG OVER TIME")
        plt.gcf().autofmt_xdate()
        plt.savefig(os.path.join('static', 'perfly_plot.png'), bbox_inches='tight')
