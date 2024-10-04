import glob
import imagehash
from PIL import Image
import cv2
import numpy as np

boy_img_url = 'Boys/ayush.jpg'

boy_hash = imagehash.average_hash(Image.open(boy_img_url))

j = glob.glob('Girls/*')
selected = j[0]
accepted_diff = 100

for i in j:
    girl_hash = imagehash.average_hash(Image.open(i))
    diff = boy_hash - girl_hash
    if diff > accepted_diff:
        selected = i
        accepted_diff = diff

img = cv2.imread(boy_img_url)
boy_img = cv2.resize(img, (500, 600))

img = cv2.imread(selected)
girl_img = cv2.resize(img, (500, 600))

final_img = Image.new('RGB', (boy_img.shape[1] + girl_img.shape[1], boy_img.shape[0]))

final_img.paste(Image.fromarray(boy_img), (0, 0))
final_img.paste(Image.fromarray(girl_img), (boy_img.shape[1], 0))
final_img.save('Final_Frame.jpg')
final_img.show()
