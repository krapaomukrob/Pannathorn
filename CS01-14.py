# car = ["ford", "volvo", "Toyota"]
# print(car)
# print(len(car))
# for i in range(3): print(car[i])

# a = ["Pannathorn", "Rasrikul", "44098"]      
# for i in range(len(a)):   print(a[i],end="\n\n")             

# fruit = ["apple", "banana", "mango"]
# for i in fruit:
#     if i != "banana":
#         print(i)

num = int(input("enter quantity of data : "))
numtotal = []
for i in range(num): 
    data = int(input("enter data : ")) 
    numtotal += [data]    
numtotal.sort()
print(numtotal)