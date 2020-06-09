# -*- coding: utf-8 -*-
import numpy as np
    
def softmax(x):
# バッチ処理の場合xは(バッチの数, 10)の2次元配列になる。
# この場合、ブロードキャストを使ってうまく画像ごとに計算する必要がある。
    if x.ndim == 2:
        # 画像ごと（axis=1）の最大値を算出し、ブロードキャストできるよにreshape
        c = np.max(x, axis=1).reshape(x.shape[0], 1)
        # オーバーフロー対策で最大値を引きつつ分子を計算
        exp_a = np.exp(x - c)
        # 分母も画像ごと（axis=1）に合計し、ブロードキャストできるよにreshape
        sum_exp_a = np.sum(exp_a, axis=1).reshape(x.shape[0], 1)
        # 画像ごとに算出
        y = exp_a / sum_exp_a

    else:
        # バッチ処理ではない場合は本の通りに実装
        c = np.max(x)
        exp_a = np.exp(x - c)  # オーバーフロー対策
        sum_exp_a = np.sum(exp_a)
        y = exp_a / sum_exp_a

    return y
