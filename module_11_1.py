import matplotlib.pyplot as plt
import requests
from PIL import Image
import matplotlib

# requests
response = requests.get('https://www.youtube.com/')
print(response.status_code)
print(response.ok)


# pillow
def new_photo(name):
    im = Image.open(name)
    print(im.format, im.size, im.mode)
    w, h = im.size
    return im.resize((w//2, h//2))


image = new_photo('111.jpg')
image.show()


#matplotlib
x_list = list(range(0,5))
y_list = [22, 17, 81, 41, 25]

plt.plot(x_list, y_list)
plt.show()