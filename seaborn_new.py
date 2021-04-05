import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#Seaborn has some inbuild datasets which you can load
tips = sns.load_dataset('tips')
print(tips.head())
# - Lets see the first plot type DIST PLOT. Its a way to see a uni-varaible distribution.
sns.displot(tips['total_bill'],kde='True')
# - Let's see Joint Plot, here we can combint two DIST plots
sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
# - Let's see Pairplot, here we plot pairwise relationship across the table. 
sns.pairplot(tips,hue='sex')
# - Let's See how RUG PLOT works. It just draws dash for every uniform variables.
sns.rugplot(tips['total_bill'])
# - Bar Plot is the most commont type of Categorical Plots that we can see. You can think this as the visualization of action
sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)
# COUNT PLOT is same as BAR PLOT insted it counts the occurance of values 
sns.countplot(x='sex',data=tips)
# BOX PLOT and VIOLEN PLOT Distribution of categorical data
sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')
#VIOLIN PLOT 
sns.violinplot(x='day',y='total_bill',data=tips)
# - STRIP PLOT 
sns.stripplot(x='day',y='total_bill',data=tips,jitter=True,hue='sex',dodge=True)
#SWARM PLOT is a comination of Violin Plot and the strip plot
sns.swarmplot(x='day',y='total_bill',data=tips)
# - Let's see about **FACTOR PLOT**, this is general form of all these plots
sns.catplot(x='day',y='total_bill',data=tips,kind='bar')
plt.show()

