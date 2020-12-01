def transformFileIntoArray(f):
    fp = open(f)
    array = []
    for line_string in fp:
        array.append(int(line_string))
    return array

def day_one_part1(f):
    two_sum = {}
    array = transformFileIntoArray(f)
    for line_string in array:
        line = int(line_string)
        difference = 2020-line
        if(difference in two_sum.keys()):
            return(difference*line)
        else:
            two_sum[line] = difference
    return 0

def day_one_part2(f):
    A = transformFileIntoArray(f)
    A.sort()
    for i in range(0, len(A)-2):
        l = i+1
        r = len(A)-1
        while(l < r):
            total = A[i] + A[l] + A[r]
            if (total == 2020):
                return(A[i]*A[l]*A[r])
            elif(total < 2020):
                l += 1
            else:
                r -= 1
    return 0
