# check if we are current dir
import os
import pandas as pd
import matplotlib.pyplot as plt
import json


print("Current directory:", os.getcwd())

# check if the data folder exists
data_folder = "data/sales.csv"
if os.path.exists(data_folder):
    print("Yes, the file exists.")
else:    
    print("Data file does not exist. Please create the file and add the sales data.")

sales_data = pd.read_csv("data/sales.csv", sep='\t', on_bad_lines="skip")



sales_data['total'] = sales_data['Quantity'] * sales_data['Unit_Price']
print("\nWith Total:")
print(sales_data.head())

os.makedirs('output', exist_ok=True)
sales_data.to_csv('output/sales_with_total.csv', index=False)

# Save as different formats
# 1. Excel
sales_data.to_excel('output/sales_calculated.xlsx', index=False)

# 2. JSON
sales_data.to_json('output/sales_calculated.json', orient='records', lines=True)



# Read the sales data from the CSV file
print("Sales data loaded successfully.")
print(sales_data.head())
# Analyze the sales data
total_sales = sales_data['Revenue'].sum()0
average_sales = sales_data['Revenue'].mean()
print(f"Total Sales: ${total_sales:.2f}")
print(f"Average Sales: ${average_sales:.2f}")





# Plotting the sales data
plt.figure(figsize=(10, 6))   
plt.plot(sales_data['Date'], sales_data['Revenue'], marker='o')
plt.title('Sales Over Time')  
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Save the analysis results to a JSON file
analysis_results = {
    
    "total_sales": int(total_sales) ,
    "average_sales": float(average_sales)
}
with open('analysis_results.json', 'w') as json_file:
    json.dump(analysis_results, json_file)
    
print("Analysis results saved to analysis_results.json")


