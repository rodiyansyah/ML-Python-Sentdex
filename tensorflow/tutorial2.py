import tensorflow as tf
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

from keras.datasets import mnist

dodol = mnist.load_data()

print(train_images)

print(train_labels)