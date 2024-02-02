from PIL import ImageOps
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

# Reading the color image
image = Image.open('The-One-Piece-Movies-In-Order-1-1140x641.jpg')

# Writing Persian text on the image
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('BYEKAN.TTF', size=50)
text = "وان پیس"
reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
bidi_text = get_display(reshaped_text)           # correct its direction
draw.text((50, 50), bidi_text, fill="black",
          font=font, align='right', stroke_width=2, stroke_fill='white')

plt.imshow(image)
plt.savefig('text.png')
# Calculating and showing histograms for each color channel
plt.figure(figsize=(10, 7))
for i, color in enumerate(['r', 'g', 'b']):
    histogram = image.histogram()[i*256:(i+1)*256]
    plt.plot(histogram, color=color)
plt.title('Color Histograms')
plt.savefig('channels.png')

# Equalizing the image histogram (for each channel)
equalized_image = ImageOps.equalize(image)

# Convert image to gray
gray_image = ImageOps.grayscale(image)

# Calculate and show histogram for the gray image
plt.figure(figsize=(5, 3))
histogram = gray_image.histogram()
plt.plot(histogram, color='black')
plt.title('Gray Image Histogram')
plt.savefig('gray_hist.png')

# Equalize the gray image histogram
equalized_gray_image = ImageOps.equalize(gray_image)

# Show the equalized histograms
plt.figure(figsize=(5, 3))
histogram = equalized_gray_image.histogram()
plt.plot(histogram, color='gray')
plt.title('Equalized Gray Image Histogram')
plt.savefig('equal_hist.png')

plt.show()
