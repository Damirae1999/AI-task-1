import torch
import matplotlib.pyplot as plt
import numpy as np

def load_mnist_images(filepath):
    with open(filepath, 'rb') as f:
        f.read(16)
        return np.frombuffer(f.read(), dtype=np.uint8).reshape(-1, 28, 28)

def load_mnist_labels(filepath):
    with open(filepath, 'rb') as f:
        f.read(8)
        return np.frombuffer(f.read(), dtype=np.uint8)

# Load from keras (download from keras equivalent)
x_train = load_mnist_images(r'C:\Users\Administrator\mnist\train-images.idx3-ubyte')
y_train = load_mnist_labels(r'C:\Users\Administrator\mnist\train-labels.idx1-ubyte')
x_test  = load_mnist_images(r'C:\Users\Administrator\mnist\t10k-images.idx3-ubyte')
y_test  = load_mnist_labels(r'C:\Users\Administrator\mnist\t10k-labels.idx1-ubyte')

# Normalize 0-1
x_train = x_train.astype('float32') / 255.0
x_test  = x_test.astype('float32')  / 255.0

# Display
print("Training Data shape:", x_train.shape)
print("Train labels shape:", y_train.shape)
print("Test Data shape:", x_test.shape)
print("Test labels shape:", y_test.shape)
# Display first 9 images
fig, axes = plt.subplots(3, 3, figsize=(6, 6))
for i, ax in enumerate(axes.flat):
    ax.imshow(x_train[i], cmap='gray')
    ax.set_title(f"Label: {y_train[i]}")
    ax.axis('off')
plt.suptitle("MNIST Training Images", fontsize=16)
plt.tight_layout()
plt.show()