from .sql import Sql
from items import Job51Item

class Job51Pipeline(object):
    def process_item(self, item, spider):
            zhiwei = item['zhiwei']
            gongsi = item['gongsi']
            didian = item['didian']
            xinzi = item['xinzi']
            gongsileixing = item['gongsileixing']
            guimo = item['guimo']
            hangye = item['hangye']
            jingyan = item['jingyan']
            xueli = item['xueli']
            fuli = item['fuli']
            zhiweiyaoqiu = item['zhiweiyaoqiu']
            lianjie = item['lianjie']
            Sql.insert_job51(zhiwei, gongsi, didian, xinzi, gongsileixing, guimo, hangye, jingyan, xueli, fuli, zhiweiyaoqiu, lianjie)
            print('写入职位信息')
