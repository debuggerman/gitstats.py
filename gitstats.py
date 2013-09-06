import urllib2
import base64
import json
from link import *;
from GitFetcher import GitHubFetcher;

username = "debuggerman"
password = "megadeth"
orgUrl = "https://api.github.com/orgs"
orgName = "coeus-solutions"

gitFetcher = GitHubFetcher(username = username, password = password, orgUrl = orgUrl, orgName = orgName)
gitFetcher.getOrgInfo()
