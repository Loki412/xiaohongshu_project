# Xiaohongshu Campus Blogger Trust-Building Language Strategy Analysis

This project is based on the deep quantitative crawling and systematic content coding of **863 valid samples** from Xiaohongshu. It aims to uncover the core language strategies employed by campus bloggers to establish reader trust and validates the actual driving effects of different strategy combinations on engagement through multi-dimensional cross-analysis.

## 📈 Project Background & Core Findings

In the current era of "solution consumption," campus content on Xiaohongshu has shifted from pure "emotional consumption" to "practical knowledge acquisition." The core research question of this project is: **What language strategies do Xiaohongshu campus bloggers use to build reader trust?**

Based on the analysis of 863 valid samples, we derived the following key research conclusions:

1. **Identity Display Strategy**: General identities (e.g., "student / college student") dominate (56.4%), but **specific identities** (mentioning specific universities or majors) perform better in high-engagement content, establishing stronger authority.

2. **Evidence Proof Strategy**: Level 4 ($L4$) evidence (pure opinions / emotional expressions) is the most widely used (44.1%), but Level 2 ($L2$) process evidence (cases / stories) exhibits the strongest driving force for overall interaction volume.

3. **Relationship Building Strategy**: **Sharing-oriented pronouns** (focusing on "I") are the most popular (40.1%), demonstrating that a sincere, experience-sharing tone is more approachable and conversion-friendly than condescending instructions.

4. **Golden Strategy Combination**: The empirically validated optimal strategy combination is: **Specific Identity +** $L4$ **Evidence + Sharing-oriented Pronouns** (or adopting "Specific Identity + $L1$ Quantitative Data + Directive-oriented" for long-term value).

## 📂 Project Structure & File Description

This repository contains data sources, analysis scripts, visualization charts, and presentation deliverables:

```text
├── xiaohongshu_trust_analysis(1).pptx  # Core research presentation/PPT (includes all charts and cross-analysis matrices)
├── xiaohongshu_sample.json             # Sample data in JSON format (contains engagement metrics, topics, and category annotations)
├── xiaohongshu_sample.csv              # Sample data in CSV format (convenient for import into Excel or Python for secondary mining)
├── xhs_simple.py                       # Automated data crawling and sample generation script based on Selenium & Edge
├── test_edge.py                        # Edge WebDriver automated environment connectivity test script
├── step_by_step.py                     # Step-by-step guidance script for automated crawler and environment setup
└── README.md                           # Project overview documentation (this file)
```

## 🛠️ Data Crawler Tool Usage (`xhs_simple.py`)

This project uses Python combined with Selenium automation to retrieve public data. If you need to run or reproduce the data collection pipeline, follow these steps:

### 1. Environment Setup

It is recommended to configure a dedicated virtual environment in Anaconda:

```bash
conda create -n xhs python=3.9 -y
conda activate xhs
pip install selenium webdriver-manager beautifulsoup4 pandas
```

### 2. Running the Script

Navigate to the project directory and run the core script:

```bash
python xhs_simple.py
```

The script supports the following four interactive modes:

* **Mode 1**: Retrieve public page information and screenshots from Xiaohongshu.
* **Mode 2**: Search for related notes by keyword (e.g., "study check-in").
* **Mode 3**: Manual login mode (saves Cookies for subsequent deep collection tasks).
* **Mode 4**: One-click generation of simulated sample data matching the project schema (includes likes, comments, dates, and topics, saved to `xiaohongshu_sample.csv`).

## 📊 Eight Core Strategy Matrices

According to the cross-analysis results in the presentation, the research categorizes strategies into 8 distinct application scenarios:

| Strategy ID | Strategy Name | Core Objective | Recommended Scenario | Key Combination Features |
| :--- | :--- | :--- | :--- | :--- |
| **Strategy A** | Professional Strategy | Build professional authority | Knowledge / Dry-goods (Specific Majors) | Specific Identity + $L1$ Quant. Evidence + Directive |
| **Strategy B** | Propagation Strategy | Expand content distribution | Knowledge / Dry-goods (General Needs) | No Identity + $L4$ Pure Opinion + Mixed |
| **Strategy C** | Trust Strategy | Enhance deep trust | Knowledge / Dry-goods (Authoritative) | General Identity + $L3$ Citation + Sharing |
| **Strategy D** | Identity Strategy | Boost emotional identification | Personal Experience (Vertical Fields) | No Identity + $L4$ Pure Opinion + Sharing |
| **Strategy E** | Interactive Strategy | Promote comment engagement | Personal Experience (Process Sharing) | General Identity + $L2$ Process Evidence + Mixed |
| **Strategy F** | Collection Strategy | Improve resource conversion | Knowledge / Dry-goods (Resource Compilations) | Specific Identity + $L1$ Quant. Evidence + Directive |
| **Strategy G** | Resonance Strategy | Spark emotional resonance | Emotional Resonance (Peers) | No Identity + $L4$ Pure Opinion + Sharing |
| **Strategy H** | Memory Strategy | Strengthen content recall | Emotional Resonance (Cross-generation) | General Identity + $L2$ Process Evidence + Sharing |

If you have any questions regarding our research data models, operationalized coding rules, or script reproduction, feel free to reach out!

# 小红书校园博主信任构建语言策略分析

本项目基于对小红书平台上 **863个有效样本** 的深度数据爬取与系统化内容编码，旨在揭示校园博主为建立读者信任所采用的核心语言策略，并通过多维度交叉分析验证不同策略组合对互动效果的实际驱动作用。

## 📈 项目背景与核心发现

在当前“解决方案消费”的时代背景下，小红书上的校园内容已从纯粹的“情绪消费”转向“实用知识获取”。本项目的核心研究问题是：**小红书校园博主使用了哪些语言策略来建立读者信任？**

基于 863 个完整样本的分析，得出以下核心研究结论：

1. **身份展示策略**：泛称身份（如“学生/大学生”）占主导地位（56.4%），但**具体身份**（提及具体高校或专业）在高互动内容中表现更优，能建立更强的权威感。

2. **经验证明策略**：$L4$ 级证据（纯观点/情感表达）使用最广泛（44.1%），但 $L2$ 级过程证据（案例/故事）对整体互动量的驱动力最强。

3. **关系建立策略**：**分享型人称**（以“我”为主）最受欢迎（40.1%），证明真诚、经验分享的口吻比居高临下的指导说教更具亲和力和转化率。

4. **黄金策略组合**：经数据验证的最优策略组合为：**具体身份 + $L4$ 级证据 + 分享型人称**（或在追求长效价值时采用“具体身份 + $L1$ 量化数据 + 指导型”）。

## 📂 项目结构与文件说明

本仓库包含研究展示 PPT、示例数据、自动化爬虫与分析脚本：

```
├── xiaohongshu_trust_analysis(1).pptx  # 核心研究汇报 PPT（包含所有图表与交叉分析矩阵）
├── xiaohongshu_sample.json             # 示例数据（JSON 格式，含互动量、话题与分类标注）
├── xiaohongshu_sample.csv              # 示例数据（CSV 格式，方便导入 Excel 或 Python 二次挖掘）
├── xhs_simple.py                       # 基于 Selenium 与 Edge 的自动化数据爬取与样本生成脚本
├── test_edge.py                        # Edge WebDriver 自动化环境连通性测试脚本
├── step_by_step.py                     # 自动化爬虫与环境配置的逐步指导脚本
└── README.md                           # 项目说明文档（本文件）
```

## 🛠️ 数据爬虫工具使用说明 (`xhs_simple.py`)

本项目采用 Python 结合 Selenium 自动化获取公开数据。如果需要运行或复现数据采集流程，请按以下步骤操作：

### 1. 环境配置

建议在 Anaconda 中配置独立的虚拟环境：

```bash
conda create -n xhs python=3.9 -y
conda activate xhs
pip install selenium webdriver-manager beautifulsoup4 pandas
```

### 2. 运行脚本

进入项目目录并运行核心脚本：

```bash
python xhs_simple.py
```

脚本支持以下四种交互模式：
* **模式 1**：获取小红书公开页面信息与截图
* **模式 2**：按关键词搜索相关笔记（如“学习打卡”）
* **模式 3**：手动登录模式（保存 Cookies 以备后续深度采集）
* **模式 4**：一键生成符合项目 Schema 的模拟样本数据（包含点赞、评论、日期、话题，保存至 `xiaohongshu_sample.csv`）

## 📊 八大核心策略矩阵

根据演示文稿中的交叉分析结果，研究将策略梳理为 8 种应用场景：

| 策略编号 | 策略名称 | 核心定位 | 推荐应用场景 | 关键组合特征 |
| :--- | :--- | :--- | :--- | :--- |
| **策略 A** | 专业型策略 | 建立专业权威 | 知识干货类（专业领域） | 具体身份 + $L1$ 量化证据 + 指导型人称 |
| **策略 B** | 传播型策略 | 扩大内容传播 | 知识干货类（通用需求） | 无身份 + $L4$ 纯观点 + 混合型人称 |
| **策略 C** | 信任型策略 | 增强用户信任 | 知识干货类（权威解读） | 泛称身份 + $L3$ 引用证据 + 分享型人称 |
| **策略 D** | 认同型策略 | 提升情感认同 | 个人经验类（垂直领域） | 无身份 + $L4$ 纯观点 + 分享型人称 |
| **策略 E** | 互动型策略 | 促进评论互动 | 个人经验类（过程分享） | 泛称身份 + $L2$ 过程证据 + 混合型人称 |
| **策略 F** | 收藏型策略 | 提高收藏转化 | 知识干货类（资料整理） | 具体身份 + $L1$ 量化证据 + 指导型人称 |
| **策略 G** | 共鸣型策略 | 引发情感共鸣 | 情感共鸣类（同龄人） | 无身份 + $L4$ 纯观点 + 分享型人称 |
| **策略 H** | 记忆型策略 | 强化内容记忆 | 情感共鸣类（跨年龄层） | 泛称身份 + $L2$ 过程证据 + 分享型人称 |

---
*如果您对我们的研究数据模型、操作化编码规则或脚本复现有任何疑问，欢迎随时交流！*
