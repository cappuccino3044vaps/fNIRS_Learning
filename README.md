# fNIRS_Learning
OSのデータセットを使ってfNIRSデータの扱いを学ぼうという試みで作りました。<br>
まずは手足のタッピング課題中の計測データを使用します。
>データセット
><https://figshare.com/articles/dataset/Open_access_fNIRS_dataset_for_classification_of_the_unilateral_finger-_and_foot-tapping/9783755?file=18069143>

# Dataset Infomation
1. mrk (marker information)
このセクションは、タスク実行中のイベント（マーカー）に関する情報を格納していると推察されます。

event: 実験中の特定のイベントを識別する番号やID。
time: イベントが発生した時間（おそらく秒単位）。
y: イベントラベル（例: 左手タップ、右手タップ、休憩などのクラス分類情報）。
className: yに対応するイベントラベル名（例: ["LeftTap", "RightTap"] など）。
用途:
タスクの開始・終了や条件の切り替えを示すマーカーとして、後でfNIRS信号解析を条件ごとに分割するために使用されます。

2. mnt (montage information)
このセクションは、fNIRSセンサーの配置（モンタージュ）に関する情報を格納していると推察されます。

x, y: 各センサーまたはチャネルの2次元座標。ヘッドキャップ上の配置を示します。
pos_3d: センサーまたはプローブの3次元空間上の位置（[x, y, z] 座標）。
clab: 各チャネルのラベル（例: ["Fp1", "Fp2", "O1", "O2"] など）。
box, box_sz: センサーやチャネルの位置を図示する際に使用するボックス情報。サイズや位置を定義。
scale_box, scale_box_sz: 配置図全体のスケール（倍率や調整用の値）。
用途:
センサーの物理的配置を定義し、信号がどの部位（頭皮のどの位置）から得られたかを示すために使われます。

3. nfo (general information)
このセクションは、fNIRS信号の取得に関する実験全体のメタデータを格納していると推察されます。

fs: サンプリング周波数（Hz）。信号が1秒間にどのくらいの頻度で記録されたかを示します。
clab: 使用されたチャネル（センサー）リスト。
T: 実験全体の測定時間（秒単位）。
nEpochs: 分析対象のエポック（データの区間）数。
length: 各エポックの長さ（秒またはデータポイント数）。
format: データフォーマット（例: "float32" や "int16" など）。
resolution: 信号の分解能（例: 物理単位あたりの値のスケール）。
file: 元のfNIRSデータが保存されているファイル名やパス。
nEvents: 記録された全イベント数。
nClasses: タスクに関連するクラス数（例: 左手、右手、休憩なら3）。
className: タスク条件を表すクラス名リスト（例: ["LeftTap", "RightTap", "Rest"] など）。
4. ch40 (fNIRS channel data)
このセクションには、個々のチャネル（ここでは40番目のチャネル）で記録されたfNIRS信号が格納されています。

Type: データ型（numpy.ndarray）、信号は数値配列として格納されていることを示します。
Content:
信号の値は連続した数値データ（例: [[0.000e+00], [-1.320e-04], [1.630e-03], ...]）。
これらはfNIRSセンサーによって記録された光の吸収や強度の変化を示します。
通常、酸化ヘモグロビン（HbO）、還元ヘモグロビン（HbR）、またはその和（HbT）として記録されます。
用途:
この信号データは、脳活動に関連する血流変化を解析するための主要なデータです。異なるチャネル（ch1 ~ ch40）は異なる頭皮上の位置からの測定を表しています。

5. dat (data information)
このセクションは、記録されたfNIRS信号全体に関するメタデータを提供しています。

fs: サンプリング周波数（Hz）。信号が1秒間に記録されたデータポイント数。
nSources: 光源（LEDやレーザー）数。
nDetectors: 光検出器数（フォトダイオードなど）。
multiplexing: 多重化の設定。異なる光源や波長を時間的または空間的に分離する方法（例: タイムスライス、多波長記録など）。
clab: チャネルのラベルリスト（例: ["ch1", "ch2", ..., "ch40"]）。
signal: 測定された信号データ（通常は各チャネルごとの配列全体を参照）。
yUnit: 信号の単位（例: "mM・mm"（濃度×距離）や "a.u."（任意単位））。
title: 測定に関する説明やタイトル（例: "Hand Tapping Task fNIRS Data"）。
xUnit: 横軸（時間）の単位（通常は「秒」）。
snr: 信号対雑音比（Signal-to-Noise Ratio）。データ品質を評価するための指標。
file: 元データのファイル名またはパス。

