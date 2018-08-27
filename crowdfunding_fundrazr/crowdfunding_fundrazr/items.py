# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrowdfundingFundrazrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    campaign_title = scrapy.Field()
    amount_raised = scrapy.Field()
    goal = scrapy.Field()
    currency_type = scrapy.Field()
    end_date = scrapy.Field()
    num_of_contributors = scrapy.Field()
    story = scrapy.Field()
    url = scrapy.Field()
    num_of_photos = scrapy.Field()
    #num_of_facebook_likes = scrapy.Field()
    location = scrapy.Field()
