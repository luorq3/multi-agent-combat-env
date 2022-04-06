from PIL import Image
import numpy as np

BASE = "../fight_env_gym/assets/images/"

def compress(path, size, s_path):
    img = Image.open(BASE + path)
    # img.show()
    w, h = img.size
    print(f"original size: {(w, h)}")
    img_ = img.resize(size)
    img_.save(BASE + s_path)

# def ttt(path):
path = 'ship.png'
img = Image.open(BASE + path)
arr = np.array(img)
print(arr.shape)





