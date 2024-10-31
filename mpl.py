import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [920,1100,1000,1350]
plt.plot(x,y)
plt.show()

legend = ["January", "February", "March", "April"]
plt.xticks(x, legend)
plt.plot(x,y)
plt.show()
plt.bar(x,y)
plt.ylabel("Sales in USD")
plt.title("Monthly Sales")
plt.show()