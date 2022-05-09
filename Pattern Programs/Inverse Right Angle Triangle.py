def get_digit(num):
    if num < 10:
        print(num)
    else:
        print(num)
        get_digit(num // 10)


get_digit(123456)

"""
123456
12345
1234
123
12
1
"""