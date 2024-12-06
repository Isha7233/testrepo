import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_excel(r"C:/Users/ishabeniwal/Downloads/crimes.xlsx")
neighborhood_summary = df['Neighborhood'].value_counts()
reporting_area_summary = df['Reporting Area'].value_counts()
plt.figure(figsize=(10, 6))
neighborhood_summary.plot.bar()
plt.title('Number of Crimes by Neighborhood')
plt.xlabel('Neighborhood')
plt.ylabel('Number of Crimes')
plt.xticks(rotation=45, ha='right')
plt.show()
