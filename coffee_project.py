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
print (data['Date'].head())
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True, errors='coerce')
print (data.head())
# Set 'Date' as the index
data.set_index ('Date', inplace = True)
# Calculate quarterly sales
quarterly_sales = data['Sales'].resample('Q').sum().reset_index()
quarterly_sales.columns = ['Quarter','Total Sales']
print (quarterly_sales)
# Plotting the quarterly sales as a bar chart
import matplotlib.pyplot as plt
plt.figure (figsize = (10, 60))
plt.bar (quarterly_sales['Quarter'].dt.to_period('Q').astype(str), quarterly_sales['Total Sales'])
plt.title ('Quarterly Sales')
plt.xlabel ('Quarter')
plt.ylabel ('Total Sales')
plt.xticks (rotation = 45)
plt.tight_layout()
plt.show()