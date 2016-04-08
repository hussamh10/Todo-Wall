from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# colors = {"Red" : }

def main():
	wallpaper = Image.new("RGB", (1024, 768), (255, 0, 0))
	f = ImageFont.load_default()

	ok = ImageDraw.Draw(wallpaper)

	ok.text( (0, 0), "Someplace Near Boulder",  font=f, fill=255)
	ok.rectangle(((0, 0), (10, 100)), fill="black", outline='blue')

	wallpaper.show()
	wallpaper.save('out.bmp')

main()
