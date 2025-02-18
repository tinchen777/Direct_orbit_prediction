import pandas as pd
import os
from collections import Counter


directory = 'dataset/RAW_Converted_ANALYS/1/2024/07'

# 获取目录中的所有子目录
subdirectories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

for dir in subdirectories:
    path = directory + '/' + dir
    file_names = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for file_name in file_names:
        file_path = path + '/' + file_name
        df = pd.read_csv(file_path)
        df3 = df['date_time'].tolist()

        # 将字符串时间列转换为 datetime 类型
        df['date_time'] = pd.to_datetime(df['date_time'])

        # 计算相邻时间差
        time_diff = df['date_time'].diff().dt.total_seconds().tolist()

        #print(time_diff)
        counter = Counter(time_diff)

        most_common = counter.most_common(1)
        #print(most_common)
        print('2024.07.{}, 时间间隔众数是:{}'.format(dir, most_common[0][0]))


#######拼接
directory = 'dataset/RAW_Converted_ANALYS/1/2024/07'
# 获取目录中的所有子目录
subdirectories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))][:4]

dfs = []

for dir in subdirectories:
    path = directory + '/' + dir
    file_names = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for file_name in file_names:
        file_path = path + '/' + file_name
        df = pd.read_csv(file_path)
        df3 = df['date_time'].tolist()
        dfs.append(df)

# 将所有 DataFrame 拼接成一个大的 DataFrame
combined_df = pd.concat(dfs, ignore_index=True)
combined_df2 = combined_df.drop(columns=['satellite_id', 'PDOP', 'other'], inplace=False)

# 将合并后的 DataFrame 保存到新的 CSV 文件
combined_df2.to_csv('dataset/star/combined.csv', index=False)
