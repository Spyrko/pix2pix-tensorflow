import glob
import os


PATH="/home/ma/masterthesis/datasets/YCB_Video_Dataset/"

TEST=["0048","0049","0050","0051","0052","0053","0054","0055","0056","0057","0058","0059"]

TOPLEVEL_FOLDER = ["test", "train", "train_seg"]

folders=glob.glob(PATH+"data/*")
train_folder_count = int((len(folders) - len(TEST))/2)
non = 0
for idx, folder in enumerate(folders):
    folder_name, _ = os.path.splitext(os.path.basename(folder))
    if folder_name in TEST:
        tf = TOPLEVEL_FOLDER[0]
        non += 1
    elif idx - non < train_folder_count:
        tf = TOPLEVEL_FOLDER[1]
    else:
        tf = TOPLEVEL_FOLDER[2]
    files=glob.glob(folder+"/*")
    print("%s: %s (%s of %s)" % (folder, tf, idx+1, len(folders)))
    for file in files:
        name, apx = os.path.splitext(os.path.basename(file))
        name, sf = name.split("-")
        path = PATH+tf+"/"+sf+"/"
        file_name = folder_name+"-"+name+apx
        os.makedirs(path, exist_ok=True)
        os.system("ln -s " + file + " " + path + file_name)