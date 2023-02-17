X = 0
n = int(input(""))
for i in range(n):
    func = input("")
    if func == "X++" or func == "++X":
        X += 1
    else:
        X -= 1
print(X)