from PIL import Image, ImageDraw
im_list=[]

im = Image.new('RGB', (500, 300), (128, 128, 128))
draw = ImageDraw.Draw(im)
draw.ellipse((100, 100, 150, 200), fill=(255, 0, 0), outline=(0, 0, 0))
im_list.append(im)

im = Image.new('RGB', (500, 300), (128, 128, 128))
draw = ImageDraw.Draw(im)
draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
im_list.append(im)

im = Image.new('RGB', (500, 300), (128, 128, 128))
draw = ImageDraw.Draw(im)
draw.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)
im_list.append(im)

for num,i in enumerate(im_list):
    i.save('./output_files/'+str(num)+'.jpg', quality=95)