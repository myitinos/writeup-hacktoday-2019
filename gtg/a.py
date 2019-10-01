import string

data1 = string.printable
data2 = string.printable

for index, (value1, value2) in enumerate(zip(data1, data2)):
    print index, value1 + value2
