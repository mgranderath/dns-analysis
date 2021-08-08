listOfDates = [
    "15-06-2021",
    "21-06-2021",
    "28-06-2021",
    "05-07-2021",
    "12-07-2021",
    "19-07-2021",
    "26-07-2021"
]

for date in listOfDates:
    port784 = set()
    port8853 = set()
    count784 = 0
    count8853 = 0
    countBoth = 0
    with open("results/" + date + "-784.csv", "r") as f:
        for line in f:
            port784.add(line.strip())
    with open("results/" + date + "-8853.csv", "r") as f:
        for line in f:
            port8853.add(line.strip())
    with open("results/" + date + "-verified.csv", "r") as f:
        for line in f:
            line = line.strip()
            if line in port784 and line in port8853:
                countBoth += 1
            elif line in port784:
                count784 += 1
            elif line in port8853:
                count8853 += 1
    print("{} | 784: {}, 8853: {}, both: {} | doq-i00: {}, doq-i02: {}".format(date, count784, count8853, countBoth, count784, count8853 + countBoth))