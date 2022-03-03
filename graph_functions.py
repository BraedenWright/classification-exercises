import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# num columns graphing


def plot_num_float():
    '''
    takes in a train(dataframe) and gives a boxplot and histogram of columns that are dtype float64
    '''
    num_cols = train.columns[[train[col].dtype == 'float64' for col in train.columns]]

    for col in num_cols:
        plt.hist(train[col])
        plt.title(col)
        plt.show()
        plt.boxplot(train[col])
        plt.title(col)
        plt.show()



#

def plot_num_int():
    '''
    takes in a train(dataframe) and gives a boxplot and histogram of columns that are dtype int64
    '''
    num_cols = train.columns[[train[col].dtype == 'int64' for col in train.columns]]

    for col in num_cols:
        plt.hist(train[col])
        plt.title(col)
        plt.show()
        plt.boxplot(train[col])
        plt.title(col)
        plt.show()
