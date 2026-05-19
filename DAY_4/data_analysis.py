import pandas as pd
import matplotlib.pyplot as plt

data = {'Name': ['Shreyas','Karan','Krish','Harsh'],
        'Math': [92,78,85,90],
        'Science': [88,82,79,95]}

df = pd.DataFrame(data)
print(df.describe())

df.set_index('Name').plot(kind='bar', title='Student Marks')
plt.tight_layout()
plt.savefig('marks_chart.png')
print("Chart saved!")