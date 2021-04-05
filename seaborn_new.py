import seaborn as sns
import matplotlib.pyplot as plt
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
plt.show()