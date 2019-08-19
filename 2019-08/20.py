#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/20 7:45
# @Author :zhai shuai

""""
1 进行文章爬取的时候，我们定义的start.py是启动项目，就不用到命令行去执行
    其命令是：
    from scrapy import cmdline

    cmdline.execute(["scrapy","crawl","爬虫名称"])

2 scrapy 爬虫
    class Bmw5Spider(scrapy.Spider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    def parse(self, response):
        #取出所有的ubox
        uiboxs = response.xpath("//div[@class='uibox']")[1:]  ########注意这个地方，response.xpath返回来的是一个列表就可以用list的方法

        #取出它每一个uibox下面的title
        for uibox in uiboxs:
            category = uibox.xpath(".//div[@class='uibox-title']/a[position()=1]/text()").get()
            imgs = uibox.xpath("//ul/li/a/img/@src").getall()

            # for img in imgs:
            #     img = response.urljoin(img)  #########注意这个地方，response有一个方法，可以把一个字符串变成url的形式，就是加上https
            #     print(img)

            imgsurl = list(map(lambda url:response.urljoin(url),imgs)) ###########注意lambda表达式的写法

            item = items.BmwItem(category=category,imgsurl=imgsurl)
            yield item

"""
