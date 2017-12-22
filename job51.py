import re
import scrapy
from bs4 import BeautifulSoup
from items import Job51Item

class Myspider(scrapy.Spider):
    name = 'job51'
    allowed_domains = ['51job.com']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

    def start_requests(self):
        for i in range(1, 208):
            url_1 = 'http://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%25E5%25B8%2588,2,'
            url_2 = '.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
            url = url_1 + str(i) + url_2
            yield scrapy.Request(url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        tls = soup.find_all('p', class_='t1 ')
        for tl in tls:
            url = tl.find('a', target='_blank')['href']
            yield scrapy.Request(url, callback=self.get_content, meta={'url': url})

    def get_content(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        item = Job51Item()
        item['zhiwei'] = soup.find('h1').get_text().replace('\xa0', '')
        item['gongsi'] = soup.find('p', class_='cname').find('a', target='_blank').get_text().replace('\xa0', '')
        item['didian'] = soup.find('span', class_='lname').get_text().replace('\xa0', '')
        item['xinzi'] = soup.find('div', class_='cn').find('strong').get_text().replace('\xa0', '')
        gongsixinxi = soup.find('p', class_='msg ltype').get_text().replace('\t', '').replace('\r', '').replace('\n', '').replace('\xa0', '')
        item['gongsileixing'] = gongsixinxi.split('|')[0]
        item['guimo'] = gongsixinxi.split('|')[1]
        item['hangye'] = gongsixinxi.split('|')[2]
        zhaopinyaoqiu = soup.find('div', class_='t1').get_text().replace('\xa0', '')
        item['jingyan'] = zhaopinyaoqiu.split('\n')[1]
        try:
            item['xueli'] = re.findall(r'<em class="i2"></em>(.*?)</span>', response.text)[0]
        except:
            item['xueli'] = '无'
        try:
            item['fuli'] = soup.find('p', class_='t2').get_text().replace('\n', ' ').replace('\xa0', '')
        except:
            item['fuli'] = '无'
        item['zhiweiyaoqiu'] = re.findall(r'<div class="bmsg job_msg inbox">(.*?)<div class="mt10">', response.text, re.I|re.S|re.M)[0]\
            .replace('\r', '').replace('\n', '').replace('\t', '').replace('\xa0', '').replace('<br>', '')\
            .replace('<br/>', '').replace('<P>', '').replace('</P>', '').replace('?', ' ').replace('<p>', '').replace('</p>', '')\
            .replace('<div>', '').replace('</div>', '').replace('<BR>', '').replace('</BR>', '')
        item['lianjie'] = response.meta['url']
        yield item




