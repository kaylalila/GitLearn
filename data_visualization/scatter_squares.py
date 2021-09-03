import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# s sets the size of the plot point
# edgecolor sets the color of outer circle
# c is self-defined color, set by RGB, range(0, 1)
plt.scatter(x_values, y_values, c = y_values, edgecolors=None, s = 10, 
                                cmap= plt.cm.Blues) # change color depth with values
plt.title("Number Squares", fontsize = 24)
plt.xlabel("Numbers", fontsize = 14)
plt.ylabel("Squares", fontsize = 14)

# label numbers along axis, but only where the data located, not from 0
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

# set range for each axis
plt.axis([0, 1100, 0, 1100000])

plt.show()

# cut the margin when saving the image
plt.savefig("NumberSquare.png", bbox_inches = 'tight')
