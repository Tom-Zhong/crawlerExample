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
        cookie = '''crl8.fpcuid=bd2b925e-5e4d-4d69-b786-ba7b6e3bf92a; guidU=4dacd74c-7361-4134-dc96-7650c0ed792c; neo.swimlane=46; dreams_sample=75; RES_TRACKINGID=61612427812157082; ResonanceSegment=1; _gscu_207448657=28075123hyzw0811; _abck=2D126308304BDF26FCBE4C05515D7A8FB833C7B5137100006C93145B425C1349~0~RaJoaT9uiUNvKj9xnVxXDh3muVUTczak8/VN7bWDC0o=~-1~-1; ajs_group_id=null; ajs_user_id=%2220233CC7CB6D3CC897490DF9991B0C52%22; _smt_uid=5b14937b.c66aabc; CONSUMERCHOICE_SESSION=t; CONSUMERCHOICE=us/en_us; AKNIKE=3M9CSSRcfjRq5FIZLVfzaM-XKWMDKCPxjx5ctCzRUjx3xACujQId21g; __ibxl=1; cid=null; cto_lwid=c23a05ca-4986-43d0-bb2a-e1a46d92cf4d; QuantumMetricUserID=10cf7da71c686e9bac66c574a8773a56; _sckey=mb2-5b2cd4b9d8b722.97732293; ajs_anonymous_id=%2220233CC7CB6D3CC897490DF9991B0C52%22; neo.experiments=%7B%22main%22%3A%7B%223698-interceptor%22%3A%22a%22%2C%220001%22%3A%22a%22%7D%2C%22mobile%22%3A%7B%220001%22%3A%22a%22%2C%223698-interceptor%22%3A%22a%22%7D%7D; cto_idcpy=a8630de7-ccb7-478f-b5bd-fa61850eccdc; DAPROPS="sdevicePixelRatio:2|sdeviceAspectRatio:16/10|bcookieSupport:1"; NIKE_COMMERCE_CCR=1529751865720; AnalysisUserId=60.210.18.101.10261529764863356; bm_sz=906B67BFC9288E9BE32A8CD205F59F59~QAAQZRLSPN5fXPhjAQAA7TcmLemjV/Z3i16mOAK1a7EFhQ5O3FVsdFWQXfXQBNq7/IHBoxnbDGi5Llai/cmq2c2VP+W7GN5mtf/Xr9UcEgSjcoRw+OGXTEr4+qdMg0A08j/1GIkI7xmdjz2xl3kGYAW09RtGO15psgnZYY63+KFT5wSgDGF8fXzzlvMZ; bc_nike_triggermail=%7B%22distinct_id%22%3A%20%22164271eec12bb7-069406cce398bf-17366952-232800-164271eec13c36%22%7D; stc111680=env:1529764808%7C20180724144008%7C20180623153257%7C5%7C1015907:20190623150257|uid:1529665725297.1210249951.6933846.111680.1247965777:20190623150257|srchist:1015907%3A1529764808%3A20180724144008:20190623150257|tsa:1529764808951.171565268.54492378.6263386084356446.:20180623153257; fs_uid=fullstory.com`BM7A6`4556502866067456:5704837555552256; guidA=6512d23c020400008e732e5bbd020000cee70700; AKA_A2=A; utag_main=_st:1529772702903$ses_id:1529771480617%3Bexp-session; guidS=4db4a875-194e-4567-94bd-b50444fb0481; guidSTimestamp=1529770903691|1529770903691; niduid=9059d476-598b-4bd7-9b1f-ce10a25c1419; exp.swoosh.user=%7B%22granted%22%3A0%7D; ppd=pdp%3Anikeid%7Cnikecom%3Epdp%3Anikeid%3ENIKE%20AIR%20CLIPPER%20'17%20ID; AMCVS_F0935E09512D2C270A490D4D%40AdobeOrg=1; AMCV_F0935E09512D2C270A490D4D%40AdobeOrg=2121618341%7CMCIDTS%7C17705%7CMCMID%7C76557564149412306991301289362433220392%7CMCAAMLH-1530357401%7C11%7CMCAAMB-1530375712%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1529778112s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-17712%7CvVersion%7C2.4.0; s_pers=%20s_dfa%3Dnikecomprod%7C1529772703575%3B%20c58%3Dno%2520value%7C1529772712157%3B; s_sess=%20c51%3Dhorizontal%3B%20prevList2%3D%3B%20s_cc%3Dtrue%3B; RT="sl=1&ss=1529770901458&tt=6418&obo=0&sh=1529770907888%3D1%3A0%3A6418&dm=nike.com&si=f32121ac-8243-4df0-8624-ae54ff2e204b&bcn=%2F%2F36fb619d.akstat.io%2F&r=https%3A%2F%2Fstore.nike.com%2Fus%2Fen_us%2Fproduct%2Falpha-air-clipper-elite-id%2F%3Fa4922a8319fa69575d0fad57a4dabb51&ul=1529772444776"'''
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
        self.save_img(wrapper.encode('utf8'), file_name=name, file_path='img')
        return wrapper.encode('utf8')

    def save_img(self, img_url, file_name, file_path='img'):
        # 保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 book\img文件夹
        try:
            if not os.path.exists(file_path):
                print '文件夹', file_path, '不存在，重新建立'
                os.makedir(file_path)
            # 获得图片后缀
            # file_suffix = os.path.splitext(img_url)[1]
            # 拼接图片名（包含路径）
            filename = '{}{}{}{}'.format(file_path, os.sep, file_name)
            # 下载图片，并保存到文件夹中
            urllib.urlretrieve(img_url, filename=filename)
        except IOError as e:
            print '文件操作失败', e
        except Exception as e:
            print '错误 ：', e
