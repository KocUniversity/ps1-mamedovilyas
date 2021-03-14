n = int(input("Enter n: "))
B = int(input("Enter B: "))
p = 0
T = 1
equation = 0
low = 1
high = 10000
guess = (high+low)/2.0
for i in range(1,n+1):
    if i%2 == 0:
        p = (2**i)+1
    else:
        p = (3**i)+1
    equation += p**(n-i)*T
while equation*guess > B or equation*guess < B:
    if guess >= 10000:
        break
    if guess <= 1:
        break
    if equation*guess > B:
        high = guess
    else:
        low = guess
    guess=(high+low)/2
if int(guess) >= 10000:
    print(-1)
elif equation*int(guess) > B:
    T = int(guess)
    print(T)
else:
    T = int(guess)+1
    print(T)
