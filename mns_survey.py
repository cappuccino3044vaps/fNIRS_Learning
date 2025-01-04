from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import os
import mne

# MATファイルのパスを指定
filename = 'fNIRS 01.mat'
filepath = os.getcwd() + '/fNIRS_data/' + filename

# MATファイルの読み込み
data = loadmat(filepath)

# サンプリングレートの取得
fs = data['nfo']['fs'][0, 0]  # サンプリング周波数

# チャンネルデータの取得（MATファイルの構造に応じて修正）
channels_hbo = [data[f'ch{i}_hbo'].flatten() for i in range(1, 40)]
channels_hbr = [data[f'ch{i}_hbr'].flatten() for i in range(1, 40)]

# チャンネル名の取得
ch_names_hbo = [f'S{i}_D{i} hbo' for i in range(1, 40)]
ch_names_hbr = [f'S{i}_D{i} hbr' for i in range(1, 40)]
ch_names = ch_names_hbo + ch_names_hbr

# チャンネルタイプ
ch_types = ['hbo'] * len(channels_hbo) + ['hbr'] * len(channels_hbr)

# データをnumpy配列に変換（[n_channels, n_samples]の形）
data_array = np.array(channels_hbo + channels_hbr)

# MNE Rawオブジェクトを作成
info = mne.create_info(ch_names=ch_names, sfreq=fs, ch_types=ch_types)
raw = mne.io.RawArray(data_array, info)

# センサー位置の設定（ダミーデータを使用、必要に応じて修正）
positions = np.random.rand(len(ch_names), 3)  # ランダム座標の例
ch_pos = {ch_names[i]: positions[i] for i in range(len(ch_names))}
montage = mne.channels.make_dig_montage(ch_pos=ch_pos, coord_frame='head')
raw.set_montage(montage)

# プロット
raw.plot(duration=5, n_channels=5)
raw.plot_sensors(show_names=True, title='Sensor Layout')
plt.show()