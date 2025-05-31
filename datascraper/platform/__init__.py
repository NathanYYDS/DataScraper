import requests
import json
import os
from .config import CONFIG_FILENAME

class Platform:
    def __init__(self, name: str):
        self.name = name.lower()
        self.config = self._load_config()
        self.cookies = self.config[self.name]["cookies"]
        self.session = requests.Session()
        self._init_session()

    def _load_config(self):
        if not os.path.exists(CONFIG_FILENAME):
            raise FileNotFoundError(f"Config file '{CONFIG_FILENAME}' not found. Please run 'datascraper platform --init' first.")

        with open(CONFIG_FILENAME, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _init_session(self):
        """初始化 session，默认带上 cookies"""
        if self.cookies:
            self.session.headers.update({
                "Cookie": self.cookies,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            })
        else:
            print(f"[!] No cookies found for {self.name}. Please manually set cookies in the config file.")

    def get(self, url, **kwargs):
        return self._request("GET", url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self._request("POST", url, data=data, json=json, **kwargs)

    def _request(self, method, url, **kwargs):
        kwargs.setdefault("timeout", 10)
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"[!] Request failed: {e}")
            return None

    def set_cookies(self, cookies: str):
        """动态设置 cookies 并保存到配置文件"""
        self.cookies = cookies
        self.config[self.name]["cookies"] = cookies
        with open(CONFIG_FILENAME, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)
        self._init_session()  # 重新初始化 session headers
        print(f"[+] {self.name.capitalize()} cookies updated.")

    def set_headers(self, headers: dict):
        """设置额外的请求头"""
        self.session.headers.update(headers)