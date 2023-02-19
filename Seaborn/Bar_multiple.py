import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

path = "your CSV's path"
df = pd.read_csv(path)
print(df)
last_row = df.tail(5) # use x number of row form last in df
print(last_row)

fig, (graph1,graph2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5)) # make subplot to display 2 graph (graph1,graph2)

#config graph1
sns.barplot(data=last_row, x=last_row.index, y='Temperature', color='red', ax=graph1)
graph1.set_title('Temparature')

#config graph2
sns.barplot(data=last_row, x=last_row.index, y='Humidity', color='blue', ax=graph2)
graph2.set_title('Humidity')

plt.show()