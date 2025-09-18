import pandas as pd
sales_data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],    
    'Sales': [2500, 3000, 2800, 3500, 4000, 4200, 4500, 4800, 5000, 5500, 6000, 6500],
    'Expenses': [1500, 1600, 1700, 1800, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700]    
}
df = pd.DataFrame(sales_data)
#Add profit column
df['Profit'] = df['Sales'] - df['Expenses']
print(df)
#Total sales

total_sales = df['Sales'].sum()
print("Total Sales in the year:", total_sales)
#Average sales
print("Average Sales:", total_sales/12)
#total expenses
total_expenses = df['Expenses'].sum()
print("Total Expenses in the year:", total_expenses)
#total profit
total_profit = df['Profit'].sum()
print("Total Profit in the year:", total_profit)
#moth with highest profit
max_profit_month = df.loc[df['Profit'].idxmax()]['Month']
print("Month with highest profit:", max_profit_month)