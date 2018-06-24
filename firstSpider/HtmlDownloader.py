# encoding: utf-8

import requests
import urllib
import os
import re
from bs4 import BeautifulSoup

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
        cookie = '''geoloc=cc=CN,rc=BJ,tp=vhigh,tz=GMT+8,la=39.90,lo=116.41,bw=5000; guidU=4ea39305-02c7-48e9-91e5-f1b3fa7c8f1d; neo.swimlane=16; dreams_sample=26; cicPWIntercept=1; _gscu_207448657=298012097ot0nl73; _gscbrs_207448657=1; _smt_uid=5b2ee9f9.dce3e66; AMCVS_F0935E09512D2C270A490D4D%40AdobeOrg=1; exp.swoosh.user=%7B%22granted%22%3A0%7D; RES_TRACKINGID=673056765826935; ResonanceSegment=1; ajs_user_id=null; ajs_group_id=null; _abck=07E3ACC7E183D39031D48069B54FEDE03CD2126502040000E3E92E5B7745F92D~0~30+XhgQZkKLR/jJ7SmGx/cSpdlXWGVdAqOgRUrsnWOM=~-1~-1; NIKE_COMMERCE_CCR=1529801214369; CONSUMERCHOICE_SESSION=t; CONSUMERCHOICE=us/en_us; nike_locale=us/en_us; NIKE_COMMERCE_COUNTRY=US; NIKE_COMMERCE_LANG_LOCALE=en_US; neo.experiments=%7B%22main%22%3A%7B%223698-interceptor%22%3A%22a%22%2C%220001%22%3A%22a%22%7D%7D; AnalysisUserId=60.210.18.101.10261529801199852; DAPROPS="sdevicePixelRatio:1.25|sdeviceAspectRatio:16/9|bcookieSupport:1"; cto_lwid=eb3e3e85-db9f-4329-b7cc-abc68c2aee11; __ibxl=1; cid=null; ajs_anonymous_id=%22F2BF7F8D6CA7620555953B0C3F327FFC%22; QuantumMetricEnabled=true; _sckey=mb6-5b2eeb5dc49a63.97777544; _scsess=sess-6-5b2eeb5dc4a3d1.51890233; QuantumMetricUserID=618f752d7cade1da4217abc75c009656; QuantumMetricSessionID=33b9215d99a67ea5765fa6da2d2ad190; fs_uid=fullstory.com`BM7A6`5554232560189440:5629499534213120; guidA=6512d23c020400006dec2e5b7802000070020800; USID=8C277CB0103AD8A76F35CBC093406CB0.sin-242-app-us-0; CART_SUMMARY=%7B%22profileId%22+%3A%2217715616175%22%2C%22userType%22+%3A%22DEFAULT_USER%22%2C%22securityStatus%22+%3A%220%22%2C%22cartCount%22+%3A0%7D; guidS=bbf7e22a-7a23-40de-ee3a-5bdf9041d56e; AMCV_F0935E09512D2C270A490D4D%40AdobeOrg=2121618341%7CMCIDTS%7C17707%7CMCMID%7C27225230798053364642425437035795949928%7CMCAAMLH-1530412295%7C11%7CMCAAMB-1530412297%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1529814695s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-17714%7CvVersion%7C2.4.0; utag_main=_st:1529810764355$ses_id:1529808071852%3Bexp-session; guidSTimestamp=1529807495103|1529808965608; stc111680=env:1529807502%7C20180725023142%7C20180624032609%7C2%7C1015907:20190624025609|uid:1529801222596.1976662740.0790873.111680.189729562.:20190624025609|srchist:1015907%3A1529807502%3A20180725023142:20190624025609|tsa:1529807502956.770998976.0815172.3014704950810152.1:20180624032609; bc_nike_triggermail=%7B%22distinct_id%22%3A%20%221642f47b36e189-0aa6e63ed73d84-737356c-144000-1642f47b36f8%22%7D; s_sess=%20c51%3Dhorizontal%3B%20prevList2%3Dgated%253Agender%253Amen%257Cshoes%253A%3B%20s_cc%3Dtrue%3B%20tp%3D32510%3B%20s_ppv%3Dnikecom%25253Epw%25253Emen%25253Eshoes%252C68%252C66%252C22014%3B; RT="dm=nike.com&si=e5cc3c22-1e5e-4b36-a9c4-70351a777f3e&ss=1529808962698&sl=0&tt=0&obo=0&sh=&bcn=%2F%2F36fb78d5.akstat.io%2F&r=https%3A%2F%2Fstore.nike.com%2Fus%2Fen_us%2Fpw%2Fmens-shoes%2F7puZoi3%3Fipp%3D120&ul=1529816368111"'''
        headers={'User-Agent':user_agent, 'accept-language': 'en-US,en;q=0.9', 'cookie': cookie, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}

        r = requests.get(url, headers=headers)

        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        else:
            return None

    def imgDownloader(self, img_url):
        print img_url
        htmlcont =  self.download(img_url)
        soup = BeautifulSoup(htmlcont, 'html.parser', from_encoding='utf-8')
        try:
            wrapper = soup.select('div > picture > img')[1]['src']
        except Exception:
            try:
                wrapper = soup.select('nav > a:nth-of-type(1) > img')[0]['src']
            except Exception:
                try:
                    wrapper = soup.select('.hero-image-container > img')[0]['src']
                except Exception:
                    print Exception
                    return ''
        queryArr = wrapper.encode('utf8').split('/')
        strLen = len(queryArr)
        name = queryArr[strLen-1]
        self.save_img(wrapper.encode('utf8'), file_name=name)
        return wrapper.encode('utf8')

    def save_img(self, img_url, file_name, file_path='img'):
        name = re.sub(r'.tif\?(\D)*$', '.jpg ', file_name)
        # 保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 book\img文件夹
        # 下载图片，并保存到文件夹中
        try:
            if type(int(name[0])) == int:
                name = 'a' + name
        except Exception:
            name = name
        try:
            if not os.path.exists(file_path):
                print '文件夹', file_path, '不存在，重新建立'
                os.makedir(file_path)
            # 获得图片后缀
            file_suffix = ''
            # 拼接图片名（包含路径）
            filename = '{}{}{}{}'.format(file_path, os.sep, name, file_suffix)

            self.auto_down(img_url, filename=filename)
            print 'down succ!'
        except IOError as e:
            print '文件操作失败', e
        except Exception as e:
            print '错误 ：', e

    def auto_down(self, url, filename):
        try:
            urllib.urlretrieve(url, filename)
        except urllib.ContentTooShortError:
            print 'Network conditions is not good.Reloading.'
            self.auto_down(url, filename)

