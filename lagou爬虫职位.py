from urllib import request
from urllib import parse
import json
import math
import pymongo

MONGO_DB = 'lagouspider'
MONGO_URL = 'localhost'
MONGO_TABLE = '爬虫工程师'

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def save_to_mongo(position):
    if db['MONGO_TABLE'].insert(position):
        print('保存成功', position)
    else:
        print('保存失败', position)


def get_html(url, headers, data):
    data = bytes(parse.urlencode(data), encoding='utf-8')
    req = request.Request(url, headers=headers, data=data, method='POST' )
    html = request.urlopen(req).read().decode()
    results = json.loads(html)
    return results


def get_page(url, headers):
    data = {
        'first':'true',
        'pn': 1,
        'kd': '爬虫工程师'
    }
    results = get_html(url, headers, data)
    pageSize = results['content']['pageSize']
    totalCount = results['content']['positionResult']['totalCount']
    page = math.ceil(totalCount/float(pageSize))
    return page
    # print(page)



def get_position_info(url, headers, page):
    for pn in range(1, page+1):
        data = {
            'first': 'true',
            'pn': pn ,
            'kd': '爬虫工程师'
        }
        aa = get_html(url, headers, data)
        results = aa['content']['positionResult']['result']
        for result in results:
            position = {
                'positionName':result['positionName'],
                'city':result['city'],
                'companyFullName':result['companyFullName'],
                'education':result['education'],
                'jobNature':result['jobNature'],
                'salary':result['salary'],
                'workYear':result['workYear']
            }
            save_to_mongo(position)

            # print(position)
#主体函数
if __name__=='__main__':
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
    headers={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': 64 ,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '_ga=GA1.2.1008389041.1525852646; user_trace_token=20180509155713-95b4f0eb-535e-11e8-9366-525400f775ce; LGUID=20180509155713-95b4f4d4-535e-11e8-9366-525400f775ce; index_location_city=%E6%B7%B1%E5%9C%B3; WEBTJ-ID=20180831165256-1658f2f747333a-0e7135a7d21967-323b5b03-1049088-1658f2f747718; _gid=GA1.2.1433543034.1535705577; LGSID=20180831165255-40c5eb61-acfb-11e8-be6f-525400f775ce; JSESSIONID=ABAAABAAAIAACBIDC490D13E8EE2886BB732F33CF7A467A; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1535335749,1535514160,1535705577,1535705603; LGRID=20180831165912-21618f54-acfc-11e8-b30a-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1535705954; TG-TRACK-CODE=search_code; SEARCH_ID=c7da36d5cbb848f380a582ba9a18247c',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB%E5%B7%A5%E7%A8%8B%E5%B8%88?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=sug&suginput=pachong',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'X-Anit-Forge-Code': 0 ,
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest'
    }
    page = get_page(url, headers)#获得页码
    get_position_info(url, headers, page)#获取招聘信息
