import cv2
import numpy as np
from collections import Counter
from urllib.request import urlopen
from sklearn.cluster import MiniBatchKMeans


def url_to_image(url):
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image


def getColorPalette(src, k=4, image_processing_size=(25, 25)):
    img = url_to_image(src)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # resize image if new dims provided
    if image_processing_size is not None:
        image = cv2.resize(hsv_img, image_processing_size,
                           interpolation=cv2.INTER_AREA)

    # reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    # cluster and assign labels to the pixels
    clt = MiniBatchKMeans(n_clusters=k, random_state=42)
    labels = clt.fit_predict(image)

    # count labels to find most popular
    label_counts = Counter(labels)

    # subset out most popular centroid
    centroids = clt.cluster_centers_
    centroids = centroids.astype(int)

    # hsv = tuple(centroids[label_counts.most_common()[0][0]])[::-1]
    # dominant_color = colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2])

    dominant_color = tuple(centroids[label_counts.most_common()[0][0]])

    palette = [
        tuple(centroids[label_counts.most_common()[1][0]]),
        tuple(centroids[label_counts.most_common()[2][0]]),
        tuple(centroids[label_counts.most_common()[3][0]])
    ]

    return dominant_color, palette


if __name__ == '__main__':

    dominant_color, palette = getColorPalette(
        src='https://images.unsplash.com/photo-1487530811176-3780de880c2d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80')

    response = {
        'dominantColor': str('hsv' + str(dominant_color)),
        'palette': [str('hsv' + str(ele)) for ele in palette]
    }

    print(response)
