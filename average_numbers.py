numbersToAverage = [43, 68, 3452, 12, 69, 420]

# tum tum
count = 0

for x in numbersToAverage:
    count += x

print(count/len(numbersToAverage))

#bajarni
sum = 0
for x in numbersToAverage:
    sum += x

print(sum / len(numbersToAverage))

#hreimur
sum = 0
count = 0
average = 0
for x in numbersToAverage:
    count += 1
    sum += x
average = sum/count
print(average)
