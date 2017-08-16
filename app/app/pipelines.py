# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from app.items import AppItem, LikeItem


class MysqlPipeline(object):
	"""
	本机 localhost；公司 etl2.innotree.org；服务器 etl1.innotree.org
	"""

	def __init__(self):
		self.conn = pymysql.connect(host='etl2.innotree.org', port=3308, user='spider', password='spider', db='spider',
		                            charset='utf8', cursorclass=pymysql.cursors.DictCursor)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		if isinstance(item, AppItem):
			sql = """replace into 360app(pic, soft_name, is_official, score, down_num, apk_size, remark, pac_name, app_id, app_cat, des, overview, auth, update_time, version, sys, lang, tag, likes, comm_num, best_num, good_num, bad_num, crawl_time) 
					VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
			args = (
				item['pic'], item['soft_name'], item['is_official'], item['score'], item['down_num'], item['apk_size'],
				item['remark'], item['pac_name'], item['app_id'], item['app_cat'], item['des'], item['overview'],
				item['auth'], item['update_time'], item['version'], item['sys'], item['lang'], item['tag'],
				item['likes'],
				item['comm_num'], item['best_num'], item['good_num'], item['bad_num'], item['crawl_time']
			)
			self.cursor.execute(sql, args=args)
			self.conn.commit()
			print(str(item['app_id']) + ' app')
		# print(str(item['app_id']))

		elif isinstance(item, LikeItem):
			sql = """replace into 360app_like(app_id, soft_id, pname, soft_name, download_urls, download_times, apk_sizes, logo_url, vote_scores, rate, apk_md5, cnxhtype, app_cat, diadian, soft_sub_name, origin) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
			args = (item["app_id"], item["soft_id"], item["pname"], item["soft_name"], item["download_urls"],
			        item["download_times"], item["apk_sizes"], item["logo_url"], item["vote_scores"], item["rate"],
			        item["apk_md5"], item["cnxhtype"], item["app_cat"], item["diadian"], item["soft_sub_name"],
			        item["origin"])
			self.cursor.execute(sql, args=args)
			self.conn.commit()
			print(str(item['soft_id']) + ' soft')
		# print(str(item['soft_id']))
