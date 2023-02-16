problems = int(input(""))
counter = 0
for n in range(problems):
    str = input("")
    str = str.split(" ")
    if str.count("1") >= 2:
        counter += 1
    else:
        continue
print(counter)    