import urllib2
import base64
import json
from link import *;

class GitHubFetcher:
	'''This class is supposed to be run rarely. It is very network heavy
	and makes a lot of requests to github. Also make sure to setup the since date.
	Perhaps we can make this class between by using the api.github.com metadata. 
	'''
	username = ""
	password = ""
	orgUrl = ""
	orgName = ""

	def __init__(self, username, password, orgUrl, orgName):
		self.username = username
		self.password = password
		self.orgUrl = orgUrl
		self.orgName = orgName

	def getAuthUrlRequest(self, oUrl):
		request = urllib2.Request(oUrl)
		base64string = base64.encodestring('%s:%s' % (self.username, self.password)).replace('\n', '')
		request.add_header("Authorization", "Basic %s" % base64string)   
		#print "Basic %s" % base64string
		result = urllib2.urlopen(request)
		return result
		pass

	def getOrgInfo(self):
		orgInfo = json.loads(getAuthUrlRequest("%s/%s" % self.orgUrl, self.orgName).read())
		return orgInfo
		pass

	def getAllRepos(self, orgInfo):
		reposUrl = orgInfo["repos_url"]
		
		reposResponse = getAuthUrlRequest(reposUrl)
		header = reposResponse.info().getheader("Link")
		link = parse_link_value(header)

		nexturl = ""
		for k in link.keys():
			x = link[k]
			if x["rel"] == "next":
				nexturl = k;
				break;
				pass

		pass

	def getAllCommitsSince(self, reposList, sinceDate):
		#if since date is None, return all
		pass

	def getAllComments(self, commitsList):
		pass

	def organizeComments(self, commentsList):
		pass

