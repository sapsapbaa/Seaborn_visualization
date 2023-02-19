import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

path = "your CSV's path"
df = pd.read_csv(path)
print(df)

sns.lineplot(data=df, x=df.index, y='Temperature')
sns.lineplot(data=df, x=df.index, y='Humidity')
plt.ylim(0,60)
plt.show()