import numpy as np

def reshpe_and_average_of_the_array(array,row,column):
    reshaped_array = np.reshape(array, (row, column))
    average_array = np.average(reshaped_array,axis=1)
    return average_array

def average_array(array):
    average_array = np.average(array)
    return average_array