import tensorflow as tf

with tf.Graph().as_default():
    c = tf.constant(1.5)
    x = tf.Variable(1.0, name="x")
    add_op = tf.add(x, c)
    assign_op = tf.assign(x, add_op)
    init = tf.initialize_all_variables()
    with tf.Session() as sess:
        sess.run(init)
        sess.run(assign_op)
        print(sess.run(x))