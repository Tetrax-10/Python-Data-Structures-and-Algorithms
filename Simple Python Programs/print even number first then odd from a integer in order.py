"""
Ques : A Integer will be given we should print all the even numbers first and then odd
       numbers without changing the order.

Sample Input  : 123456789
Sample Output : 246813579

Sample Input  : 76149872348
Sample Output : 64824871973

"""

num = int(input())

even, odd, oddCount = 0, 0, 0
times = len(str(num))
while(times):
    i = (num // 10**(times-1)) % 10
    if(i % 2 == 0):
        even = (even*10) + i
    else:
        odd = (odd*10) + i
        oddCount += 1
    times -= 1

print(even*(10**oddCount) + odd)
