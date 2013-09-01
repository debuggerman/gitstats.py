import urllib2
import base64
import json
from link import *;
from GitFetcher import *;

username = ""
password = ""
orgUrl = "https://api.github.com/orgs"
orgName = ""

def getAuthUrlRequest(oUrl):
	request = urllib2.Request(oUrl)
	base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
	request.add_header("Authorization", "Basic %s" % base64string)   
	#print "Basic %s" % base64string
	result = urllib2.urlopen(request)
	return result
	pass

def getOrgInfo():
	orgInfo = json.loads(getAuthUrlRequest("%s/%s" % orgUrl, orgName).read())
	return orgInfo
	pass

def getAllRepos(orgInfo):
	reposUrl = orgInfo["repos_url"]

	print "fetching repos at %s" % reposUrl
	#get link header, split on , then split on ;
	reposRequest = getAuthUrlRequest(reposUrl)
	header = reposRequest.info().getheader("Link")
	link = parse_link_value(header)
	print link

	nexturl = ""
	for k in link.keys():
		x = link[k]
		if x["rel"] == "next":
			nexturl = k;
			break;
			pass

	pass

def getAllCommitsSince(reposList, sinceDate):
	#if since date is None, return all
	pass

def getAllComments(commitsList):
	pass

def organizeComments(commentsList):
	pass

# pagination is a problem huston!


orgInfo = getOrgInfo()
reposList = getAllRepos(orgInfo)
commitsList = getAllCommitsSince(reposList = reposList, sinceDate = None)
commentsList = getAllComments(commitsList)


repoUrls = [(repo["name"],repo["url"]) for repo in reposList]

for aRepoUrl in repoUrls:
	print "Getting commits for %s" % aRepoUrl[0]
	repoDetails = json.loads(getAuthUrlRequest(aRepoUrl[1]).read())
	commitUrl = repoDetails["commits_url"]
	commitUrl = commitUrl.replace("{/sha}","")
	commits = json.loads(getAuthUrlRequest(commitUrl).read())
	print "found %d commits..." % len(commits)

