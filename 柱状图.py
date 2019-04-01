import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def DrawHistogram(read_name):

    #读取数据
    read_name = r"C:\Users\Administrator\Desktop\ssq.csv"
    fp = pd.read_csv(read_name)
    first_prize = fp.first_prize
    second_prize = fp.second_prize

    #配置图形参数
    ind = np.arange(len(first_prize))
    width = 0.5
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width/2, first_prize, width, color='SkyBlue', label='First')
    rects2 = ax.bar(ind + width/2, second_prize, width,color='IndianRed', label='Second')

    ax.set_ylabel('Stakes')
    ax.set_title('Stakes by year and rank')
    plt.xticks(ind,(18,17,16,15,14,13,12,11,10,9,8,7,6,5))
    ax.legend()
    plt.show()

if __name__=='__main__':

   DrawHistogram(r"C:\Users\Administrator\Desktop\ssq.csv")
