import scrapy


class StackOverflowSpider(scrapy.Spider):
    name = "stackoverflow"
    start_urls = [
        # "http://stackoverflow.com/questions?sort=votes"
        'file:///home/lwq/Desktop/lwq/stackoverflow/html/Highest Voted Questions - Stack Overflow.html'
    ]

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)
            # print(full_url)
            # print(href.extract())
            # break

    def parse_question(self, response):
        return {
            'title': response.css('h1 a::text').extract()[0],
            'votes': response.css(".question .vote-count-post::text").extract()[0],
            'body': response.css(".question .post-text").extract()[0],
            'tags': response.css('.question .post-tag::text').extract(),
            'link': response.url,
        }