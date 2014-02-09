__author__ = 'aa'


import itertools
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from wo.items import WoItem
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
print sys.getdefaultencoding()

class Wo(BaseSpider):
    name = "test"
    allowed_domains = ["ccf.org.cn"]
    start_urls = ["http://www.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2567814757416",
                  #"http://www.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2567814757420",
                  #"http://www.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2567814757428",
                  #"http://www.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2567814757404",
                  #"http://www.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2567518742937",
                  #"http://www.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2567814757408",
                  #"http://www.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2567814757424",
                  #"http://www.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2567814757412",
                  #"http://www.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2624633320934",
                  #"http://www.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2567814757432"
                  ]


    def parse(self, response):
        x = Selector(response)
        items = []

        filename = response.url.split("/")[-2]
        print filename
        #file = open(filename, 'wb')

        title = x.xpath("//html/head/title/text()").extract()
        print title[0]
        category = x.xpath("//span[@id='pt8081field']/text()").extract()
        print isinstance(category[0], unicode)
        print category[0]

        i = 0
        lei = x.xpath('//table[1][@width="850"]/tbody/tr')
        print len(lei)

        for ti in lei:
            if i == 0:
                i = i + 1
                continue
            item = WoItem()
            print "check level 1"
            tii = ti.xpath('.//td[1]/*/text()').extract()
            if len(tii) > 0:
                print tii[0], len(tii[0])
                item['ranking'] = tii[0]
                item['category'] = category[0]
                item['level'] = "A"
            else:
                tii = ti.xpath('.//td[1]/text()').extract()
                if len(tii) > 0:
                    print tii[0]
                    item['ranking'] = tii[0]
                    item['category'] = category[0]
                    item['level'] = 'A'

            name = ti.xpath('.//td[2]/*/text()').extract()
            if len(name) > 0:
                print name[0]
                item['name'] = name[0]
            else:
                name = ti.xpath('.//td[2]/text()').extract()
                if len(name) > 0:
                    print name[0]
                    item['name'] = name[0]

            fullname = ti.xpath('.//td[3]/*/text()').extract()
            if len(fullname) > 0:
                print "".join(itertools.chain(*fullname))
                item['fullname'] = "".join(itertools.chain(*fullname))
            else:
                fullname = ti.xpath('.//td[3]/text()').extract()
                if len(fullname) > 0:
                    print "".join(itertools.chain(*fullname))
                    item['fullname'] = "".join(itertools.chain(*fullname))

            url = ti.xpath('.//td[5]/*/a/@href').extract()
            if len(url) > 0:
                print url[0]
                item['url'] = url[0]
            else:
                url = ti.xpath('.//td[5]/a/@href').extract()
                if len(url) > 0:
                    print url[0]
                    item['url'] = url[0]

            items.append(item)

        i = 0
        lei = x.xpath('//table[@width="850"][5]/tbody/tr')

        for ti in lei:
            if i == 0:
                i = i + 1
                continue
            item = WoItem()
            print "check level 2"
            tii = ti.xpath('.//td[1]/*/text()').extract()
            if len(tii) > 0:
                print tii[0]
                item['ranking'] = tii[0]
                item['category'] = category[0]
                item['level'] = 'B'
            else:
                tii = ti.xpath('.//td[1]/text()').extract()
                if len(tii) > 0:
                    print tii[0]
                    item['ranking'] = tii[0]
                    item['category'] = category[0]
                    item['level'] = 'B'

            name = ti.xpath('.//td[2]/*/text()').extract()
            if len(name) > 0:
                print name[0]
                item['name'] = name[0]
            else:
                name = ti.xpath('.//td[2]/text()').extract()
                if len(name) > 0:
                    print name[0]
                    item['name'] = name[0]

            fullname = ti.xpath('.//td[3]/*/text()').extract()
            if len(fullname) > 0:
                print "".join(itertools.chain(*fullname))
                item['fullname'] = "".join(itertools.chain(*fullname))
            else:
                fullname = ti.xpath('.//td[3]/text()').extract()
                if len(fullname) > 0:
                    print "".join(itertools.chain(*fullname))
                    item['fullname'] = "".join(itertools.chain(*fullname))

            url = ti.xpath('.//td[5]/*/a/@href').extract()
            if len(url) > 0:
                print url[0]
                item['url'] = url[0]
            else:
                url = ti.xpath('.//td[5]/a/@href').extract()
                if len(url) > 0:
                    print url[0]
                    item['url'] = url[0]

            items.append(item)

        i = 0
        lei = x.xpath('//table[@width="850"][6]/tbody/tr')
        for ti in lei:

            if i == 0:
                i = i + 1
                continue

            item = WoItem()
            print "check level 3"
            tii = ti.xpath('.//td[1]/*/text()').extract()
            if len(tii) > 0:
                print tii[0]
                item['ranking'] = tii[0]
                item['category'] = category[0]
                item['level'] = 'C'
            else:
                tii = ti.xpath('.//td[1]/text()').extract()
                if len(tii) > 0:
                    print tii[0]
                    item['ranking'] = tii[0]
                    item['category'] = category[0]
                    item['level'] = 'C'

            name = ti.xpath('.//td[2]/*/text()').extract()
            if len(name) > 0:
                print name[0]
                item['name'] = name[0]
            else:
                name = ti.xpath('.//td[2]/text()').extract()
                if len(name) > 0:
                    print name[0]
                    item['name'] = name[0]

            fullname = ti.xpath('.//td[3]/*/text()').extract()
            if len(fullname) > 0:
                print "".join(itertools.chain(*fullname))
                item['fullname'] = "".join(itertools.chain(*fullname))
            else:
                fullname = ti.xpath('.//td[3]/text()').extract()
                if len(fullname) > 0:
                    print "".join(itertools.chain(*fullname))
                    item['fullname'] = "".join(itertools.chain(*fullname))

            url = ti.xpath('.//td[5]/*/a/@href').extract()
            if len(url) > 0:
                print url[0]
                item['url'] = url[0]
            else:
                url = ti.xpath('.//td[5]/a/@href').extract()
                if len(url) > 0:
                    print url[0]
                    item['url'] = url[0]

            items.append(item)

        #open(filename, 'wb').write(item)
        return items

    """
        strlist = x.select("//h1/@title").extract()
        if len(strlist) > 0:
            item['name'] = strlist[0]

        strlist = x.select("//div[@class='doc-info-price']//span[@class='txt-now-price-num']/text()").extract()
        if len(strlist) > 0:
            item['price'] = strlist[0]

        strlist = x.select("//div[@class='privilege-price']/span[contains(@style, 'color:')]/text()").extract()
        if len(strlist) > 0:
            item['memprice'] = strlist[0]

        strlist = x.select("//ul[@class='doc-info-org']/li/text()").extract()

        count = len(strlist)
        if count > 0:
            item['author'] = strlist[0]

        if count > 1:
            item['publication'] = strlist[1]

        if count > 2:
            item['press'] = strlist[2]


        strlist = x.select("//div[@class='des-content']/p/text()").extract()
        if len(strlist) > 0:
            item['desc'] = strlist[0]

        strlist = x.select("//li/a[contains(@data-logsend, 'send')]/text()").extract()

        belong = ""
        index = 0
        for str in strlist:
            index += 1
            if index <= 1:
                continue

            if len(belong) <= 0:
                belong += str
            else:
                belong += "->"+str

        item['belong'] = belong

        self.log(item['url']+"    "+item['name'])
        return item
    """