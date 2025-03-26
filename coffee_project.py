# Open CSV
import pandas as pd
data = pd.read_csv('Coffee_company.csv')
print(data.head())
# Round up Units sold
data['Units Sold'] = data['Units Sold'].astype(int)
print(data.head())
# Check exact name of each columns
print (data.columns)
# Change the column name Month Name to Month 
data.rename (columns = {'Month Name':'Month'}, inplace = True)
data.head()
# Remove space in column name
data.columns = data.columns.str.strip()
# Removing unnecessary characters from Sales
data['Sales'] = pd.to_numeric(data['Sales'].str.replace(',','',regex = False).str.replace('$','',regex = False), errors = 'coerce')
# Change data type of Sales
data ['Sales'] = data['Sales'].astype(float)
print (data.head())
# Calculate total sales
total_sales = data['Sales'].sum()
print ("Total Sales: $", total_sales)
# Output: Total Sales: $ 408015039.62999994
# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'], format = '%d/%m/%y')
print (data.head())
# Set 'Date' as the index
data.set_index ('Date', inplace = True)
# Calculate quarterly sales
quarterly_sales = data['Sales'].resample('Q').sum().reset_index()
quarterly_sales.columns = ['Quarter','Total Sales']
print (quarterly_sales)