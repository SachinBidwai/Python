# -----------------------------------------------------------
# Print or store the Descriptive Statistical data
# -----------------------------------------------------------

# Import the library for statistical analysis
import statistics as st


# Create a list of data. This could even be taken from a file.
data = [1,2,3,3]


# Apply statistics functions to get various measures
mean = st.mean(data)
median = st.median(data)
mode = st.mode(data)
std_dev = st.stdev(data)
variance = st.variance(data)
