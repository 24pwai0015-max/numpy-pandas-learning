# grid lines
import matplotlib.pyplot as plt
months = ['January', 'February', 'March', 'April', 'May']
sales = [1400, 2344, 1232, 1456, 5556]
'''Grid lines are the background lines on a chart that help your eyes trace values 
accurately.'''
plt.plot(months,sales)
plt.title('use of grid lines')
plt.grid(True,
         axis='x',
         color='#000000',
         alpha=0.7,
         linewidth=0.7,
         linestyle='--')
plt.show()


plt.plot(months,sales)
plt.title('use of grid lines')
plt.grid(True,
         axis='y',
         color='#000000',
         alpha=0.7,
         linewidth=0.7,
         linestyle='--')
plt.show()

plt.plot(months,sales ,color="#E61010")
plt.title('use of grid lines')
plt.grid(True,
         axis='both',
         color='#000000',
         alpha=0.7,
         linewidth=0.5,
         linestyle='--')
plt.show()



