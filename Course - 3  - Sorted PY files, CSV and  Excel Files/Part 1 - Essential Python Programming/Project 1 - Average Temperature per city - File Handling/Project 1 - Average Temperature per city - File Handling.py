# -------------------------------------------------------
# Exercise to print the Average Temperature per city
# -------------------------------------------------------
#

# Open the file
cityTemp = open("citytemp.csv")


# Read the first record and split into variables
rec1 = cityTemp.readline()
city, temperature, unit = rec1.split(',')
prev_city = city


# Position the pointer to the first record
cityTemp.seek(0)

# Initialise the variables
tempSum = 0.0
count = 0
averageTemp = 0.0


# Run the loop to read all the records and do the processing
for records in cityTemp:
    records = records.rstrip('\n')
    city, temperature, unit = records.split(',')
    
    if unit == "C":
        temperature = (float(temperature) * 9/5) + 32

    if city != prev_city:
        averageTemp = tempSum/count
        print(prev_city + "  " + str(round(averageTemp,2)))
        prev_city = city
        tempSum = 0.0
        count = 0
        averageTemp = 0.0
    tempSum = tempSum + float(temperature)
    count = count + 1
else:
    averageTemp = tempSum/count
    print(prev_city + "  " + str(round(averageTemp,2)))

