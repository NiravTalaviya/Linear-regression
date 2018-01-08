# ############# Method 1 ##############
# import numpy as np
# from matplotlib import pyplot as plt
# import csv
# if __name__ == "__main__":
#     x = []
#     y = []
#     with open('train.csv') as csvfile:
#         reader = csv.DictReader(csvfile)
#         i = 0
#         for row in reader:
#             x.append(row.get('x'))
#             y.append(row.get('y'))
#     x = np.array(x,dtype=float)
#     y = np.array(y,dtype=np.float)
#     n = np.size(x)
#     n = np.ones((n,n))
#     m_x = np.mean(x)
#     m_y = np.mean(y)
#     SS_xy = np.sum(y * x - n * m_y * m_x)
#     SS_xx = np.sum(x * x - n * m_x * m_x)
#     b_1 = SS_xy / SS_xx
#     b_0 = m_y - b_1 * m_x
#     print("Estimated coefficients:\nb_0 = {}  \
#               \nb_1 = {}".format(b_0, b_1))
#     plt.scatter(x, y, color="m", s=30)
#     y_pred = b_0 + b_1*x
#     plt.plot(x, y_pred,linewidth=2)
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.show()
#
#
# ################ Method 3 #########

import numpy
import csv
from matplotlib import pyplot as plt
x = []
y = []
z = []
with open('train.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for inputdata in reader:
        x.append(inputdata['x'])
        y.append(inputdata['y'])
x = numpy.asarray(x, dtype=numpy.double)
y = numpy.asarray(y, dtype=numpy.double)
len = x.size
max_x = x.max()
max_y = y.max()
for i in range(len):
    x[i] /= max_x
for i in range(len):
    y[i] /= max_y
alpha = numpy.double(1.00)
accuracy = 0.00000001
theta1 = numpy.double(5)
theta2 = numpy.double(0)
m, n = 0.1, 0.1
k = 0
for k in range(100):
    ans1 = 0
    ans2 = 0
    for i in range(len):
        ans1 += (theta2 * x[i] + theta1 - y[i])
        ans2 += (theta2 * x[i] + theta1 - y[i]) * x[i]
    theta1 -= alpha * (ans1 / len)
    theta2 -= alpha * (ans2 / len)
    k += 1
for i in range(len):
    th = theta2 * x[i] + theta1
    z.append(th)
plt.scatter(x, y)
plt.plot(x, z, color="red")
plt.show()



