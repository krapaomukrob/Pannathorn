# s = int(input("score : "))

# if s <= 10 :               print("ไม่ผ่าน")
# elif s <= 20 and s > 10 :  print("ปรับปรุง")
# elif s <= 30 and s > 20 :  print("ดีมาก")

a = int(input("work score :"))
b = int(input("midterm score : "))
c = int(input("final score : "))

s = a + b + c 
print()

if s >= 0 and s < 50:   print("grade : F")
elif s >= 50 and s < 55: print("grade : D")
elif s >= 55 and s < 60: print("grade : D+")
elif s >= 60 and s < 65: print("grade : C")
elif s >= 60 and s < 65: print("grade : C+")
elif s >= 65 and s < 70: print("grade : B")
elif s >= 75 and s < 80: print("grade : B+")
elif s >= 80 and s <= 100: print("grade : A")


