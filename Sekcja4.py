import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

weekdays = ["Monday",'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdaysSeries = pd.Series(weekdays)
freeDays = [False, False, False, False, False, True, True]
freeDaysSeries = pd.Series(freeDays)
holidays = {"New Year" : "2018-01-01", "Epiphany" : "2018-01-06", 'Easter' : '2018-04-01'}
holidaysSeries = pd.Series(holidays)


def printing(name):

    print(name)


if __name__ == '__main__':
    printing(weekdaysSeries)
    printing(freeDaysSeries)
    printing(holidaysSeries)
    holidaysSeries.size