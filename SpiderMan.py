# encoding: utf-8
from firstSpider.DataOutput import DataOutput
from firstSpider.HtmlDownloader import HtmlDownloader
from firstSpider.UrlManager import UrlManager
from firstSpider.HtmlParser import HtmlParser
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawlHTML(self, root_url):

        # 添加入口URL
        self.manager.add_new_url(root_url)

        # 判断url管理中时候是否有新的url， 同时判断抓取了多少个url
        while(self.manager.has_new_url()):
            try:
                # 从URL管理器获取新的url
                new_url = self.manager.get_new_url()
                # HTML下载器下载网页
                html = self.downloader.download(new_url)
                # HTML解析器抽取网页数据
                self.parser.parser(new_url, html)
            except Exception,e:
                print e
                print "crawl failed"

        # 数据存储器将文件输出成指定格式
        # self.output.output_html()
    def crawlJSON(self, root_url, rangeStart=0, rangeStop=1):

        for i in range(rangeStart, rangeStop):
            try:
                url = root_url + str(i)
                self.manager.add_new_url(url)
                print url
                # 从URL管理器获取新的url
                new_url = self.manager.get_new_url()
                # HTML下载器下载网页
                JSON = self.downloader.download(new_url)
                # print JSON
                # HTML解析器抽取网页数据
                print '第' + str(i) + '个JSON'
                self.parser.parserJSON(JSON)
            except Exception,e:
                print e
                print "crawl failed"

if __name__ == '__main__':
    spider_man = SpiderMan()
    # spider_man.crawlHTML('https://store.nike.com/us/en_us/pw/mens-shoes/7puZoi3?ipp=120')
    spider_man.crawlJSON('https://store.nike.com/html-services/gridwallData?country=US&lang_locale=en_US&gridwallPath=mens-shoes/7puZoi3&pn=', 3, 13)