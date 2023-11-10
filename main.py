# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd


def read_data(filename):
    return pd.read_csv(filename)


def analyze_data(dataframe):
    # visualize data in a simple chart x-axis is time, y-axis is power
    # how many null entries do we have in power
    # in case of null values how do we fill them - avg, max, min or delete record
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    orig_train_data = read_data("./data/train.csv")
    print(orig_train_data.head(4))
