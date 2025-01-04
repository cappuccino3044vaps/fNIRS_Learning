from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import os
import mne

def explore_mat_struct(data, depth=0, file=None):
    """MATファイル内のデータ構造を再帰的に探索"""
    indent = '  ' * depth
    if isinstance(data, dict):
        for key, value in data.items():
            if not key.startswith('__'):
                file.write(f"{indent}{key}: {type(value)}\n")
                explore_mat_struct(value, depth + 1, file)
    elif isinstance(data, np.ndarray) and data.dtype.names:
        for name in data.dtype.names:
            file.write(f"{indent}{name}: {data[name].shape}\n")
    else:
        file.write(f"{indent}Type: {type(data)}, Content: {data}\n")

# MATファイルのパスを指定
filename = 'fNIRS 01.mat'
filepath = os.getcwd() + '/fNIRS_data/' + filename

# 出力ファイルを開く
output_file = 'keywords.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    data = loadmat(filepath)
    explore_mat_struct(data,file=file)



