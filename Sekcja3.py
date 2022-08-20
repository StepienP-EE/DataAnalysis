import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

excel = pd.read_csv('../../Downloads/course-files/pokemon.csv')C:\Users\przem\Documents\GitHub\DataAnalysis
from datetime import datetime

#birthday = datetime(1996, 2, 4, 0, 0, 0)
#diff = datetime.today() - birthday
month = np.arange(1, 13, 1)
amount = [1,5,20,450,700]
income =100 + 3*month
cost= 50+ 10*month

x = np.arange(-5, 5, 0.1)

def plots():
    fig, ax = plt.subplots(2)
    ax[0].plot(x, pow(2,x))
    ax[1].plot(month, income, 'go', month, cost, 'r^')
    plt.show()



#plt.plot(t, t**3, 'ro')
#Output


def printing(name):

    print(name +  f'{income}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    printing('PyCharm')
    plots()