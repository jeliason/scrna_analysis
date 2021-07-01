import numpy as np
def read_npy_file(file):
    npy_data = np.load(file)
    return npy_data
