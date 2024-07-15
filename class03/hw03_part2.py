
# Question 11
# ======================================================================
from PIL import Image

img = Image.open("il_mountains.jpg")
pixels = img.load()
# img.show()


print(img.size)
print(f"{img.width},{img.height}")

for x in range(img.width):
  for y in range(img.height):
    print(pixels[x, y])
    # print(f"{x},{y}")

# ======================================================================