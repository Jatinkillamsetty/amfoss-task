from PIL import Image, ImageDraw, ImageFont
img = Image.new('RGB', (200, 50), color=(255, 255, 255))

d = ImageDraw.Draw(img)
font = ImageFont.truetype("DejaVuSans-Bold.ttf", 40)  
d.text((50, 5), "2 + 2", fill=(0, 0, 0), font=font)
img.save("jatin.png")
