# step_by_step.py - 逐步指导
import time

print("=" * 60)
print("小红书爬虫 - 逐步指导")
print("=" * 60)

steps = [
    "1. 创建虚拟环境: conda create -n xhs python=3.9 -y",
    "2. 激活环境: conda activate xhs",
    "3. 安装库: pip install selenium webdriver-manager beautifulsoup4",
    "4. 进入项目目录: cd xiaohongshu_project",
    "5. 运行脚本: python xhs_simple.py",
    "6. 选择模式1（获取公开信息）测试",
    "7. 查看生成的文件",
    "8. 如果成功，尝试其他模式"
]

print("\n请按以下步骤操作:\n")
for i, step in enumerate(steps, 1):
    print(f"步骤{i}: {step}")
    time.sleep(0.5)

print("\n" + "=" * 60)
print("按以下命令顺序执行:\n")

commands = [
    "conda create -n xhs python=3.9 -y",
    "conda activate xhs",
    "pip install selenium webdriver-manager beautifulsoup4 pandas",
    "mkdir xiaohongshu_project && cd xiaohongshu_project",
    "python xhs_simple.py"
]

for cmd in commands:
    print(f"  {cmd}")
    
print("\n提示: 复制命令到Anaconda Prompt中执行")