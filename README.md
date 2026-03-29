# 恒大集团 GONE 理论财务风险研究 - Z-score 修正 Logistic 回归代码

**论文标题**：基于 GONE 理论的恒大集团财务风险动因研究  
**作者**：杨志明  
**用途**：本仓库包含论文第七章“基于房地产样本的 Z-score 修正探索”中所使用的全部自研 C++ 代码、数据文件及复现脚本。

## 仓库内容
- `src/`：C++17 源代码（使用 Eigen 线性代数库）
- `data/`：50 家房地产上市公司样本（危机组 25 + 稳健组 25）
- `results/`：论文中表 3~表 9 的原始输出文件
- `README.md`：本说明文件

## 如何复现论文结果（一键运行）
1. 安装 C++11 编译器（推荐 Visual Studio 2022 或 g++）
2. 安装 Eigen 库（头文件方式即可）
3. 编译运行：
   ```bash
   g++ -std=c++17 -O2 -I/path/to/eigen src/main.cpp -o zscore_correction
   ./zscore_correction
