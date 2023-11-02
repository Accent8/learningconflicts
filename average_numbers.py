numbersToAverage = [43, 68, 3452, 12, 69, 420]
sum = 0
count = 0
average = 0
for x in numbersToAverage:
    count += 1
    sum += x
average = sum/count
print(average)
