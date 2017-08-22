# -*- coding: utf-8 -*-
import scrapy
from topgoods.items import TopgoodsItem


class TmGoodsSpider(scrapy.Spider):
    name = "tm_goods"
    allowed_domains = ["www.tmall.com"]
    start_urls = [
        # 'https://list.tmall.com/search_product.htm?type=pc&totalPage=100&cat=50025135&sort=d&style=g&from=sn_1_cat-qp&active=1&jumpto=10#J_Filter',
        # 发生重新定位  https://login.tmall.com/?from=sm&redirect_url=https%3A%2F%2Fsec.taobao.
        # com%2Fquery.htm%3Faction%3DQueryAction%26event_submit_do_login%3Dok%26smApp%3Dtmall
        # search%26smPolicy%3Dtmallsearch-product-anti_Spider-html-checklogin%26smCharset%3DGBK
        # %26smTag%3DMTIzLjEyOS41MS4zNCwsY2E0NWRhMDk0ZWEyNDQ3Njg3NzNlYTEwN2Q1OTdkNWE%253D%26sm
        # Return%3Dhttps%253A%252F%252Flist.tmall.com%252Fsearch_product.htm%253Ftype%253Dpc%25
        # 26totalPage%253D100%2526cat%253D50025135%2526sort%253Dd%2526style%253Dg%2526from%253D
        # sn_1_cat-qp%2526active%253D1%2526jumpto%253D10%26smSign%3DJ9HTJ5Hdm4JF2Yaj9P0SJw%253D
        # %253D
        'file:///home/lwq/Python/Scrapy_tutorial/12/topgoods/html/tm.html'
    ]
    # 记录处理的页数
    count = 0
     
    def parse(self, response):
        print('ok')
        TmGoodsSpider.count += 1
        
        # divs = response.xpath("//div[@id='J_ItemList']/div[@class='product']/div")
        divs = response.xpath("//div[@id='J_ItemList']/div/div")
        if not divs:
            self.log("列表页出错--%s" % response.url)
        print('url', response.url)

        print("商品数量: ", len(divs))
        
        for div in divs:
            item = TopgoodsItem()
            # 商品价格
            # item["GOODS_PRICE"] = div.xpath("p[@class='productPrice']/em/@title")[0].extract()
            item["GOODS_PRICE"] = div.xpath("p[@class='productPrice']/em/@title")[0].extract()
            # 商品名称
            item["GOODS_NAME"] = div.xpath("p[@class='productTitle']/a/@title")[0].extract()
            # 商品连接
            pre_goods_url = div.xpath("p[@class='productTitle']/a/@href")[0].extract()
            item["GOODS_URL"] = pre_goods_url if "https:" in pre_goods_url else ("https://"+pre_goods_url)
            # 图片链接
            try:
                file_urls = div.xpath('div[@class="productImg-wrap"]/a[1]/img/@src|'
                                      'div[@class="productImg-wrap"]/a[1]/img/@data-ks-lazyload').extract()[0]
                file_urls = file_urls.split('/')[-1]
                item['file_urls'] = ['https://img.alicdn.com/bao/uploaded/i3/' + file_urls]
            except Exception as e:
                print("Error: ", e)
                import pdb;pdb.set_trace()
            # yield scrapy.Request(url=item["GOODS_URL"], meta={'item': item}, callback=self.parse_detail,
            #                      dont_filter=True)
            print(item)
            break

    def parse_detail(self, response):

        div = response.xpath('//div[@class="extend"]/ul')
        if not div:
            self.log("Detail Page error--%s" % response.url)
            
        item = response.meta['item']
        div = div[0]
        # 店铺名称
        item["SHOP_NAME"] = div.xpath("li[1]/div/a/text()")[0].extract()
        # 店铺连接
        pre_shop_url = div.xpath("li[1]/div/a/@href")[0].extract()
        item["SHOP_URL"] = response.urljoin(pre_shop_url)
        # 公司名称
        item["COMPANY_NAME"] = div.xpath("li[3]/div/text()")[0].extract().strip()
        # 公司所在地
        item["COMPANY_ADDRESS"] = div.xpath("li[4]/div/text()")[0].extract().strip()
        
        yield item
