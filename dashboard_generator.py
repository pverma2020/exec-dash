# dashboard_generator.py
import operator
import os
import pandas as pd
import matplotlib.pyplot as plt

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)  # > $12,000.71

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")

# Generate Bar Chart for data from Chart Gallery Exercise
genre = [x["genre"] for x in bar_data]
y_pos = np.arange(len(genre))
views = [y["viewers"] for y in bar_data]
plt.barh(y_pos, views, align='center')
plt.yticks(y_pos, genre)
plt.xlabel("Product")
plt.title("Monthly Sales (USD)")
plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
plt.show()