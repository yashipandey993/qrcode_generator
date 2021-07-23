import qrcode
import cv2
img = qrcode.make("India is a country with many religions. I love India")
img.save("C:/Users/yashi/Desktop/youtubeQR.jpg")
qr=cv2.imread("C:/Users/yashi/Desktop/youtubeQR.jpg")
cv2.imshow('QR',qr)
