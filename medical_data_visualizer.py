import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['height'] = df ['height'] / 100      # convert to meters
df['overweight'] = np.where(((df['weight']) / (df['height'] ** 2)) > 25, 1, 0)

# 3
df['cholesterol'] = np.where((df['cholesterol']) == 1, 0, 1)
df['gluc'] = np.where((df['gluc']) == 1, 0, 1)

# 4
def draw_cat_plot():
    # 5
    melt = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=melt, var_name='variable', value_name='value')

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    figure = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    )

    # 8
    fig = figure.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = corr = df_heat.corr().round(1)

    # 13
    mask = mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(12,10))

    # 15
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax
    )


    # 16
    fig.savefig('heatmap.png')
    return fig
