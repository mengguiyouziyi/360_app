# coding:utf-8

import os
import sys
from os.path import dirname

from .my_redis import QueueRedis


father_path = os.path.abspath(dirname(__file__))
sys.path.append(father_path)


red = QueueRedis()


def get_key(key):
	results = red.read_from_queue(key, 1)
	if results:
		result = results[0].decode().strip()
		# print(result)
		return result
	else:
		return 0








# """
# 本机 localhost；服务器 a027.hb2.innotree.org
# """
# red = QueueRedis()
#
#
# def get_id():
# 	results = red.read_from_queue('ids', 1)
# 	if results:
# 		result = int(results[0])
# 		return result
# 	else:
# 		return 0
