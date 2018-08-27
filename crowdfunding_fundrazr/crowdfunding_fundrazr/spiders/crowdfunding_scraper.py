import scrapy
from crowdfunding_fundrazr.items import CrowdfundingFundrazrItem
from datetime import datetime
import re

class Crowfund_Fundrazr(scrapy.Spider):
    name = "fundrazr_scraper"
    
    #start url
    start_urls = ["https://fundrazr.com/find?category=Health"]
    
    num_pages = 500
    
    #add all start urls
    for i in range(2, num_pages + 2):
        start_urls.append("https://fundrazr.com/find?category=Health&page=" + str(i) + "")
        
    def parse(self, response):
        #get individual campaigns on a page
        for href in response.xpath(
                "//h2[contains(@class, 'title headline-font')]/a[contains(@class, 'campaign-link')]//@href"):
            # add the scheme, eg http://
            url = "https:" + href.extract()
            yield scrapy.Request(url, callback=self.parse_dir_contents)   
            
    def parse_dir_contents(self, response):
        sample = CrowdfundingFundrazrItem()
        
        #get campaign title
        sample['campaign_title'] = response.xpath("//div[contains(@id, 'campaign-title')]/descendant::text()").extract()[
            0].strip()
        
        #get amount raised
        sample['amount_raised'] = float(response.xpath(
            "//span[contains(@class, 'stat')]/span[contains(@class, 'amount-raised')]/descendant::text()").extract()[0].replace(',', ''))
        
        #get the goal
        sample['goal'] = float(" ".join(response.xpath(
            "//div[contains(@class, 'stats-primary with-goal')]//span[contains(@class, 'stats-label hidden-phone')]/text()").extract()).strip()[4:-6])*1000
        
        #get currency type
        sample['currency_type'] = response.xpath("//div[contains(@class, 'stats-primary with-goal')]/@title").extract()[0] 
        
        #get end date
        sample['end_date'] = "".join(response.xpath(
            "//div[contains(@id, 'campaign-stats')]//span[contains(@class,'stats-label hidden-phone')]/span[@class='nowrap']/text()").extract()).strip()
        
        #get number of contributors
        sample['num_of_contributors'] = int(response.xpath(
            "//div[contains(@class, 'stats-secondary with-goal')]//span[contains(@class, 'donation-count stat')]/text()").extract()[0])
        
        #get story 
        story_list = response.xpath("//div[contains(@id, 'full-story')]/descendant::text()").extract()
        story_list = [x.strip() for x in story_list if len(x.strip()) > 0]
        sample['story'] = " ".join(story_list)
        
        #get url
        sample['url'] = response.xpath("//meta[@property='og:url']/@content").extract()[0]
        
        #get number of photos
        sample['num_of_photos'] = int(response.xpath("//span[contains(@class,'media-count')]/descendant::text()").extract()[0][1:-1])
        
        #get number of facebook likes
        #sample['num_of_facebook_likes'] = 
        
        #get location
        sample['location'] = response.xpath("//span[contains(@class, 'small muted nowrap dot-after')]/a[contains(@class,'muted nowrap')]/text()").extract()[0]
        
        yield sample


        
        