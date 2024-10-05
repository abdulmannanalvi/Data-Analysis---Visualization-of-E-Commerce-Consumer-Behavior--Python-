import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_data.csv')

print(df.head())
print(df.describe())
print(df.isnull().sum())


# Check the data types of the columns
print(df.dtypes)

# Check for non-numeric entries in 'Product_Sold'
print(df['Product_Sold'].unique())
df['Product_Sold'] = pd.to_numeric(df['Product_Sold'], errors='coerce')
# Option 1: Fill NaN values with 0
df['Product_Sold'].fillna(0, inplace=True)

# Option 2: Drop rows with NaN values in 'Product_Sold'
df.dropna(subset=['Product_Sold'], inplace=True)
# Now this line should work without error
top_sold_products = df.groupby('Product_Name')['Product_Sold'].sum().sort_values(ascending=False).head(10)

# Plot the top sold products
plt.figure(figsize=(10,6))
sns.barplot(x=top_sold_products, y=top_sold_products.index)
plt.title('Top 10 Most Sold Products')
plt.xlabel('Units Sold')
plt.ylabel('Product Name')
plt.show()


