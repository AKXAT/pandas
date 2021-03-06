#FUNTIONAL 

import matplotlib.pyplot as plt 
import numpy as np 
x = np.linspace(0,5,11)
y = x**2 


plt.plot(x,y)
plt.xlabel('X lable')
plt.ylabel('Y lable')
plt.title('Test')

#add multi plots  
plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.plot(y,x,'b')



#OBJET ORIENTED 
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8]) 
axes.plot(x,y,'r') 
axes.set_xlabel('X Lable')
axes.set_ylabel('Y Lable')
axes.set_title('Test')

#add multitple plots
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes1.plot(x,y)
axes2.plot(y,x)
fig,axes = plt.subplots(nrows=1,ncols=2)
axes[0].plot(x,y)
axes[1].plot(y,x)

# Figures size and the DPI

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,2),dpi=200)
axes[0].plot(x,y)
axes[1].plot(y,x)


# Legend 
fig2 = plt.figure()
ax = fig2.add_axes([0,0,1,1])
ax.plot(x,x**2,label='X Square')
ax.plot(x,x**3,label='X Cube')
ax.legend()
plt.tight_layout()
plt.show()



# Appearnce and colours in the plot 
fig3 = plt.figure()
ax3 = fig3.add_axes([0,0,1,1])
ax3.plot(x,y,color='#ff8c00',linewidth=3,marker='o',markersize=20,
markerfacecolor='yellow',markeredgewidth=3,markeredgecolor='black')
plt.show()



# axis customization 
fig4 = plt.figure()
ax4 = fig4.add_axes([0,0,1,1])
ax4 = fig4.add_subplot(111)
ax4.plot(x,y,color='purple',linewidth=2,linestyle='--')
ax4.set_xlim([0,1])
ax4.set_ylim([0,1])
plt.show()

#special plot types. 
