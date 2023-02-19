import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

path = "your CSV's path"
df = pd.read_csv(path)
print(df)
last_row = df.tail(5) # use x number of row form last in df
print(last_row)

sns.barplot(data=last_row, x='Time', y='Temperature')
plt.ylim(0,None)
plt.show()