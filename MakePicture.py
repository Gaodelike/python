import pandas as pd
import matplotlib.pyplot as plt

fig, axes = plt.subplots(figsize=(15,10))
df = pd.read_table("sample.xlsx",index_col=0)
length = len(df.columns)   #统计需要画的样本有几个
plt.bar(np.array([x*4 for x in range(length)]),np.array(df.ix[0,:]),np.array([3]*length),label=df.index[0])  #label就是最后的legend
ax = plt.gca()  #获取axes的实例对象
ax.set_xticks(np.array([x*4 for x in range(length)]))    #先把每个柱状图的x轴标签设置好对应的物理坐标，然后才能用set_xticklabels进行替换
ax.set_xticklabels(list(df.columns))
