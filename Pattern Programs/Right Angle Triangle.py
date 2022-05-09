def get_digit(num):
    if num < 10:
        print(num)
    else:
        get_digit(num // 10)
        print(num)


get_digit(123456)

"""
1
12
123
1234
12345
123456
"""