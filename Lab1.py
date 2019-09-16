import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import shannon_entropy
from PIL import Image


def read_image(path):
    try:
        image = Image.open(path)
        return image
    except IOError:
        print("Cannot open image")
        exit(0)


def pixels(image):
    width, height = image.size
    return width * height


def hist(image, fmt):
    pix = np.asarray(list(image.getdata()))
    plt.hist(pix, 16)
    plt.title(fmt)
    plt.xlabel("group")
    plt.ylabel("frequency")
    x = [i for i in range(7, 256, 16)]
    plt.xticks(x, [i for i in range(16)])
    plt.show()


def entropy_formula(image):
    pix = np.asarray(list(image.getdata()))
    _, counts = np.unique(pix, return_counts=True)
    size = pixels(image)
    entropy = np.sum([(i / size) * np.log2(i / size) for i in counts if i != 0])
    return -entropy


def entropy_bultin(image):
    return shannon_entropy(image)


img1_jpg = read_image("photo1.jpeg")
img1_bmp = read_image("photo1.bmp")
img1_png = read_image("photo1.png")
img1_tiff = read_image("photo1.tiff")


print("JPEG\n entropy with formula is {f}, with built-in function is {b}".format(f=entropy_formula(img1_jpg),
                                                                                 b=entropy_bultin(img1_jpg)))
print("BMP\n entropy with formula is {f}, with built-in function is {b}".format(f=entropy_formula(img1_bmp),
                                                                                b=entropy_bultin(img1_bmp)))
print("PNG:\n entropy with formula is {f}, with built-in function is {b}".format(f=entropy_formula(img1_png),
                                                                                 b=entropy_bultin(img1_png)))
print("TIFF:\n entropy with formula is {f}, with built-in function is {b}".format(f=entropy_formula(img1_tiff),
                                                                                  b=entropy_bultin(img1_tiff)))

hist(img1_jpg, "JPEG")
hist(img1_bmp, "BMP")
hist(img1_png, "PNG")
hist(img1_tiff, "TIFF")

print("Image histograms can be seen on plots.")