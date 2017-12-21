BOT_NAME = 'job51'

SPIDER_MODULES = ['job51.spiders']
NEWSPIDER_MODULE = 'job51.spiders'

MYSQL_HOSTS = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_PORT = 3306
MYSQL_DB = 'job51'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'job51.pipelines.Job51Pipeline': 300,
}

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
