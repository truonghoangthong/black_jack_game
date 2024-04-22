import matplotlib.pyplot as plt
import pandas as pd
import os

class draw:
    def raw():
        color = ['green', 'red', 'yellow']
        edgecolor = ['darkred', 'darkblue', 'black']
        df = pd.read_csv('match_history.csv', usecols=['win', 'lose', 'tie'])
        column_sums = df.sum()
        plt.figure(figsize=(10, 6))
        plt.bar(column_sums.index, column_sums.values,color=color,
            edgecolor=edgecolor,linewidth=3)
        for index, value in enumerate(column_sums.values):
            plt.text(index,value, str(value), ha='center',va='bottom')
        plt.title("")
        plt.xlabel("Result")
        plt.ylabel("Match")
        plt.xticks(rotation=0)
        file_name = 'match.png'
        plt.savefig(file_name)
        return file_name

