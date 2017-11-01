from flask import Flask, render_template, request
from perfly_plot import PerflyPlot


perfly_plot_app = Flask(__name__, static_url_path='/static')


@perfly_plot_app.route('/perflyPlot', methods=['GET', 'POST'])
def perfly_plot_rest():
    if request.method == 'POST':
        date_string = request.args.get("date")
        card_processing_avg = request.args.get("cardProcessingAVG")

        perfly_plot = PerflyPlot()
        perfly_plot.load_perfly_data()
        perfly_plot.save_new_perfly_data(date_string, card_processing_avg)
        perfly_plot.prepare_axes_data()
        perfly_plot.create_plot()

        return "Data added to the perfly plot."
    else:
        return render_template('index.html')


if __name__ == "__main__":
    perfly_plot = PerflyPlot()
    perfly_plot.load_perfly_data()
    perfly_plot.prepare_axes_data()
    perfly_plot.create_plot()
    perfly_plot_app.run(threaded=True)
