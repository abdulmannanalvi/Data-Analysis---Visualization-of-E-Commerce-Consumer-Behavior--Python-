import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_data.csv')

print(df.head())
print(df.describe())
print(df.isnull().sum())


# Check the data types of the columns
print(df.dtypes)

subcategory_sales = df.groupby('Product_Subcategory')['Product_Sold'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=subcategory_sales, y=subcategory_sales.index)
plt.title('Top 10 Subcategories by Units Sold')
plt.xlabel('Units Sold')
plt.ylabel('Subcategory')
plt.show()
