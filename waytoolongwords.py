nbr = int(input(""))
strig = []
for i in range(nbr):
    stri = input("")
    strig.append(stri)
for text in strig:    
    if len(text) > 10:
        print(text[0]+str(len(text)-2)+text[-1])
    else:
        print(text)