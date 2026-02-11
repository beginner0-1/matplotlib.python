import matplotlib.pyplot as plt

x=[10,20,30,40]
y=[34,45,67,87]

plt.plot(x,y,color="red",marker="o")
plt.xlabel("room number")
plt.ylabel("students")
plt.title("simple graph")

plt.show()