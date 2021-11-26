# -------------------------------------------------------------
# Create separate plots in different figures
# -------------------------------------------------------------

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


# Create a list of lists
sale_list.append(s_list)
sale_list.append(c_list)


# Plot the Scatter Plot
plt.figure('My Scatter Plot')
plt.title("Sales Vs Cost")
plt.xlabel("Sale")
plt.ylabel("Cost")
plt.scatter(s_list,c_list)
plt.savefig('01scatter.png')


# Plot the Boxplot
plt.figure('My Boxplot')
plt.title("Box Plot of Sales")
plt.ylabel("USD")
plt.boxplot(sale_list)
plt.savefig('01boxplot.png')

# Show plots
plt.show()

