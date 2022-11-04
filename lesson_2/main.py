import numpy as np

data_1 = np.genfromtxt('data_for_np_les2.csv', delimiter=',', skip_header=0)

list_of_one = [1 for i in range(data_1.shape[1])]
data_2 = np.diag(list_of_one)

multy = np.matmul(data_1, data_2)
np.savetxt('final_matrix.csv', multy, delimiter=",")