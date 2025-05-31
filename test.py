from datascraper.platform import Platform

zhihu = Platform("zhihu")

#print(zhihu.cookies)  # 输出当前平台的 cookies
#zhihu.set_cookies("your_new_cookies_here")  # 动态设置 cookies

response = zhihu.get("https://zhuanlan.zhihu.com/p/52090691")
with open("zhihu.html", "w", encoding="utf-8") as f:
    f.write(response.text)


