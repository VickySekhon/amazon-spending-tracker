import matplotlib as plt
import pandas as pd

# Read CSV file

path = 'C://Users/Vicky/Downloads/'
df = pd.read_csv(path)

# Initialization

# show relevant columns of data
pd.set_option('display.max_columns', 36)
# remove NaN values
df.fillna(0)

# Prepare values

# remove '$' from necessary calculation values and convert them into float
df["item_total"] = df["item_total"].str.replace("$", "").astype(float)
df["item_subtotal"] = df["item_subtotal"].str.replace("$", "").astype(float)
df["item_subtotal_tax"] = df["item_subtotal_tax"].str.replace("$", "").astype(float)

# Calculations

# total spending amount
df["item_total"].sum()
# max, min, mean, and median spending amounts
df["item_total"].max()
df["item_total"].min()
df["item_total"].mean()
df["item_total"].median()

# total spent on tax
df["item_subtotal_tax"].sum()
# calculate overall taxation rate paid **specific to Canada**
df["item_subtotal_tax"].sum() / df["item_subtotal"].sum() # tax rate = total tax ÷ taxable spending

# Plot data
# convert date times to standard format
df["order_date"] = pd.to_datetime(df["order_date"]).dt.date
bar = df.plot.bar(x="Order Date", y="Item Total", rot=0, color="rgb(0,20,175)")

plt.show()