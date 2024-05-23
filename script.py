from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# create your figure here
plt.figure(figsize=(12, 8))

# Subplot 1
ax1 = plt.subplot(1,2,1)
x_values = range(len(months))
plt.plot(x_values, visits_per_month, marker='s')
plt.title('Number of Visits Over the Past Year')
plt.xlabel('Month')
plt.ylabel('Number of Visits')
plt.xticks(x_values)
ax1.set_xticklabels(months)

# Subplot 2
ax2 = plt.subplot(1,2,2)
plt.plot(x_values, key_limes_per_month, c='green')
plt.plot(x_values, persian_limes_per_month, c='orange')
plt.plot(x_values, blood_limes_per_month, c='brown')
plt.legend(['Key Limes', 'Persian Limes', 'Blood Limes'], loc=1)
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
plt.title('Numbers of limes of different species sold each month')
plt.xlabel('Month')
plt.ylabel('Number of Sales')

# Adjust margin, save and display plots
plt.subplots_adjust(wspace=0.5)
plt.savefig('sublimes_lime_graphs.png')
plt.show()
plt.clf()