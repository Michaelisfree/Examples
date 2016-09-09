from PIL import Image,ImageFont,ImageDraw,ImageFilter
import random

def ranchar():
    return chr(random.randint(65,90))
def  rancolor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def rancolor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
w=60*4
h=60
image=Image.new('RGB',(w,h),(255, 255, 255))
font=ImageFont.truetype("arial.ttf", 36)
draw=ImageDraw.Draw(image)

for i in range(1,w):
    for j in range(1,h):
        draw.point((i,j),fill=rancolor())

for i in range(0,4):
    draw.text((60*i+10,10),ranchar(),font=font,fill=rancolor2())
image.show()
image=image.filter(ImageFilter.BLUR)
image.save("abig news.jpg","jpeg")
#image.save('code.jpg', 'jpeg');

