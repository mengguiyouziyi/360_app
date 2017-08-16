# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import base64
from random import choice

# 代理服务器
proxyServer = "http://proxy.abuyun.com:9020"

# 1
# proxyUser = "HFE1U7J80076EKWD"
# proxyPass = "39E53297BE82AEA6"

# 2
# proxyUser = "HGJ3233ZHQ21680D"
# proxyPass = "C69FE010F7C5B14E"

# 3
# proxyUser = "H2R4K25D5KITV1SD"
# proxyPass = "BD8E1C7F384AF1BA"

# 4
proxyUser = "HU382OU308UQFR9D"
proxyPass = "D5AD3D3FF4383DFC"

# 5
# proxyUser = "H4W4C128D84D39ID"
# proxyPass = "AE0738C61F7324E4"


# for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")


class ProxyMiddleware(object):
	def process_request(self, request, spider):
		request.meta["proxy"] = proxyServer
		request.headers["Proxy-Authorization"] = proxyAuth


class RetryMiddleware(object):
	def process_response(self, request, response, spider):
		if response.status == 429:
			# print('wrong status: %s, retrying~~' % response.status, request.url)
			return request.replace(url=request.url)
		else:
			return response

	def process_exception(self, request, exception, spider):
		return request.replace(url=request.url)


class RotateUserAgentMiddleware(object):
	"""Middleware used for rotating user-agent for each request"""

	def __init__(self, agents):
		self.agents = agents

	@classmethod
	def from_crawler(cls, crawler):
		return cls(crawler.settings.get('USER_AGENT_CHOICES', []))

	def process_request(self, request, spider):
		request.headers.setdefault('User-Agent', choice(self.agents))



