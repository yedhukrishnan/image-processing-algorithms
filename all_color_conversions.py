from rgbcmy import *
from rgbhsi import *
from rgbyiq import *
from rgbycbcr import *


rgb = misc.imread('kid.jpg')
cmy = 255 - rgb
hsi = rgb_to_hsi(rgb)
ycbcr = convert_to_ycbcr(rgb)
yiq = convert_to_yiq(rgb)

f, a = plt.subplots(4, 2)
a[0, 0].imshow(rgb)
a[1, 0].imshow(rgb)
a[2, 0].imshow(rgb)
a[3, 0].imshow(rgb)
a[0, 1].imshow(cmy)
a[1, 1].imshow(hsi)
a[2, 1].imshow(ycbcr)
a[3, 1].imshow(yiq)

a[0, 0].set_title('RGB')
a[1, 0].set_title('RGB')
a[2, 0].set_title('RGB')
a[3, 0].set_title('RGB')

a[0, 1].set_title('CMY')
a[1, 1].set_title('HSI')
a[2, 1].set_title('YCbCr')
a[3, 1].set_title('YIQ')

plt.show()
