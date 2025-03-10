import numpy as np


def RSE(pred, true):
    return np.sqrt(np.sum((true - pred) ** 2)) / np.sqrt(np.sum((true - true.mean()) ** 2))


def CORR(pred, true):
    u = ((true - true.mean(0)) * (pred - pred.mean(0))).sum(0)
    d = np.sqrt(((true - true.mean(0)) ** 2).sum(0) * ((pred - pred.mean(0)) ** 2).sum(0))
    return (u / d).mean(-1)


def MAE(pred, true):  # 平均绝对误差
    return np.mean(np.abs(pred - true))


def MSE(pred, true):   # 均方误差
    return np.mean((pred - true) ** 2)


def RMSE(pred, true):  # 均方根误差
    return np.sqrt(MSE(pred, true))


def MAPE(pred, true):   # 平均绝对百分比误差
    return np.mean(np.abs((pred - true) / true))


def MSPE(pred, true):  # 均方百分比误差
    return np.mean(np.square((pred - true) / true))


def metric(pred, true):
    mae = MAE(pred, true)   # 平均绝对误差
    mse = MSE(pred, true)    # 均方误差
    rmse = RMSE(pred, true)   # 均方根误差
    mape = MAPE(pred, true)   # 平均绝对百分比误差
    mspe = MSPE(pred, true)   # 均方百分比误差

    return mae, mse, rmse, mape, mspe
