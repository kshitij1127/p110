import statistics
import csv
import pandas as pd 
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

popmean = statistics.mean(data)
popdev = statistics.stdev(data)

print("Original mean of the unsampled data is: ", popmean)
print("Original standard deviation of unsampled data is: ", popdev)

def randomset_ofmean(counter): 
    dataset = []
    for i in range(0, counter):
        randomindex = random.randint(0, len(data) - 1)
        value = data[randomindex]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def avg(mean_list):
    m = statistics.mean(mean_list)
    print("The mean of the sampled data from the file is: ", m)

def standard_deviation():
    mean_list = []
    for i in range(1, 1000):
        setofmeans = randomset_ofmean(100)
        mean_list.append(setofmeans)
    standard_D = statistics.stdev(mean_list)
    print("New standard deviation of sampled data is: ",standard_D)

def setup():
    meanlist = []
    for i in range(1, 1000):
        setofmeans = randomset_ofmean(100)
        meanlist.append(setofmeans)
    avg(meanlist)

standard_deviation()
setup()