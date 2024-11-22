#[[x1,x2] , [y1, y2]]
#[[0 0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
x = int(input("What is the dimension along the x axis?"))
y = int(input("What is the dimension along the y axis?"))

List = []
for i in range(x):
    temp_list1 = []
    for j in range(y):
        num = int(input("Enter the no."))
        temp_list1.append(num)
    List.append(temp_list1)

print(List)