import scrapy
from helphopelive.items import HelphopeliveItem
from datetime import datetime
import re

class Crowdfund_Helphopelive(scrapy.Spider):
    name = "helphopelive_scraper"
    #make list of all start urls   
    
    def start_requests(self):
        start_urls = ["https://helphopelive.org/campaign/10798/"]
        for url in start_urls:
            yield scrapy.Request(url=url,callback=self.parse)
    #start_urls = []
    #for i in range(5100, 5110):
        #start_urls.append("https://helphopelive.org/campaign/" + str(i) + "/")
    
         
    def parse(self, response):
        #url = response.xpath("//meta[@property='og:url']/@content").extract()[0]
        
        #yield scrapy.Request(url, callback=self.parse_dir_contents)
        
        #for url in start_urls:
         #   yield scrapy.Request(url, callback=self.parse_dir_contents) 
        #get individual campaign
        #href = response.xpath("//h2[contains(@class, 'title headline-font')]/a[contains(@class, 'campaign-link')]//@href"):
        # add the scheme
             
    
    #def parse_dir_contents(self, response):
        #create instance of the item
        sample = HelphopeliveItem()
        
        #get campaign title
        sample['campaign_title'] = response.xpath("//section[contains(@class,'campaign-element campaign-lead')]//h1[contains(@class,'lead')]/descendant::text").extract()[0]
        
        #get amount raised
        sample['amount_raised'] = response.xpath("//span[contains(@class,'teal')]/descendant::text()").extract()[0]
        
        #get the location
        sample['location'] = response.xpath("//p[contains(@class,'location')]/descendant::text()").extract()[0]
        
        #get the goal
        sample['goal'] = response.xpath("//div[contains(@class,'profile-lockup__footer')]/p/text()").extract()[0]
        
        #get the story
        sample['story'] = " ".join(response.xpath("//section[contains(@class,'campaign-element campaign-lead')]//p/text()").extract())
        
        #get the url
        sample['url'] = response.xpath("//meta[@property='og:url']/@content").extract()[0]
        
        #get the number of photos
        sample['num_of_photos'] = response.xpath("//div[contains(@class,'campaign-element__header')]//span[contains(@class,'photos-total')]/text()").extract()[0]
        
        yield sample