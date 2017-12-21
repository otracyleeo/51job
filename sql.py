import pymysql.cursors
import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = pymysql.connect(
    host=MYSQL_HOSTS,
    port=MYSQL_PORT,
    user=MYSQL_USER,
    passwd=MYSQL_PASSWORD,
    db=MYSQL_DB,
    charset='gbk')
cur = cnx.cursor()

class Sql:
    @classmethod
    def insert_job51(cls, zhiwei, gongsi, didian, xinzi, gongsileixing, guimo, hangye, jingyan, xueli, fuli, zhiweiyaoqiu, lianjie):
        sql = 'INSERT INTO job51(zhiwei,gongsi,didian,xinzi,gongsileixing,guimo,hangye,jingyan,xueli,fuli,zhiweiyaoqiu,lianjie) ' \
              'VALUES(%(zhiwei)s,%(gongsi)s,%(didian)s,%(xinzi)s,%(gongsileixing)s,%(guimo)s,%(hangye)s,%(jingyan)s,%(xueli)s,%(fuli)s,%(zhiweiyaoqiu)s,%(lianjie)s)'
        value = {'zhiwei': zhiwei,
                 'gongsi': gongsi,
                 'didian': didian,
                 'xinzi': xinzi,
                 'gongsileixing': gongsileixing,
                 'guimo': guimo,
                 'hangye': hangye,
                 'jingyan': jingyan,
                 'xueli': xueli,
                 'fuli': fuli,
                 'zhiweiyaoqiu': zhiweiyaoqiu,
                 'lianjie': lianjie,}
        cur.execute(sql, value)
        cnx.commit()
