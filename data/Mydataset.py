'''
@project : LeNet-5
@author  : Hoodie_Willi
@description: ${}
@time   : 2019-06-26 18:24:39
'''
from torch.utils.data import Dataset
from PIL import Image


'''
    所有继承Dataset类的自定义dataset类，都要override  __len__和 __getitem__方法
'''


class MyDataset(Dataset):

    def __init__(self, txt_path, transform=None, target_transform=None):
        fh = open(txt_path, 'r')
        imgs = []
        for line in fh:
            line = line.rstrip()  # 删除 string 字符串末尾的指定字符（默认为空格）.
            words = line.split()
            imgs.append((words[0], int(words[1])))

        self.imgs = imgs        # 最主要就是要生成这个list， 然后DataLoader中给index，通过getitem读取图片数据
        self.transform = transform
        self.target_transform = target_transform

    '''
        提供了数据集的大小, 返回数据集的长度
    '''
    def __len__(self):
        return len(self.imgs)

    '''
        支持整数索引，范围从0到len(self)
    '''
    def __getitem__(self, index):
        fn, label = self.imgs[index]
        img = Image.open(fn).convert('L') # 像素值 0~255，在transfrom.totensor会除以255，使像素值变成 0~1

        if self.transform is not None:
            img = self.transform(img)  # 在这里做transform，转为tensor等等

        return img, label