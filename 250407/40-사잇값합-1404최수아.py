import random as r

while True:
    start = r.randint(1,10)
    end = r.randint(1,10)

    if start > end:
        start,end = end,start
    else:
        hap = 0
        for i in range(start, end + 1):
            hap += i
        print(f'{start} ~ {end} => {hap}')

    if start == end:
        break