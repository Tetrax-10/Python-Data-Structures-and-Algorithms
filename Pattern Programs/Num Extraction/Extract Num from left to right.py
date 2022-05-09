def get_digit(num):
    if num < 10:
        print(num)
    else:
        get_digit(num // 10)
        print(num % 10)


get_digit(123456)

"""
1
2
3
4
5
6
"""