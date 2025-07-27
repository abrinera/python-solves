c= input("camelCase: ")
print("snake_case: ", end="")
for i in c:
    if i.isupper():
        low="_"+i.lower()
        print(low, end="")
    else:
        print(i, end="")

