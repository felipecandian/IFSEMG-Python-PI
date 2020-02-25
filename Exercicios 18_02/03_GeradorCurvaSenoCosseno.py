#
# @felipecandian
#

import matplotlib.pyplot as plt  #A biblioteca matplotlib tem que está instalada 
import numpy as np               #A biblioteca numpy tem que está instalada 

x = np.arange(0,1*np.pi-1,0.1)   
y = np.sin(x) #seno
z = np.cos(x) #cosseno

plt.plot(x,y,x,z)
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 4pi')
plt.legend(['seno(x)', 'cosseno(x)'])      
plt.show()

