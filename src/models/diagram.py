import matplotlib.pyplot as plt

KEY_DIAGRAM_DATA = "data"
KEY_DIAGRAM_LABELS = "labels"
KEY_DIAGRAM_DATA_X = "data_x"
KEY_DIAGRAM_NAME_X = "name_axis_x"
KEY_DIAGRAM_DATA_Y = "data_y"
KEY_DIAGRAM_NAME_Y = "name_axis_y"
KEY_DIAGRAM_TYPE = "diagram_type"
DIAGRAM_TYPES = ["plot", "scatter", "pie"]


class Diagram:
    def __init__(self, **kwargs):
        self._data = kwargs.get(KEY_DIAGRAM_DATA)
        self._labels = kwargs.get(KEY_DIAGRAM_LABELS)

        self._data_x = kwargs.get(KEY_DIAGRAM_DATA_X)
        self._data_y = kwargs.get(KEY_DIAGRAM_DATA_Y)
        self._name_axis_x = kwargs.get(KEY_DIAGRAM_NAME_X)
        self._name_axis_y = kwargs.get(KEY_DIAGRAM_NAME_Y)
        self._diagram_type = kwargs.get(KEY_DIAGRAM_TYPE) if str(kwargs.get(KEY_DIAGRAM_TYPE)).lower() in \
            DIAGRAM_TYPES else None

        if self._diagram_type is None:
            raise ValueError("No appropriate diagram type was specified")

        self._prepare_diagram()

    def show(self):
        plt.show()

    def _prepare_diagram(self):
        if self._diagram_type == DIAGRAM_TYPES[0]:
            # Plot diagrams
            self._diagram = plt.plot(self._data_x, self._data_y)

        elif self._diagram_type == DIAGRAM_TYPES[1]:
            # Scatter diagrams
            self._diagram = plt.scatter(self._data_x, self._data_y)
            pass

        elif self._diagram_type == DIAGRAM_TYPES[2]:
            # Pie charts
            # self._diagram = plt.pie(self._data, labels=self._labels, colors=["g", "r"])
            pass
