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

## 👥 Team Members & Roles

* **Project Coordination / Data Crawling**: Yuzhen Lin
* **Data Cleaning / Category Annotation**: You Chen, Bingbing Zhu
* **Visualization Chart Design**: Yuzhen Lin, Jingwen Qiu
* **Chart Interpretation / PPT & Documentation**: Jingwen Qiu

*If you have any questions regarding our research data models, operationalized coding rules, or script reproduction, feel free to reach out!*