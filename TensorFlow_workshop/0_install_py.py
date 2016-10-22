import tensorflow as tf
hello = tf.constant('It works!')
sess = tf.Session()
print(sess.run(hello))
print("You have version %s" % tf.__version__)


import pylab
import numpy as np
import matplotlib as plt
plt.interactive(False)

# create some data using numpy. y = x * 0.1 + 0.3 + noise
x_train = np.random.rand(100).astype(np.float32)
noise = np.random.normal(scale=0.01, size=len(x_train))
y_train = x_train * 0.1 + 0.3 + noise

# plot it
pylab.plot(x_train, y_train, '.')
plt.pyplot.show()