from jinja2 import Template
import os

# 定义HTML模板
template_str = """
<!DOCTYPE html>
<html>
<head>
<meta name="pypi:repository-version" content="1.1">
</head>
<body>
{% for whl_file in whl_files %}
<a href="{{ base_url }}{{ whl_file }}">{{ whl_file }}</a><br>
{% endfor %}
</body>
</html>
"""

# 创建Jinja2模板对象
template = Template(template_str)

# 目录路径，这里假设是当前目录下的whl文件夹
directory_path = 'assets/whl'

# 获取目录下所有的.whl文件
whl_files = [f for f in os.listdir(directory_path) if f.endswith('.whl')]

# 基础URL，这里假设是你的GitHub Pages的URL
base_url = 'https://raw.githubusercontent.com/myhloli/wheels/main/assets/whl'

# 渲染HTML模板
html_content = template.render(whl_files=whl_files, base_url=base_url)

# 写入HTML文件
with open('index.html', 'w') as file:
    file.write(html_content)
