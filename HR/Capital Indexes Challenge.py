List =[]
def capital_indexes(Name):
    for i in range(len(Name)):
        if Name[i]== Name[i].upper():
            List.append(i)
    return List
Name = str(input("Enter name you want to check: "))
capital_indexes(Name)
print(List)