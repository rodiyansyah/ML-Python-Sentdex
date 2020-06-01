import tensorflow as tf

tf.compat.v1.disable_eager_execution()

x1 = tf.constant(5)
x2 = tf.constant(6)
result = tf.multiply(x1,x2)
print(result)

with tf.compat.v1.Session() as sess:
    output = sess.run(result)
    print(output)

    with tf.device('/gpu:1'):
        matrix1 = tf.constant([[3., 3.]])
        matrix2 = tf.constant([[2.],[2.]])
        product = tf.matmul(matrix1, matrix2)
        print(product)