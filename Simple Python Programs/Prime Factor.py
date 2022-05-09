a = int(input())
primeFactors = ""
print("\n\nSteps :")
for i in range(2, a+1):
    while a % i == 0 and a != 1:
        print(f"{a} % {i} = {a//i}")
        primeFactors += f"{i},"
        a = a//i
    if(a == 1):
        break
print(f"\n\n{primeFactors}")
