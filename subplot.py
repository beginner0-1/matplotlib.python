# plt subplot(nrows,ncolumn ,index)

import matplotlib.pyplot as plt

x = [10,30,50,70]
y = [20,40,60,80]

plt.subplot(1,2,1)
plt.plot(x,y , color ="red")
plt.title("line plot")

plt.subplot(1,2,2)
plt.bar(x,y)
plt.title("bar chart")

plt.suptitle("compare between line and bar charts")

plt.tight_layout(rect=[0,0,1,0.95])
plt.show()