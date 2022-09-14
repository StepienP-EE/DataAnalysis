import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math
import random as rnd


#Deklaracja dataseries_1
weekdays = ["Monday",'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdaysSeries = pd.Series(weekdays)
freeDays = [False, False, False, False, False, True, True]
freeDaysSeries = pd.Series(freeDays)
holidays = {"New Year" : "2018-01-01", "Epiphany" : "2018-01-06", 'Easter' : '2018-04-01'}
holidaysSeries = pd.Series(holidays)
#Deklaracja dataseries_2
dataAsFloatList = []
for i in range(100000):
    dataAsFloatList.append(i*rnd.random())
dataAsFloatSeries = pd.Series(dataAsFloatList)
#Deklaracja dataseries_3
dataAsStringList = []
for i in range(100000):
    dataAsStringList.append(i*rnd.random())
dataAsStringSeries=pd.Series(dataAsStringList)

# Deklaracja dataseries_4
cities = ["Shanghai", "Beijing", "Istanbul"]
population = [24183300, 20794100, 15030000]
citypop = pd.Series(index=cities, data=population)

def dataSeries_4():


    print(citypop.sum())
    print(citypop.mean())
    print(citypop.index)
    print(citypop.keys())
    print(citypop.values)
    print(citypop.tolist())

def dataSeries_6():

    age = ["do 6", "7-14", "15-17", "18-24", "25-39", "40-59", "60 i więcej"]
    incident = [14, 334, 312, 5823, 9491, 7486, 4343]
    incidents = pd.Series(data=incident, index=age)
    print(incidents.where(incidents > 1000).dropna())
    incident1000 = incidents.where(incidents > 1000).dropna()
    print(incident1000)
    print(incidents.filter(items=["18-24", "25-39", "40-59"]))
    incidents.where(incidents <= 1000, inplace=True)
    print(incidents)
    incidents.dropna(inplace=True)
    print(incidents)

def printing_DataSeries(name):
    print(name)
    print("Size: \t", name.size)
    print("Memory usage: \t", name.memory_usage(deep=True))
    print("Shape: \t", name.shape)
    print("Axes: \t", name.axes)
    print("dtype: \t", name.dtype)
    print("Index: \t", name.index)
    print("Is unique? \t", name.is_unique)
    print("Is monotonic? \t", name.is_monotonic)



if __name__ == '__main__':
    print("Wersja " + pd.__version__)
    #print(weekdaysSeries)
    #print(freeDaysSeries)
    #print(holidaysSeries)
    #dataSeries_4()
    #printing_DataSeries(dataAsFloatSeries)
    #printing_DataSeries(dataAsStringSeries)
    dataSeries_6()