from jinja2 import Template
import os

# 定义HTML模板
template_str = """
<!DOCTYPE html>
<html>
<head>
<meta name="pypi:repository-version" content="1.1">
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?15d27875695f5ffb9252818426884ce8";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
</head>
<body>
{% for package in packages %}
<a href="{{ base_url }}{{ package }}/">{{ package }}</a><br>
{% endfor %}
</body>
</html>
"""

# 定义子页面的HTML模板
subpage_template_str = """
<!DOCTYPE html>
<html>
<head>
<meta name="pypi:repository-version" content="1.1">
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?15d27875695f5ffb9252818426884ce8";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
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
subpage_template = Template(subpage_template_str)

# 目录路径，这里假设是当前目录下的whl文件夹
directory_path = 'assets/whl'

# 获取目录下所有的子目录（即包名）
packages = next(os.walk(directory_path))[1]

# 基础URL，这里假设是你的GitHub Pages的URL
# base_url = 'https://raw.githubusercontent.com/myhloli/wheels/main/assets/whl'

base_url = 'https://gitee.com/myhloli/wheels/raw/main/assets/whl'

index_base_url = 'https://myhloli.github.io/wheels/'

# 渲染顶级HTML模板
html_content = template.render(packages=packages, base_url=index_base_url)

# 写入顶级HTML文件
with open('index.html', 'w') as file:
    file.write(html_content)

# 遍历每个包的子目录，生成子页面
for package in packages:
    subdirectory_path = os.path.join(directory_path, package)
    whl_files = [f for f in os.listdir(subdirectory_path) if f.endswith('.whl')]

    # 渲染子页面HTML模板
    subpage_content = subpage_template.render(whl_files=whl_files, base_url=f"{base_url}/{package}/")

    # 创建子目录（如果不存在）
    os.makedirs(package, exist_ok=True)

    # 写入子页面HTML文件
    with open(f'{package}/index.html', 'w') as file:
        file.write(subpage_content)