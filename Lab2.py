from skimage.measure import shannon_entropy
from scipy.stats import entropy
from PIL import Image
from collections import Counter
import numpy as np


def read_image(path):
    try:
        image = Image.open(path)
        return image
    except IOError:
        print("Cannot open image")
        exit(0)


def kl_divergence(image_p, image_q):
    p = list(image_p.getdata())
    q = list(image_q.getdata())
    cp = Counter(p)
    cq = Counter(q)
    size = np.multiply(*image_p.size)
    pk = np.zeros(256)
    qk = np.zeros(256)
    for i in cp:
        pk[i] = cp[i] / size
    for i in cq:
        qk[i] = cq[i] / size

    return entropy(q, p)


img = read_image("photo1.bmp")
ent = shannon_entropy(img)
width, height = img.size
disc_img_2 = img.resize((int(width/np.sqrt(2)), int(height/np.sqrt(2))))
disc_img_4 = img.resize((int(width/2), int(height/2)))
quant_img_8 = img.convert("P", palette=Image.ADAPTIVE, colors=8)
quant_img_16 = img.convert("P", palette=Image.ADAPTIVE, colors=16)
quant_img_64 = img.convert("P", palette=Image.ADAPTIVE, colors=64)
disc_img_2.save("di2.bmp")
disc_img_4.save("di4.bmp")
quant_img_8.save('qi8.bmp')
quant_img_16.save("qi16.bmp")
quant_img_64.save("qi64.bmp")
entdi2 = shannon_entropy(disc_img_2)
entdi4 = shannon_entropy(disc_img_4)
entqi8 = shannon_entropy(quant_img_8)
entqi16 = shannon_entropy(quant_img_16)
entqi64 = shannon_entropy(quant_img_64)
print("Source entropy = {}".format(ent))
print("Sampled by 2 entropy = {}".format(entdi2))
print("Sampled by 4 entropy = {}".format(entdi4))
print("Quantized with 8 levels entropy = {}".format(entqi8))
print("Quantized with 16 levels entropy = {}".format(entqi16))
print("Quantized with 64 levels entropy = {}".format(entqi64))
restdi2l = disc_img_2.resize((width, height), resample=Image.BILINEAR)
restdi2c = disc_img_2.resize((width, height), resample=Image.BICUBIC)
restdi4l = disc_img_4.resize((width, height), resample=Image.BILINEAR)
restdi4c = disc_img_4.resize((width, height), resample=Image.BICUBIC)
restdi2l.save("restored2L.bmp")
restdi2c.save("restored2C.bmp")
restdi4l.save("restored4L.bmp")
restdi4c.save("restored4C.bmp")
relentrestdi2c = kl_divergence(img, restdi2c)
relentrestdi2l = kl_divergence(img, restdi2l)
relentrestdi4c = kl_divergence(img, restdi4c)
relentrestdi4l = kl_divergence(img, restdi4l)
relentqi8 = kl_divergence(img, quant_img_8)
relentqi16 = kl_divergence(img, quant_img_16)
relentqi64 = kl_divergence(img, quant_img_64)
print("Relative entropy for restored by 2 image (bilinear) = {}".format(relentrestdi2l))
print("Relative entropy for restored by 2 image (bicubic) = {}".format(relentrestdi2c))
print("Relative entropy for restored by 4 image (bilinear) = {}".format(relentrestdi4l))
print("Relative entropy for restored by 4 image (bicubic) = {}".format(relentrestdi4c))
print("Relative entropy for quantized with 8 image = {}".format(relentqi8))
print("Relative entropy for quantized with 16 image = {}".format(relentqi16))
print("Relative entropy for quantized with 64 image = {}".format(relentqi64))