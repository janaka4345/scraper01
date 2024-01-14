# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BooksPipeline:
    def process_item(self, item, spider):
        adapter=ItemAdapter(item)
        field_names=adapter.field_names()
        for field_name in field_names:
            if field_name !='description':
                value=adapter.get(field_name)
                adapter[field_name]=value.strip()
        return item

from pymongo import MongoClient

class SaveToMOngoDBPipeline:
    def process_item(self,item,spider):
        client = MongoClient('mongodb+srv://<usernam>:<pasward>@mer-learn2.ehyuufp.mongodb.net/')
        db = client['books_to_scrape']
        collection = db['allBooks2']
        collection.insert_one(dict(item))
        return item 
    
    def close_spider(self,spider):
        MongoClient.close()

        

