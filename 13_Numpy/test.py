import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 20) #在0到3之間等距切成20個點
y = np.linspace(0, 9, 20) #相同的把0到9之間切成20個點
plt.plot(x, y)
#plt.plot(x, y, "ro")，加了第三個後會露點
plt.show()
