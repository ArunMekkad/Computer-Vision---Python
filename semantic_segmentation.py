import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
from skimage.segmentation import mark_boundaries
from sklearn.cluster import KMeans

# Load the image
image = imread('./segment_image.jpg')

# Convert the image to grayscale for Otsu's thresholding
gray_image = rgb2gray(image)

# Perform Otsu's thresholding
thresh = threshold_otsu(gray_image)
binary_otsu = gray_image > thresh

# Perform K-means clustering
image_reshape = np.reshape(image, (image.shape[0]*image.shape[1], image.shape[2]))
kmeans = KMeans(n_clusters=2, random_state=0).fit(image_reshape)
segments_kmeans = kmeans.labels_.reshape(image.shape[0], image.shape[1])

# Create color preserved segmented images
segmented_otsu = np.copy(image)
segmented_kmeans = np.copy(image)

# Draw boundaries on the segmented images
boundaries_otsu = mark_boundaries(segmented_otsu, binary_otsu, color=(0, 1, 0))  # Green boundaries
boundaries_kmeans = mark_boundaries(segmented_kmeans, segments_kmeans, color=(0, 1, 0))  # Green boundaries

# Display the original and segmented images
fig, ax = plt.subplots(2, 3, figsize=(15, 10), sharex=True, sharey=True)

ax[0, 0].imshow(image)
ax[0, 0].set_title('Original Image')
ax[0, 0].axis('off')

ax[0, 1].imshow(segmented_otsu)
ax[0, 1].set_title('Segmented Image - Otsu')
ax[0, 1].axis('off')

ax[0, 2].imshow(segmented_kmeans)
ax[0, 2].set_title('Segmented Image - K-means')
ax[0, 2].axis('off')

ax[1, 0].imshow(image)
ax[1, 0].set_title('Original Image')
ax[1, 0].axis('off')

ax[1, 1].imshow(boundaries_otsu)
ax[1, 1].set_title('Segmented Image with Boundaries (Otsu)')
ax[1, 1].axis('off')

ax[1, 2].imshow(boundaries_kmeans)
ax[1, 2].set_title('Segmented Image with Boundaries (K-means)')
ax[1, 2].axis('off')

plt.tight_layout()
plt.show()
