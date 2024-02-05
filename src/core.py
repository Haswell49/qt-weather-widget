from PySide6.QtWidgets import QApplication

from src.loaders import ReportDownloader
from src.ui.widgets import MainWidget


class Application(QApplication):
    _main_widget: MainWidget

    _report_downloader: ReportDownloader

    __application = None

    @property
    def main_widget(self):
        return self._main_widget

    @main_widget.setter
    def main_widget(self, widget: MainWidget):
        widget.setWindowTitle("Weather")

        self._main_widget = widget

        # self.update()

    # def __new__(cls):
    #     if cls.__application:
    #         return cls.__application
    #
    #     cls.__application = super(Application, cls).__new__(cls)

    def __init__(self, *args,
                 report_downloader=ReportDownloader(), **kwargs):
        super(Application, self).__init__(*args, **kwargs)

        self._report_downloader = report_downloader

    def subscribe_labels(self, *labels):
        for label in labels:
            self._report_downloader.add_observer(label)

    def update(self):
        self._report_downloader.download_report(
            (54.7116095, 20.46453))
