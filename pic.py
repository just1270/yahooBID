from bs4 import BeautifulSoup

# 假设这是你的HTML内容，包含了一个具有特定类名的<span>元素
html_content = '<span class="sc-dlGagL sc-gKBqHi dkipYY cWhwYS">$117</span>'

# 使用 BeautifulSoup 解析 HTML 内容
soup = BeautifulSoup(html_content, "html.parser")

# 找到 class 为 "sc-dlGagL sc-gKBqHi dkipYY cWhwYS" 的 span 元素
target_span = soup.find("span", class_="sc-dlGagL sc-gKBqHi dkipYY cWhwYS")

# 提取 span 元素的文本内容并打印
if target_span:
    print(target_span.text)
else:
    print("未找到指定的<span>元素")
