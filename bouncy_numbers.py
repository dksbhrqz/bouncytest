def is_bouncy (n):
    num_list = [int (x) for x in str (n)]
    goes_up = goes_down = False
    for index in range (1, len (num_list)):
        if (num_list[index-1] < num_list[index]):
            goes_up = True
        elif (num_list[index-1] > num_list[index]):
            goes_down = True
        if (goes_up and goes_down):
            return True
    return False

trials = 0
bouncy = 0
for i in range (100, 5000000):
    trials += 1
    if (is_bouncy (i)):
        bouncy += 1
    percent_bouncy = bouncy * 100 / trials
    if (99 == percent_bouncy):
        print('The least number with 99% of the proportion of bouncy numbers is', i)
        break
