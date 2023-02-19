import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

path = "your CSV's path"
df = pd.read_csv(path)
print(df)

sns.lineplot(data=df, x=df.index, y='Temperature')
plt.ylim(0,40)
plt.show()