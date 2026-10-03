# -*- coding: utf-8 -*-
"""
小红书爬虫 - 最简Edge版本
在Anaconda Prompt中运行
"""

import time
import json
import csv
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import os

def setup_edge_driver():
    """自动设置Edge驱动"""
    print("1. 正在自动配置Edge WebDriver...")
    
    # 自动下载和管理Edge驱动
    driver_path = EdgeChromiumDriverManager().install()
    
    # 配置Edge选项
    edge_options = Options()
    
    # 防止被检测为自动化工具
    edge_options.add_argument('--disable-blink-features=AutomationControlled')
    edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    edge_options.add_experimental_option('useAutomationExtension', False)
    
    # 设置用户代理
    edge_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0')
    
    # 其他设置
    edge_options.add_argument('--start-maximized')  # 最大化窗口
    edge_options.add_argument('--disable-notifications')  # 禁用通知
    
    # 创建服务
    service = Service(driver_path)
    
    # 创建浏览器实例
    driver = webdriver.Edge(service=service, options=edge_options)
    
    print("✓ Edge浏览器配置成功!")
    return driver

def get_public_data(driver):
    """获取小红书公开数据"""
    print("\n2. 访问小红书...")
    
    # 访问小红书
    driver.get("https://www.xiaohongshu.com")
    time.sleep(5)
    
    print(f"当前页面: {driver.title}")
    print(f"当前URL: {driver.current_url}")
    
    # 获取页面标题
    page_title = driver.title
    print(f"页面标题: {page_title}")
    
    # 截屏保存
    driver.save_screenshot('xiaohongshu_homepage.png')
    print("✓ 页面截图已保存: xiaohongshu_homepage.png")
    
    # 获取页面源码（可以用于分析）
    page_source = driver.page_source
    with open('xiaohongshu_page.html', 'w', encoding='utf-8') as f:
        f.write(page_source)
    print("✓ 页面源码已保存: xiaohongshu_page.html")
    
    return {
        'title': page_title,
        'url': driver.current_url,
        'source_length': len(page_source)
    }

def search_keyword(driver, keyword):
    """搜索关键词"""
    print(f"\n3. 搜索关键词: {keyword}")
    
    # 构建搜索URL
    search_url = f"https://www.xiaohongshu.com/search_result?keyword={keyword}"
    
    driver.get(search_url)
    time.sleep(5)
    
    # 截屏
    driver.save_screenshot(f'search_{keyword}.png')
    print(f"✓ 搜索结果截图: search_{keyword}.png")
    
    # 获取页面中的一些信息
    try:
        # 查找可能的笔记元素
        page_text = driver.page_source
        
        # 简单统计
        note_count = page_text.count('note-item') + page_text.count('笔记')
        
        print(f"页面包含 '笔记' 相关元素: {note_count} 处")
        
        # 尝试获取一些文本内容
        elements = driver.find_elements(By.TAG_NAME, 'div')
        text_contents = []
        
        for i, elem in enumerate(elements[:20]):  # 只取前20个
            text = elem.text.strip()
            if text and len(text) > 10:
                text_contents.append(text)
        
        print(f"找到 {len(text_contents)} 条文本内容")
        
        # 保存找到的文本
        with open(f'search_results_{keyword}.txt', 'w', encoding='utf-8') as f:
            for text in text_contents[:10]:  # 保存前10条
                f.write(f"{text}\n{'='*50}\n")
        
        return {
            'keyword': keyword,
            'note_elements': note_count,
            'text_found': len(text_contents),
            'screenshot': f'search_{keyword}.png'
        }
        
    except Exception as e:
        print(f"搜索时出错: {e}")
        return {'error': str(e)}

def manual_login_mode(driver):
    """手动登录模式"""
    print("\n=== 手动登录模式 ===")
    print("1. 浏览器窗口已打开")
    print("2. 请手动登录小红书账号")
    print("3. 登录完成后，按Enter键继续...")
    
    driver.get("https://www.xiaohongshu.com")
    time.sleep(3)
    
    input("登录完成后，按Enter键继续...")
    
    # 获取cookies
    cookies = driver.get_cookies()
    
    # 保存cookies
    with open('xiaohongshu_cookies.json', 'w', encoding='utf-8') as f:
        json.dump(cookies, f, ensure_ascii=False, indent=2)
    
    print(f"✓ 已保存 {len(cookies)} 个cookies")
    
    # 显示当前页面信息
    print(f"当前页面: {driver.title}")
    
    return cookies

def generate_sample_data():
    """生成示例数据（如果爬取失败）"""
    print("\n生成示例数据...")
    
    import pandas as pd
    import random
    
    data = []
    topics = ["学习打卡", "考研", "自律", "早起", "读书"]
    
    for i in range(50):
        topic = random.choice(topics)
        data.append({
            'id': f'note_{10000+i}',
            'title': f'{topic}日记第{i+1}天',
            'content': f'今天坚持{topic}了{random.randint(1, 8)}小时，收获满满！',
            'user': f'用户_{random.randint(1, 100)}',
            'likes': random.randint(50, 1000),
            'comments': random.randint(5, 100),
            'date': f'2024-{random.randint(1,12):02d}-{random.randint(1,28):02d}',
            'topic': topic,
            'source': 'generated'
        })
    
    # 保存为CSV和JSON
    df = pd.DataFrame(data)
    df.to_csv('xiaohongshu_sample.csv', index=False, encoding='utf-8-sig')
    df.to_json('xiaohongshu_sample.json', orient='records', force_ascii=False)
    
    print(f"✓ 已生成 {len(data)} 条示例数据")
    print("  文件: xiaohongshu_sample.csv, xiaohongshu_sample.json")
    
    return data

def main():
    """主函数"""
    print("=" * 60)
    print("小红书数据获取工具")
    print("=" * 60)
    
    driver = None
    try:
        # 1. 设置Edge驱动
        driver = setup_edge_driver()
        
        # 2. 选择模式
        print("\n请选择模式:")
        print("1. 获取公开页面信息")
        print("2. 搜索关键词")
        print("3. 手动登录")
        print("4. 生成示例数据")
        
        choice = input("\n请输入选择 (1-4): ").strip()
        
        results = []
        
        if choice == '1':
            # 获取公开数据
            data = get_public_data(driver)
            results.append(data)
            
        elif choice == '2':
            # 搜索关键词
            keyword = input("请输入搜索关键词: ").strip() or "学习打卡"
            data = search_keyword(driver, keyword)
            results.append(data)
            
        elif choice == '3':
            # 手动登录
            cookies = manual_login_mode(driver)
            print(f"\n登录成功! 已获取 {len(cookies)} 个cookies")
            
        elif choice == '4':
            # 生成示例数据
            data = generate_sample_data()
            results.extend(data)
            
        else:
            print("无效选择，将获取公开页面信息")
            data = get_public_data(driver)
            results.append(data)
        
        # 显示结果摘要
        print("\n" + "=" * 60)
        print("执行完成!")
        print("=" * 60)
        
        if results:
            print(f"获取到 {len(results)} 条结果")
        
        print("\n生成的文件:")
        for file in os.listdir('.'):
            if file.startswith('xiaohongshu') or file.startswith('search'):
                print(f"  - {file}")
        
        print("\n下一步:")
        print("1. 查看生成的 .png 截图文件")
        print("2. 查看 .html 或 .txt 文本文件")
        print("3. 如果有数据文件 (.csv/.json)，可以用于分析")
        
    except Exception as e:
        print(f"\n❌ 执行出错: {e}")
        print("\n常见问题解决:")
        print("1. 确保Edge浏览器已安装")
        print("2. 确保网络连接正常")
        print("3. 尝试以管理员身份运行Anaconda Prompt")
        
        # 生成示例数据作为备用
        generate_sample_data()
        
    finally:
        # 关闭浏览器
        if driver:
            input("\n按Enter键关闭浏览器...")
            driver.quit()
            print("浏览器已关闭")

if __name__ == "__main__":
    main()