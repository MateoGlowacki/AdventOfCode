import re

lines = open('Day_1_input.txt').readlines()

total = 0
for line in lines:
    line = re.sub("oneight", "18", line)
    line = re.sub("twone", "21", line)
    line = re.sub("threeight", "38", line)
    line = re.sub("fiveight", "58", line)
    line = re.sub("sevenine", "79", line)
    line = re.sub("eightwo", "82", line)
    line = re.sub("nineight", "98", line)
    line = re.sub("one", "1", line)
    line = re.sub("two", "2", line)
    line = re.sub("three", "3", line)
    line = re.sub("four", "4", line)
    line = re.sub("five", "5", line)
    line = re.sub("six", "6", line)
    line = re.sub("seven", "7", line)
    line = re.sub("eight", "8", line)
    line = re.sub("nine", "9", line)
    first = 0
    r = 0
    last = 0
    for l in line:
        if l.isdigit():            
            last = int(l)
            if r == 0:
                first = int(l)
                r = 1
    total = total+10*first+last
print(total)