# encoding: utf-8

import re
import urlparse
from bs4 import BeautifulSoup
from urllib import unquote
from firstSpider.HtmlDownloader import HtmlDownloader
from firstSpider.DataOutput import DataOutput
import json
class HtmlParser(object):
    def __init__(self):
        self.htmlDownloader = HtmlDownloader()
        self.dataOutput = DataOutput()
    def parser(self, page_url, html_cont):
        '''
        用于解析网页内容， 抽取URL和数据
        :param page_url: 下载页面的URL
        :param html_cont:  下载的网页内容
        :return: 返回URL和数据
        '''

        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        return new_urls

    def _get_new_urls(self, page_url, soup):
        '''
        抽取新的URL集合
        :param page_url: 下载页面的URl
        :param soup: soup
        :return: 返回新的URL集合
        '''

        new_urls = set()
        #抽取符合要求的a标记
        wrapper = soup.select('div.exp-gridwall-standard > div.exp-product-wall > div')
        # print len(wrapper)
        i = 0
        headers = ['title', 'category', 'link', 'price']
        for child in wrapper:
            link =  child.div.div.div.div.a['href'].encode('utf8')
            imgLink = self.htmlDownloader.imgDownloader(link).encode('utf8')

            name = child.div.select('.product-display-name')[0].string.encode('utf8')
            category =  child.div.select('.product-subtitle')[0].string.encode('utf8')
            price =  child.div.select('.local.nsg-font-family--base')[0].string.encode('utf8')
            if name == None:
                name = ''
            if category == None:
                category = ''
            if imgLink == None:
                imgLink = ''
            if price == None:
                price = '0'
            data = {'title': name, 'category':category, 'link':imgLink, 'price': price}
            print('目前下载进度： ' + str(i))
            i = i + 1
            self.dataOutput.datas.append(data)
            print data
        self.dataOutput.output_csv(headers)
        return new_urls

    def _get_new_data(self, page_url, soup):

        '''
        抽取有效数据
        :param page_url:下载页面的URL
        :param soup:
        :return: 返回有效数据
        '''
        data = {}
        data['url'] = unquote(page_url)
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')

        # 获取ta中包含的所有的文本内容， 包括子孙tag中的内容， 并将结合作为Unicode字符串返回
        data['summary'] = summary.get_text()

        return data

    def parserJSON(self, jsonData):
        if jsonData is None:
            return
        text = json.loads(jsonData)
        print text['sections'][0]['items'][0]
