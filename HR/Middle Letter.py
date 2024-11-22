
Position = 0
Length = 0
Letter = ""


def mid (Name):
    if len(Name) % 2 != 0:
        global Position, Length, Letter
        Length = len(Name) +1
        Position = Length//2
        Letter = Name[Position-1]
        return Letter
    else:
        print("")

Name = str(input("Enter the string you want to get the middle Letter: "))
mid(Name)
print(Letter)
