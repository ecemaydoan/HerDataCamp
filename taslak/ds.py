import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df=sns.load_dataset("tips")
#print(df.head())


#SEABORN İLE VERİYİ GÖRSELLEŞTİRME
df["sex"].value_counts()
sns.countplot(x=df["sex"],data=df)
plt.title('seaborn')
plt.show()

#MATPLOTLIB İLE VERİYİ GÖRSELLEŞTİRME
df['sex'].value_counts().plot(kind='bar')
plt.title('Matplotlib')
plt.show()





#pd.set_option('display.max.columns',None)

#df = sns.load_dataset("titanic")



#df["sex"].value_counts().plot(kind='bar')
#plt.show()


#x=np.array([1,8])
#y=np.array([0,150])

#plt.plot(x,y,'o')
#plt.show()
