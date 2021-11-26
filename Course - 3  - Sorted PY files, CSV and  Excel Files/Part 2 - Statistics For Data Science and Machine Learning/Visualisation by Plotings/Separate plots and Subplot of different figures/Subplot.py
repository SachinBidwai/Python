# ------------------------------------------------------------
# Create the subplots of multiple plots in one figure
# ------------------------------------------------------------

# Import pyplot
import matplotlib.pyplot as plt


# Open the file in read mode and read lines
f = open('salesdata2.csv','r')
salefile = f.readlines()


# Create the sales List
sale_list = []
s_list = []
c_list = []


# Append all the records from the file to the saleslist
for records in salefile:
    sale, cost = records.split(sep=',')
    s_list.append(int(sale))
    c_list.append(int(cost))


# Create list of lists
sale_list.append(s_list)
sale_list.append(c_list)


# Subplot 1 for Scatter Plot
plt.subplot(2,2,1)
plt.title("Sales Vs Cost")
plt.xlabel("Sale")
plt.ylabel("Cost")
plt.scatter(s_list,c_list)

# Subplot 2 for Boxplot
plt.subplot(2,2,2)
plt.title("Box Plot of Sales")
plt.ylabel("USD")
plt.boxplot(sale_list)
plt.show()

# Subplot 3 for Histogram of sales
plt.subplot(2,2,3)
plt.title("Histogram of Sales")
plt.ylabel("USD")
plt.hist(s_list, bins=5, rwidth=0.9)

# Subplot 4 for lineplot of stock
x_days  = [1,2,3,4,5]
y_price1 = [9,9.5,10.1,10,12]

plt.subplot(2,2,4)
plt.title("Stockprice History")
plt.ylabel("Price")
plt.xlabel("Day")
plt.plot(x_days, y_price1)

# tight_layout to avoid overlap
plt.tight_layout()

# Save the figure as the png picture file
plt.savefig('01subplot.png')

# Show the plots
plt.show()
