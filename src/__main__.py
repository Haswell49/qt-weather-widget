import sys

from src.core import Application
from src.ui.widgets import MainWidget


if __name__ == "__main__":
    app = Application()

    main_widget = MainWidget(app)

    app.main_widget = main_widget
    main_widget.show()

    sys.exit(app.exec())
