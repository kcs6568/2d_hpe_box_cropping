import json
import pickle
import mmcv
import os.path as osp


# mpii_test_path = '/root/data/mpii/annotations/mpii_test.json'
# mpii_train_path = '/root/data/mpii/annotations/mpii_train.json'
# mpii_trainval_path = '/root/data/mpii/annotations/mpii_trainval.json'
# mpii_val_path = '/root/data/mpii/annotations/mpii_val.json'
# image_root = '/root/data/mpii/images'
# annotation_root = '/root/data/mpii/annotations'

# annotation_test = mmcv.load(mpii_test_path, file_format='json')
# # annotation_train = mmcv.load(mpii_train_path, file_format='json')
# # annotation_trainval = mmcv.load(mpii_trainval_path, file_format='json')
# # annotation_val = mmcv.load(mpii_val_path, file_format='json')


# # print("test len:", len(annotation_test))
# # print("train len:", len(annotation_train))
# # print("trainval len:", len(annotation_trainval))
# # print("val len:", len(annotation_val))

# # img_name = annotation_test[0]['image']
# # img_path = osp.join(image_root, img_name)
# # print(img_path)

# img_name = annotation_test[0]['image']
# img_path_list = [osp.join(image_root, img['image']) for img in annotation_test]
# mpii_test_pickle = osp.join(annotation_root, 'mpii_test_pickle.pkl')

# mmcv.dump(img_path_list, file=mpii_test_pickle, file_format='pickle')
# data = mmcv.load(mpii_test_pickle, file_format='pickle')

# print(type(data))


# def write_file(data, path, file_format):

from collections import defaultdict

dicts = defaultdict(dict)

data = {'a':1, 'b':2, 'c':3}

for i in range(10):
    dicts[i] = data


path = '/root/volume'
file = osp.join(path, 'tmp.json')

for i, j in dicts.items():
    
    mmcv.dump(i, file, file_format='json')

# mmcv.dump(dicts, file, file_format='json')




