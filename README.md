# DataScraper
各大平台数据抓取

## 使用方法
```bash
# 安装依赖
pip install requirements
cd DataScraper
pip install -e .

# 初始化平台cookie文件
datascraper platform --init
```

手动在platform_config.json中或者使用类的`set_cookies`方法配置平台cookie信息，然后运行test.py进行测试。