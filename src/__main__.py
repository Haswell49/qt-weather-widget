import sys

from PySide6.QtWidgets import QWidget

from src.core import Application
from src.ui.widgets import MainWidget


if __name__ == "__main__":
    app = Application()

    main_widget = MainWidget(app)
    # main_widget.resize(200, 200)

    app.main_widget = main_widget
    main_widget.show()

    sys.exit(app.exec())
