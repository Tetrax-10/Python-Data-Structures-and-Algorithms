def sumOfFirstNNum(num):
    if(num == 1):
        return 1
    return num + sumOfFirstNNum(num-1)


print(sumOfFirstNNum(5))
