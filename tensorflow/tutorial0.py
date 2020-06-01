import tensorflow as tf

#tf.compat.v1.Session(
#    target='', graph=None, config=None
#)
tf.compat.v1.disable_eager_execution()

param_x = tf.compat.v1.placeholder(dtype=tf.float32)
param_y = tf.compat.v1.placeholder(dtype=tf.float32)

op_x_plus_y = tf.add(param_x, param_y)

sess = tf.compat.v1.Session()

result = sess.run(op_x_plus_y, feed_dict={param_x: 20, param_y: 1.1})

#print(result)

magic_numbers = tf.compat.v1.placeholder(dtype=tf.int32, shape=[None])
offset = tf.compat.v1.placeholder(dtype=tf.int32)
magic_numbers_plus_offset = magic_numbers + offset
#
magic_numbers_plus_offset = sess.run(magic_numbers_plus_offset, feed_dict={offset: 10, magic_numbers: [62, 91, 98, 98, 101, 34, 22, 77, 101, 104, 98, 90, 23]})
print([chr(i) for i in magic_numbers_plus_offset])

#