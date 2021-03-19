from PIL import Image, ImageFilter

image1 = Image.open("D:\Projects\Python-Projects\data\pokedex\squirtle.jpg")
image2 = Image.open('D:/Projects/Python-Projects/data/pokedex/pikachu.jpg')
print(image1)
print(image1.format)
print(image1.size)
print(image1.mode)
print(dir(image1))

converted_image = image2.convert('L')
# converted_image.save('./data/pokedex/gray_pikachu.png', 'png')
filtered_img1 = image1.filter(ImageFilter.BLUR)
# filtered_img1.save('D:/Projects/Python-Projects/data/pokedex/blur_squirtle.png', 'png')

filtered_img2 = image2.filter(ImageFilter.SMOOTH)
# filtered_img2.save('D:/Projects/Python-Projects/data/pokedex/smooth_pikachu.png', 'png')

filtered_img3 = image2.filter(ImageFilter.SHARPEN)
# filtered_img3.save('D:/Projects/Python-Projects/data/pokedex/sharp_pikachu.png', 'png')

# converted_image.show()

rotate_90 = filtered_img1.rotate(90)
# rotate_90.show()
# rotate_90.save('./data/pokedex/squirtle_90.png','png')

resized = image1.resize((300,300))
# resized.save('./data/pokedex/resized_squirtle.png','png')

box = (100, 100, 400,400)
cropped = image2.crop(box)
# cropped.show()
# cropped.save('./data/pokedex/cropped_pikachu.png','png')

image3 = Image.open('D:/Projects/Python-Projects/data/pokedex/charmander.jpg')
image3.thumbnail((200,200)) # Let's you specify the max size but adjusts exact dims to keep aspect ratio unlike .resize()
image3.save('D:/Projects/Python-Projects/data/pokedex/thumb_charmander.png', 'png')