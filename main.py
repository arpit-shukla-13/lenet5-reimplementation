import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 1. MNIST Dataset ko Load karna
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

print(f"Training data shape: {x_train.shape}") # (60000, 28, 28)
print(f"Training labels shape: {y_train.shape}") # (60000,)
print(f"Test data shape: {x_test.shape}")       # (10000, 28, 28)


plt.imshow(x_train[0], cmap='gray')
plt.title(f"Label: {y_train[0]}")
plt.show()


x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0


x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

print(f"New training data shape: {x_train.shape}") # (60000, 28, 28, 1)

# 4. Encoding Labels (One-hot encoding)
# 5 -> [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
num_classes = 10
y_train = tf.keras.utils.to_categorical(y_train, num_classes)
y_test = tf.keras.utils.to_categorical(y_test, num_classes)

print(f"Sample label before one-hot encoding: 5")
print(f"Sample label after one-hot encoding: {y_train[5]}")

print("\n✅ Data loading and preparation complete!")