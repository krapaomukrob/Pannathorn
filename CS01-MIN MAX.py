totalnum = []
for i in range(int(input("quantity of data : "))):
    n = int(input("Enter data{} : ".format(i+1)))
    totalnum.append(n)

print()
print(totalnum)
print()
print(max(totalnum))
print(min(totalnum))