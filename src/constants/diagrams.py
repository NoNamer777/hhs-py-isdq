from numpy import array, ndarray, sum, unique
from os.path import join
from pandas import read_csv


def count_occurrences(data: ndarray, to_count: ndarray):
    occurrences = []

    for count in to_count:
        occurrences.append(sum(data == count))

    return array(occurrences)


DIAGRAM_1_DATA = read_csv(join("src", "assets", "data", "employee_roles.csv"))
DIAGRAM_1_DATA_X = unique(DIAGRAM_1_DATA["role"].values.tolist())
DIAGRAM_1_DATA_Y = count_occurrences(DIAGRAM_1_DATA["role"], DIAGRAM_1_DATA_X)
DIAGRAM_1_TITLE = "Employee Roles Distribution"
DIAGRAM_1_DESCRIPTION = "The distribution of how many employees haven taken on a certain role.\n"

DIAGRAM_2_DATA = read_csv(join("src", "assets", "data", "rental_agreements.csv"))
DIAGRAM_2_DATA_X = unique(DIAGRAM_2_DATA["rental status"].values.tolist())
DIAGRAM_2_DATA_Y = count_occurrences(DIAGRAM_2_DATA["rental status"], DIAGRAM_2_DATA_X)
DIAGRAM_2_TITLE = "Rental Agreements statuses"
DIAGRAM_2_DESCRIPTION = "The distribution of the different rental agreements statuses and how many agreements have a" \
                        " certain status.\n"
