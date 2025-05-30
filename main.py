import cv2
import sys

img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load failed')
    sys.exit()

if img1.ndim == 2:
    print('img1 is a grayscale image')

if len(img1.shape) == 2:
    print('img1 is a grayscale image')

##행렬식으로 값이 나옴
h, w = img1.shape
print('w x h = {} x {}'.format(w, h))

h, w = img2.shape[:2]
print('w x h = {} x {}'.format(w, h))

x = 20
y = 10
p = img1[y,x]
print(p)