# Prediction
# Inference ---> Loss --> Training
# Goal : Maximize Accuracy and Minimize Loss
# y = W*x + b
import tensorflow as tf


# Interference

x = tf.placeholder(shape=[None], dtype=tf.float32, name="x")

W = tf.get_variable(shape=[], name ="W")

b = tf.get_variale(shape=[], name ="b")

y = W*x + b

# Run computation
with tf.Sesion() as sess:
    sess.run(tf.initialize_all_variables())
    print(sess.run(y, feed_dict={x: x_in}))

# Define Loss Function
# Loss = (expected - trained output)^2

loss = tf.reduce_mean(tf.square(y - y_train))


# Gradient Descent - How to tweak variable to minimize loss
# 0.5 : learning rate
optimizer = tf.train.GradientDescentOptimizer(0.5)

# Create an operation that minimizes loss
train = optimizer.minimize(loss)
