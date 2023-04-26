import torch
import dgl
"""
假设我们所有wsi的存储方式为csv+提取好的patch embedding（.pth）
csv中记录了suoyoupatch的文件名和顺序信息(与.pth文件中的顺序对应)

"""