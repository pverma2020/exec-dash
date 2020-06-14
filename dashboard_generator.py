# dashboard_generator.py
import csv
import operator
import os
import pandas as pd
import matplotlib.pyplot as plt
import calendar
import datetime

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)  # > $12,000.71

#
#INPUT - PICK YOUR FILE & ERROR MESSAGE IF FILE DOESN'T EXIST
#

while True:
	year = input("Please enter the year of the sales data you wish to view (YYYY): ")
	month = input("Please enter the month of the sales data you wish to view (MM): ")
	csv_file_name = "sales-"+year+month+".csv" #data files should be named: (sales-YYYYMM.csv)
	csv_file_path = os.path.join("data/",csv_file_name)
    
	if not os.path.isfile(csv_file_path):
		print("Sorry, that file does not exist. Please make sure that you have added that .csv file in the 'Data' Subfolder.")
	else:
		break

#
#CALCULATIONS
#

#Monthly Total
csv_data = pd.read_csv(csv_file_path) #read the file
monthly_total = csv_data["sales price"].sum() #sum the monthly total
monthly_total = to_usd(monthly_total)
#print(monthly_total) #prints $12,000.71
#print(type(monthly_total)) #string - remember for output statement

#Top Selling Products
#need to remove duplicates but keep price - find a way to group and sort: (.groupby()/.sort_values)
#column options: "date","product","unit price","units sold","sales price"
#Project description only wants to show "Product" and "Sum of Sales Price"
df = pd.DataFrame(csv_data)
df.rename(columns = {"product":"Product"}, inplace = True) #Column Header: "Product"
df.rename(columns = {"sales price":"Sum of Sales Price"}, inplace = True) #Column Header: "Sum of Sales Price"

df = df.groupby(["Product"]).sum() #group by product
df = df[["Sum of Sales Price"]]
df = df.sort_values(by=["Sum of Sales Price"], ascending = False)
#print(df) #prints 2 columns: Product and Sum of Sales Price


#
#OUTPUTS
#

#TO DO: figure out how to change 03 to March; Utilize user input in some way since they put in month and year?
#got help from: https://www.pythonprogramming.in/how-can-i-get-the-month-name-from-the-month-number.html
#month_num = month
month_num = int(month) #convert month from line 19 into integer to run line 60
month_name = datetime.date(2015, month_num, 1).strftime('%B')
#print("MONTH:", month_name, year) 
#print(type(month_name)):string
#print(type(year)):string

#print("-----------------------")
#print("MONTH:", month_name, year) #"MONTH: March 2018"

#print("-----------------------")
#print("CRUNCHING THE DATA...")

#print("-----------------------")
#print("TOTAL MONTHLY SALES: " + monthly_total)

#print("-----------------------")
#print("TOP SELLING PRODUCTS:")
#print(df)


#print("-----------------------")
#print("VISUALIZING THE DATA...")
#lines 83-109 came from Professor's starter code which I just found when looking for resources for the chart:https://github.com/prof-rossetti/intro-to-python/blob/master/projects/exec-dash/pandas_matplotlib_solution.py
#the realization in line 82 would have been help 8 hours ago :(
product_names = csv_data["product"]
unique_product_names = product_names.unique()  # :-D
unique_product_names = unique_product_names.tolist()

# Accumulate total sales per product

top_sellers = []

for product_name in unique_product_names:
    matching_rows = csv_data[csv_data["product"] == product_name]
    product_monthly_sales = matching_rows["sales price"].sum()
    top_sellers.append(
        {"name": product_name, "monthly_sales": product_monthly_sales})


top_sellers = sorted(top_sellers, key=operator.itemgetter(
    "monthly_sales"), reverse=True)

#chart_title = "Top Selling Products (" + month_name + year +")""   # TODO: get month and year


sorted_products = []
sorted_sales = []

for d in top_sellers:
    sorted_products.append(d["name"])
    sorted_sales.append(d["monthly_sales"])

sorted_products.reverse()
sorted_sales.reverse()

plt.barh(sorted_products, sorted_sales)
plt.title(f"Top Selling Products ({month_name} {year})")
#plt.title(chart_title)
plt.xlabel("Monthly Sales (USD)")
plt.ylabel("Product")
plt.show() #show chart window

