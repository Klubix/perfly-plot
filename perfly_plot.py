import yaml
import os
import matplotlib.pyplot as plt
from datetime import datetime


class PerflyPlot(object):

    def __init__(self):
        self._dates_list = list()
        self._results_list = list()
        self._perfly_plot_data = dict()
        self._perfly_data_file = "perfly_data.yaml"
        self._perfly_plot_png_file = "perfly_plot.png"
        self._perfly_results_key = "perfly_results"
        self._card_processing_avg_key = "card_processing_avg"
        self._card_processing_avg_limits_key = "card_processing_avg_limit"
        self._static_files_folder = "static"
        self._perfly_plot_date_time_format = "%Y%m%d%H%M"
        self._perfly_plot_legend_data_label = "Card processing avg"
        self._perfly_plot_legend_limit_label = "AVG limit"
        self._perfly_plot_title = "PERFLY CARD PROCESSING AVG OVER TIME"

    def load_perfly_data(self):
        with open(self._perfly_data_file, 'r') as perfly_data_file:
            self._perfly_plot_data = yaml.load(perfly_data_file)

    def save_new_perfly_data(self, date_string, card_processing_avg):
        self._perfly_plot_data[self._perfly_results_key][str(date_string)] = dict()
        self._perfly_plot_data[self._perfly_results_key][str(date_string)][self._card_processing_avg_key] = \
            float(card_processing_avg)
        with open(self._perfly_data_file, 'w') as perfly_data_file:
            yaml.dump(self._perfly_plot_data, perfly_data_file)

    def prepare_axes_data(self):
        for perfly_result in self._perfly_plot_data[self._perfly_results_key]:
            perfly_date_time = datetime.strptime(str(perfly_result), self._perfly_plot_date_time_format)
            card_processing_avg_result = \
                self._perfly_plot_data[self._perfly_results_key][perfly_result][self._card_processing_avg_key]
            self._dates_list.append(perfly_date_time)
            self._results_list.append(card_processing_avg_result)

    def create_plot(self):
        plt.clf()
        plt.figure(figsize=(20, 6))
        plt.plot(self._dates_list, self._results_list, 'ro', label=self._perfly_plot_legend_data_label)
        plt.axhline(y=self._perfly_plot_data[self._card_processing_avg_limits_key],
                    label=self._perfly_plot_legend_limit_label)
        plt.legend(loc='best', bbox_to_anchor=(0.2, -0.3), ncol=2, fancybox=True)
        plt.title(self._perfly_plot_title)
        plt.gcf().autofmt_xdate()
        plt.xticks(self._dates_list, rotation='vertical')
        plt.savefig(os.path.join(self._static_files_folder, self._perfly_plot_png_file), bbox_inches='tight')
