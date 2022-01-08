import numpy as np
from os.path import join
import pandas as pd

from ..models import Diagram


def count_occurrences_in_list(data: np.ndarray) -> list:
    occurrences = []

    for entry in data:
        occurrences.append(np.count_nonzero(data == entry))
        data = data[data != entry]

    return occurrences


def count_occurrences(data: list, values: list) -> list:
    occurrences = []

    for query in values:
        occurrences.append(np.count_nonzero(data == query))

    return occurrences


DIAGRAM_1_DATA_X = np.unique(
    pd.read_csv(join("src", "assets", "data", "incoming_purchase_agreements.csv"))["date"].values,
    return_index=False,
    return_inverse=False,
    return_counts=True
)[0]
DIAGRAM_1_DATA_Y = np.array(count_occurrences_in_list(DIAGRAM_1_DATA_X))
DIAGRAM_1_LABEL_X = "Purchase date"
DIAGRAM_1_LABEL_Y = "Amount of purchases"
DIAGRAM_1_TYPE = "plot"
DIAGRAM_1_TITLE = "Number of purchases per day"
DIAGRAM_1_DESCRIPTION = "This diagram shows the number of purchases that have been done on a particular day"

DIAGRAM_2_DATA = np.array(count_occurrences(
    pd.read_csv(join("src", "assets", "data", "articles.csv"))["game or console"],
    ["CONSOLE", "SPEL"]
))
DIAGRAM_2_LABELS = np.array(["Games", "Consoles"])
DIAGRAM_2_TITLE = "Inventory distribution games vs. consoles"
DIAGRAM_2_TYPE = "pie"
DIAGRAM_2_DESCRIPTION = "This diagram shows distribution in the inventory of the shop in games vs. consoles"

DIAGRAM_1 = Diagram(
    data_x=DIAGRAM_1_DATA_X,
    data_y=DIAGRAM_1_DATA_Y,
    label_x=DIAGRAM_1_LABEL_X,
    label_y=DIAGRAM_1_LABEL_Y,
    diagram_type=DIAGRAM_1_TYPE,
    titel=DIAGRAM_1_LABEL_Y,
    description=DIAGRAM_1_DESCRIPTION
)
DIAGRAM_2 = Diagram(
    data=DIAGRAM_2_DATA,
    labels=DIAGRAM_2_LABELS,
    diagram_type=DIAGRAM_2_TYPE,
    titel=DIAGRAM_2_TITLE,
    description=DIAGRAM_2_DESCRIPTION
)

DIAGRAMS = [DIAGRAM_1, DIAGRAM_2]
