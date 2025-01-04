import random
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.animation import FuncAnimation


# 日本語フォントの設定
font_path = 'C:/Windows/Fonts/msgothic.ttc'  # フォントファイルのパス
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

def generate_initial_population(surname_list, min_count=100, max_count=1000000):
    """
    初期人口を生成する。
    
    Args:
        surname_list (list): 苗字のリスト。
        min_count (int): 各苗字の最小人口。
        max_count (int): 各苗字の最大人口。
    
    Returns:
        list: 初期の総人口リスト。
    """
    population = []
    for surname in surname_list:
        count = random.randint(min_count, max_count)  # 各苗字の人口をランダムに決定
        population.extend([surname] * count)  # 苗字を指定された回数リストに追加
    return population

def simulate_generations(initial_population, num_generations):
    """
    世代ごとのシミュレーションを実行する。
    
    Args:
        initial_population (list): 初期の総人口リスト。
        num_generations (int): シミュレーションする世代数。
    
    Returns:
        list: 各世代の苗字の分布を記録したリスト。
    """
    current_population = initial_population[:]
    history = []

    for generation in range(num_generations):
        # 現在の総人口をシャッフルしてランダムにペアを作成
        random.shuffle(current_population)
        pairs = [current_population[i:i+2] for i in range(0, len(current_population), 2)]

        next_generation = []

        for pair in pairs:
            if len(pair) == 2:
                # 2つの苗字からランダムに1つを選択して次世代に加える
                tmp=random.choice(pair)
                next_generation.append(tmp)
                next_generation.append(tmp)
            else:
                # 奇数の場合、余った1つはそのまま次世代に加える
                next_generation.append(pair[0])

        # 次世代の苗字分布を記録
        history.append(Counter(next_generation))

        # 次世代を現在の人口として更新
        current_population = next_generation

        # 苗字が1種類になったら終了
        if len(set(current_population)) == 1:
            break

    return history

def animate_surname_evolution(history):
    fig, ax = plt.subplots(figsize=(8, 8))

    def update(frame):
        ax.clear()
        distribution = history[frame]
        labels = distribution.keys()
        sizes = distribution.values()
        
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        ax.set_title(f"世代 {frame + 1} の苗字分布")
        ax.axis('equal')  # 円を真円にする

    ani = FuncAnimation(fig, update, frames=len(history), repeat=False)
    plt.show()

# 初期設定
surnames = ["佐藤", "鈴木", "高橋", "田中", "渡辺", "伊藤", "山本", "中村", "小林", "加藤",
            "吉田", "山田", "佐々木", "山口", "松本", "井上", "木村", "林", "清水", "斉藤"]

# 初期の総人口を生成
initial_population = generate_initial_population(surnames, min_count=10, max_count=100)

# シミュレーション実行
num_generations = 100
history = simulate_generations(initial_population, num_generations)

# 結果の表示
print(f"初期人口: {Counter(initial_population)}")
for i, distribution in enumerate(history):
    print(f"世代 {i+1}: {dict(distribution)}")

# 最終的な苗字の割合を計算
final_population = sum(history[-1].values())
final_distribution = {k: v / final_population for k, v in history[-1].items()}
print("\n最終的な苗字の割合:")
for surname, ratio in final_distribution.items():
    print(f"{surname}: {ratio:.2%}")

# アニメーションを表示
animate_surname_evolution(history)

# グラフの表示
generations = list(range(1, num_generations + 1))
for surname in surnames:
    counts = [distribution.get(surname, 0) for distribution in history]
    plt.plot(generations, counts, label=surname)

plt.xlabel('世代')
plt.ylabel('人口')
plt.title('苗字の進化')
plt.legend()
plt.show()
