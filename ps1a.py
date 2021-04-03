n = int(input("Enter n: "))
B = int(input("Enter lower bound: "))
p = 0
T = 1
equation = 0
for i in range(1,n+1):
    if i%2 == 0:
        p = (2**i)+1
    else:
        p = (3**i)+1
    equation += p**(n-i)*T
while equation*T <= B:
    T += 1
if T >= 10000:
    print(-1)
else:
    print(T)

