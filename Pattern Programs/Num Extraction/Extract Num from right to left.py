def get_digit(num):
    if num < 10:
        print(num)
    else:
        print(num % 10)
        get_digit(num // 10)


get_digit(123456)

"""
6
5
4
3
2
1
"""
