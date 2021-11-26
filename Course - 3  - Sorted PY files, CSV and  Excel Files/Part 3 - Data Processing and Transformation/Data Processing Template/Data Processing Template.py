# --------------------------------------------------
# Data processing template
# --------------------------------------------------

# Import libraries
import pandas as pd

# Read data from the csv file
dataset = pd.read_csv('loan_small.csv')


# Read data from the tsv (Tab Seperated) file
dataset_tab = pd.read_csv('loan_small_tsv.txt', sep='\t')


# Access the data using iloc. 
# Example - Get first three rows from the second and third column
subset = dataset.iloc[0:3, 1:3]


# Access the data using column names
# Get all rows of the column Gender and ApplicantIncome
subsetN = dataset[['Gender', 'ApplicantIncome']]



# Get first three rows of the columns Gender and ApplicantIncome
subsetN = dataset[['Gender', 'ApplicantIncome']][0:3]



# display a small set of data for quick check on a large data
dataset.head(10)


# Get the Shape of the dataframe (Row x Columns)
dataset.shape


# Get column names of the dataframe
dataset.columns


# Store column names of the dataframe in a list
column_list = dataset.columns.to_list()


# -------------------------------------------------------------
# Handling missing values
# -------------------------------------------------------------

# Find out columns with missing values with their count
dataset.isnull().sum(axis=0)



# Drop all the rows with missing values
dataset_clean = dataset.dropna()


# Drop all the rows with missing values of a particular column 
dataset_clean = dataset.dropna(subset=["Loan_Status"])


# Replace missing categorical values using column names
dt = dataset.copy()
cols = ['Gender', 'Area', 'Loan_Status']


# fillna for filling NaN values
dt[cols] = dt[cols].fillna(dt.mode().iloc[0])
dt.isnull().sum(axis=0)


# Replace missing numerical values using column names
cols2 = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']


# fillna for filling NaN values
dt[cols2] = dt[cols2].fillna(dt.mean())
dt.isnull().sum(axis=0)


#
# ---------------------------------------------------------
# label encoding - Convert Categorical to Numerical values
# ---------------------------------------------------------

# Get datatypes of all the columns of the dataframe
dt.dtypes


# Convert string/object column types to categorical 
dt[cols] = dt[cols].astype('category')


# Convert string to numerical codes
for columns in cols:
    dt[columns] = dt[columns].cat.codes



# ---------------------------------------------------------
# Hot encoding or Dummy Variable Creation
# ---------------------------------------------------------

# Drop a column using column name
df2 = dataset.drop(['Loan_ID'], axis=1)


# using get_dummies function of Pandas
df2 = pd.get_dummies(df2)


# Avoid dummy variable trap using drop_first
df3 = dataset.drop(['Loan_ID'], axis=1)
df3 = pd.get_dummies(df3, drop_first=True)


# ---------------------------------------------------------
# Data Normalization using Standardscaler and MinMax 
# ---------------------------------------------------------

# extract data to scale
data_to_scale = dataset_clean.iloc[:, 2:5]


# Import the StandardScaler class
from sklearn.preprocessing import StandardScaler


# Create an object of the class StandardScaler
scaler = StandardScaler()


# Fit and Transform the data for normalization
ss_scaler = scaler.fit_transform(data_to_scale)


# MinMax Normalization of the data
from sklearn.preprocessing import minmax_scale


# Fit and Transform the data for MinMax normalization
mm_scaler = minmax_scale(data_to_scale)

# ----------------------------------------------------------
# Split the Data by rows and columns
# ----------------------------------------------------------
df = dataset.copy()


# Split by column for X(independent) and Y(dependent) variables
X = df.iloc[:, :-1]
Y = df.iloc[:,  -1]


# Split by rows for training and test datasets
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test =      train_test_split(X, Y, test_size=0.3, random_state=1234)

