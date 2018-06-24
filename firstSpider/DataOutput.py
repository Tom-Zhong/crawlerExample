# encoding: utf-8

import codecs
import csv
class DataOutput(object):

    def __init__(self):
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = codecs.open('baike.html', 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<head><meta charset="UTF-8"></head>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>'%data['url'])
            # fout.write('<td>%s</td>'%data['title'])
            # fout.write('<td>%s</td>'%data['summary'])
            fout.write('</tr>')
            self.datas.remove(data)
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()

    def output_csv(self, headers='name'):
        with open('nikeShop.csv', 'w') as f:
            f_csv = csv.DictWriter(f,headers)
            f_csv.writeheader()
            print self.datas
            f_csv.writerows(self.datas)