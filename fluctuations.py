import os.path
from collections import Counter

listOfDates = [
    "15-06-2021",
    "21-06-2021",
    "28-06-2021",
    "05-07-2021",
    "12-07-2021",
    "19-07-2021",
    "26-07-2021",
    "02-08-2021",
    "09-08-2021",
    "16-08-2021",
    "23-08-2021"
]

def getWeeklyServers():
    weeks = []
    for date in listOfDates:
        temp = set()
        with open("results/" + date + "-verified.csv", "r") as f:
            for line in f:
                line = line.strip()
                temp.add(line)
        if os.path.isfile("results/" + date + "-853-verified.csv"):
            with open("results/" + date + "-853-verified.csv", "r") as f:
                for line in f:
                    line = line.strip()
                    temp.add(line)
        weeks.append(temp)
    return weeks

def getTotalSetForPort(port = 784):
    allResolvers = set()
    for date in listOfDates:
        portsOfWeek = set()
        verified = set()
        with open("results/" + date + "-{}.csv".format(port), "r") as f:
            for line in f:
                portsOfWeek.add(line.strip())
        with open("results/" + date + "-verified.csv", "r") as f:
            for line in f:
                verified.add(line.strip())
        allResolvers.update(portsOfWeek.intersection(verified))
    return allResolvers

def getTotalSetForPort853():
    allResolvers = set()
    for date in listOfDates:
        portsOfWeek = set()
        verified = set()
        if os.path.isfile("results/" + date + "-853.csv"):
            with open("results/" + date + "-853.csv", "r") as f:
                for line in f:
                    portsOfWeek.add(line.strip())
        if os.path.isfile("results/" + date + "-853-verified.csv"):
            with open("results/" + date + "-853-verified.csv", "r") as f:
                for line in f:
                    verified.add(line.strip())
        allResolvers.update(portsOfWeek.intersection(verified))
    return allResolvers

def getWeeklyByPort():
    weeks = []
    for date in listOfDates:
        port784 = set()
        port8853 = set()
        port853 = set()
        result = Counter()
        with open("results/" + date + "-784.csv", "r") as f:
            for line in f:
                port784.add(line.strip())
        with open("results/" + date + "-8853.csv", "r") as f:
            for line in f:
                port8853.add(line.strip())
        if os.path.isfile("results/" + date + "-853.csv"):
            with open("results/" + date + "-853.csv", "r") as f:
                for line in f:
                    port853.add(line.strip())
        mergedVerified = set()
        with open("results/" + date + "-verified.csv", "r") as f:
            for line in f:
                mergedVerified.add(line.strip())
        if os.path.isfile("results/" + date + "-853-verified.csv"):
            with open("results/" + date + "-853-verified.csv", "r") as f:
                for line in f:
                    mergedVerified.add(line.strip())
        for item in mergedVerified:
            if item in port784 and item in port8853 and item in port853:
                result["784+8853+853"] += 1
            elif item in port784 and item in port8853:
                result["784+8853"] += 1
            elif item in port784 and item in port853:
                result["784+853"] += 1
            elif item in port8853 and item in port853:
                result["8853+853"] += 1
            elif item in port784:
                result["784"] += 1
            elif item in port8853:
                result["8853"] += 1
            elif item in port853:
                result["853"] += 1
        weeks.append(dict(result))
    return weeks


if __name__ == "__main__":
    weeks = getWeeklyServers()
    print(weeks)