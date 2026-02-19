import matplotlib.pyplot as plt 

n = int(input("enter number of student: "))

names =  []
marks = []
percentage = []

for i in range(n):
    name = input("enter student name : ")
    mark = int(input("enter marks out of 500 :"))

    names.append(name)
    marks.append(mark)

    per =(mark/500)*100
    percentage.append(per)

print("\n---Result---") 

for i in range(n):
    print(names[i],"percentage:", percentage[i])

    if percentage[i]>=40:
        print("status: pass")
    else:
        print("status; Fail") 

topper_index = marks.index(max(marks))
print("\n Topper is:" , names[topper_index])   


plt.bar(names, percentage)
plt.xlabel("students")
plt.ylabel("percentage")
plt.title("student performance analysis")
plt.show()

