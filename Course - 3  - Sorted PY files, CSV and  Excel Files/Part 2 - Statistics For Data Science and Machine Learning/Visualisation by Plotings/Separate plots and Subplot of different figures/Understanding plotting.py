# ---------------------------------------------------------
# Understand basics of Plotting
# ---------------------------------------------------------

# Import pyplot from matplotlib
import matplotlib.pyplot as plt


# Create data to plot
x_days  = [1,2,3,4,5]
y_price1 = [9,9.5,10.1,10,12]
y_price2 = [11,12,10.5,11.5,12.5]


# Change the chart labels
plt.title("Stock Movement")
plt.xlabel("Week Days")
plt.ylabel("Price in USD")


# Create the plot
plt.plot(x_days, y_price1, label="Stock 1")
plt.plot(x_days, y_price2, label="Stock 2")
plt.legend(loc=2, fontsize=12)

# Show the Plot
plt.show()

