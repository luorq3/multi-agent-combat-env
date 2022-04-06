from PIL import Image
import numpy as np
import os


BASE = "../fight_env_gym/assets/images/"
fs = os.listdir(BASE)

for n in fs:
    img = Image.open(BASE + n)

    arr = np.array(img)
    shape = arr.shape

    w_s = 0
    while True:
        if np.all(arr[w_s, :, :] == 0):
            w_s += 1
        else:
            break
    print(w_s)

    w_e = shape[0] - 1
    while True:
        if np.all(arr[w_e, :, :] == 0):
            w_e -= 1
        else:
            break
    print(w_e)

    h_s = 0
    while True:
        if np.all(arr[:, h_s, :] == 0):
            h_s += 1
        else:
            break
    print(h_s)

    h_e = shape[1] - 1
    while True:
        if np.all(arr[:, h_e, :] == 0):
            h_e -= 1
        else:
            break
    print(h_e)

    arr = arr[w_s: w_e+1, h_s:h_e+1, :]
    new_img = Image.fromarray(arr).convert()
    new_img.save(BASE + n)






