import scipy.io
import numpy as np
import glob
import os

PATH = "/home/ma/masterthesis/datasets/YCB_Video_Dataset/train/"
os.mkdir(PATH+"rotation")
paths = glob.glob(PATH + "meta/*")
for path in paths:
    name, _ = os.path.splitext(os.path.basename(path))
    mat = scipy.io.loadmat(path)
    res = [[v for v in np.concatenate((mat["cls_indexes"][i], mat["poses"][:,:3,i].flatten()))] for i in range(len(mat["cls_indexes"]))]
    str = ""
    for row in res:
        for v in row:
            str += "%s," % v
        str = str[:-1]
        str += "\n"
    with open(PATH + "rotation/" + name + ".csv", "w") as fh:
        fh.write(str)