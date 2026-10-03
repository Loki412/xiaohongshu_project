# test_edge.py - 测试Edge是否能正常工作
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# 测试Edge驱动
print("测试Edge WebDriver...")
driver_path = EdgeChromiumDriverManager().install()
print(f"驱动路径: {driver_path}")

service = Service(driver_path)
driver = webdriver.Edge(service=service)

print("打开百度测试...")
driver.get("https://www.baidu.com")
print(f"页面标题: {driver.title}")

driver.quit()
print("测试成功!")