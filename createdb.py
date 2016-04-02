# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import rethinkdb as r
try:
    from settings import RDB_HOST, RDB_PORT, RDB_DATABASE
except:
    RDB_HOST = "localhost"
    RDB_PORT = 28015
    RDB_DATABASE = "Mawto"
    RDB_AUTHKEY = "atom"
table1 = "ArticleURL"
table2 = "ArticleMeta"
table3 = "ArticleGnews"
table4 = "ArticleSummaryMain"
table5 = "ArticleMedia"
table6 = "ArticleSummaryBasic"
r.connect(RDB_HOST, RDB_PORT, 'rethinkdb', RDB_AUTHKEY).repl()

    ##create the requested db if it does not exist
if RDB_DATABASE not in r.db_list().run():
    r.db_create(RDB_DATABASE).run()


    ##create the required table if it does not exist
if table1 not in r.db(RDB_DATABASE).table_list().run():
    r.db(RDB_DATABASE).table_create(table1, primary_key='link').run()
    r.db(RDB_DATABASE).table(table1).wait().run()
    r.db(RDB_DATABASE).table(table1).index_create("id").run()
    ##create the required table if it does not exist
if table2 not in r.db(RDB_DATABASE).table_list().run():
    r.db(RDB_DATABASE).table_create(table2, primary_key='link').run()
    r.db(RDB_DATABASE).table(table2).wait().run()
    r.db(RDB_DATABASE).table(table2).index_create("title").run()
    r.db(RDB_DATABASE).table(table2).index_create("id").run()
    r.db(RDB_DATABASE).table(table2).index_create("keywords", multi=True).run()
    ##create the required table if it does not exist
if table3 not in r.db(RDB_DATABASE).table_list().run():
    r.db(RDB_DATABASE).table_create(table3, primary_key='link').run()
    r.db(RDB_DATABASE).table(table3).wait().run()
    r.db(RDB_DATABASE).table(table3).index_create("id").run()
    r.db(RDB_DATABASE).table(table3).index_create("topstory").run()
    r.db(RDB_DATABASE).table(table3).index_create("sublinks").run()

if table4 not in r.db(RDB_DATABASE).table_list().run():
    r.db(RDB_DATABASE).table_create(table4, primary_key = 'link').run()
    r.db(RDB_DATABASE).table(table4).wait().run()
    r.db(RDB_DATABASE).table(table4).index_create("id").run()
    r.db(RDB_DATABASE).table(table4).index_create("title").run()


if table5 not in r.db(RDB_DATABASE).table_list().run():
    r.db(RDB_DATABASE).table_create(table5, primary_key = 'link').run()
    r.db(RDB_DATABASE).table(table5).wait().run()
    r.db(RDB_DATABASE).table(table5).index_create("id").run()
    r.db(RDB_DATABASE).table(table5).index_create("top_image").run()

if table6 not in r.db(RDB_DATABASE).table_list().run():
    r.db(RDB_DATABASE).table_create(table6, primary_key = 'link').run()
    r.db(RDB_DATABASE).table(table6).wait().run()
    r.db(RDB_DATABASE).table(table6).index_create("id").run()
    r.db(RDB_DATABASE).table(table6).index_create("title").run()

r.db('rethinkdb').table('cluster_config').get('auth').update({'auth_key': RDB_AUTHKEY})

