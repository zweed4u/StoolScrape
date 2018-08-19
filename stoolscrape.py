#!/usr/bin/python3
import json
import requests
import xmltodict

response = requests.request('GET','https://www.barstoolsports.com/sitemap.xml')
response_json = xmltodict.parse(response.content)
for location in response_json['sitemapindex']['sitemap']:
    print("==============================================")
    print(location['loc'])
    print("==============================================")
    response = requests.request('GET',location['loc'])
    response_json = xmltodict.parse(response.content)
    for blog in response_json['urlset']['url']:
        print(f'├─{blog["loc"]}')
    print('└─END OF MONTH/UP-TO-DATE\n')
