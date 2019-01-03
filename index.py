import warnings
warnings.filterwarnings('ignore')

# imports
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt, numpy as np, pandas as pd
from sklearn.cluster import KMeans

plt.rcParams['figure.figsize'] = (12, 6)

df=pd.read_csv('driver-data.csv', sep='\s+')
df.head()

plt.figure()
plt.plot(df.Distance_Feature,df.Speeding_Feature,'ko')
plt.ylabel('Speeding Feature')
plt.xlabel('Distance Feature')
plt.ylim(0,100)
plt.show()

