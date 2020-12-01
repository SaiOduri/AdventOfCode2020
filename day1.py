def day_one(f):
    fp = open(f)
    two_sum = {}
    for line_string in fp:
        line = int(line_string)
        difference = 2020-line
        if(difference in two_sum.keys()):
            return(difference*line)
        else:
            two_sum[line] = difference
    return 0