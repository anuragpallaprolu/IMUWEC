#!/usr/bin/python
from numpy import *
from pylab import *
from matplotlib import rc, rcParams

# Read in data from an ASCII data table
data = genfromtxt('gyrox_n.txt')
data_f = genfromtxt('gyrox_n_e.txt')
#'data' is a matrix containing the columns and rows from the file
time   = data[:,0]  # Python indices are (row,col) as in linalg
gyrox = data[:,1]  # Creates arrays for first two columns
gyrox_f = data_f[:,1]
# Create a loglog plot of data
plot(time,gyrox)
plot(time,gyrox_f)
# Turn on a grid
grid(True)

# Save the figure in a separate file
savefig('read_and_plot_data.png')

# Draw the plot to the screen
show()
