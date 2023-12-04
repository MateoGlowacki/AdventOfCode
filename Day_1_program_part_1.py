lines = open('Day_1_input.txt').readlines()

total = 0
for line in lines:
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
        