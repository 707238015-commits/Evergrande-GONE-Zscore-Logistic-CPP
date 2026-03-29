# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm

# 1. 读取数据（改成你的路径）
df = pd.read_excel(r"E:\Pyshon\data_check.xlsx")

# 2. 选择变量
X = df[['x1','x2','x3','x4','x5']]

# 3. 处理缺失值（重要）
X = X.dropna()

# 4. 相关系数矩阵
corr_matrix = X.corr()
print("相关系数矩阵：")
print(corr_matrix)

# 5. 加常数项（更规范）
X_const = sm.add_constant(X)

# 6. 计算 VIF
vif_data = pd.DataFrame()
vif_data["variable"] = X_const.columns
vif_data["VIF"] = [
    variance_inflation_factor(X_const.values, i)
    for i in range(X_const.shape[1])
]

print("\nVIF结果：")
print(vif_data)
input("按回车退出...")