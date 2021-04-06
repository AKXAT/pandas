import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#Seaborn has some inbuild datasets which you can load
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
iris = sns.load_dataset('iris')
'''#print(tips.head())
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
# - Let's First create set up or data input on which we are going to plot the MATRIX PLOTS 
tc = tips.corr()
sns.heatmap(tc,annot=True,cmap='coolwarm')
fm = flights.pivot_table(index='month',columns='year',values='passengers')
sns.heatmap(fm,linecolor='white',linewidth='1')
# - Let's now see how a **CLUISTER MAP** looks like. It's basically cluster of Heat Map
sns.clustermap(fm)
# REGRESSION PLOT 
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'])
# GRID
var = sns.PairGrid(iris)
var.map(plt.scatter)
# if you want to specify what to mention on the diagonal 
var.map_diag(sns.distplot)
var.map_upper(plt.scatter)
var.map_lower(sns.kdeplot)
# Facet Grid 
g = sns.FacetGrid(data=tips,col='time',row='smoker')
g.map(sns.displot,'total_bill')
#Style and Color 
sns.set_style(style='darkgrid') # to set the background
sns.despine(left=True,bottom=True) # to remove the peaks 
#plt.figure(figsize=(12,12))
sns.set_context('poster')
sns.countplot(x='sex',data=tips)
'''
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm')
plt.show()
