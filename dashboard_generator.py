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
#print("-----------------------")
#print("MONTH: March 2018")

#print("-----------------------")
#print("CRUNCHING THE DATA...")

#print("-----------------------")
#print("TOTAL MONTHLY SALES: " + monthly_total)

#print("-----------------------")
#print("TOP SELLING PRODUCTS:")
#print(df)


#print("-----------------------")
#print("VISUALIZING THE DATA...")

# Generate Bar Chart for data from Chart Gallery Exercise
#plt.barh(y_pos, views, align='center')
#plt.yticks(y_pos, genre)
#plt.xlabel("Product")
#plt.title("Monthly Sales (USD)")
#plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
#plt.show()