import requests
import json
import pymongo

MONGO_URL = 'localhost' #数据的地址
MONGO_DB = 'zhilianspider' #数据库的名字
MONGO_TABLE = 'job' #数据库的集合名

client = pymongo.MongoClient(MONGO_URL) #与数据库建立连接
db = client[MONGO_DB] #数据库名不存在，则创建数据库


#保存数据到MongoDB
def save_to_mongo(info):
    if db[MONGO_TABLE].insert(info):
        print('保存成功', info)
    else:
        print('保存失败', info)


def get_url():
    header = {
    #     'Accept': 'application/json, text/plain, */*',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'zh-CN,zh;q=0.9',
    #     'Connection': 'keep-alive',
        'Cookie': 'adfbid2=0; sts_deviceid=1644948d85879-00809ff45590d7-3e3d5f01-1049088-1644948d859ff; _ga=GA1.2.1035819392.1526269927; JSSearchModel=0; _jzqa=1.2335851547338655000.1526269928.1535704880.1535767657.15; _jzqx=1.1535442607.1535767657.4.jzqsr=sou%2Ezhaopin%2Ecom|jzqct=/.jzqsr=zhaopin%2Ecom|jzqct=/; LastSearchHistory=%7b%22Id%22%3a%22b1801444-bf65-4a81-9a72-229faebcd6a8%22%2c%22Name%22%3a%22python+%2b+%e6%b7%b1%e5%9c%b3%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d765%26kw%3dpython%26sm%3d0%26p%3d1%22%2c%22SaveTime%22%3a%22%5c%2fDate(1535767686578%2b0800)%5c%2f%22%7d; urlfrom2=121113803; adfcid2=pzzhubiaoti; ZP_OLD_FLAG=false; _jzqy=1.1530237852.1535767706.7.jzqsr=baidu|jzqct=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98.jzqsr=baidu|jzqct=zhilian; urlfrom=121113803; adfcid=pzzhubiaoti; adfbid=0; dywea=95841923.4215651220301152000.1526269927.1535772692.1535936715.28; dywec=95841923; dywez=95841923.1535936715.28.24.dywecsr=other|dyweccn=121113803|dywecmd=cnt|dywectr=%E6%99%BA%E8%81%94; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1535615914,1535682584,1535767705,1535936715; sts_sg=1; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fAhw9s0P7KI0KqiAsjjBckU00000FxNENb00000IK9arW.THLyktAJ0A3qmh7GuZNCUvd-gLKM0Znqrj7hmyF9n16snj0zPWb4u0Kd5Hnzf1bvn1nzrRDLwjDvrHc4fRm1fbnkrj7KrHTznjc10ADqI1YhUyPGujY1nHnzrjDdP1f1FMKzUvwGujYkP6K-5y9YIZ0lQzqLILT8Xh99ULKGUB4WUvYOTv-b5HDznHDkn16snzu1pgw-5gKlXh9dmh-9ULwG0APzm1Y1njRkPs%26tpl%3Dtpl_11535_17772_13457%26l%3D1505613207%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3132815743_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D83%26wd%3D%25E6%2599%25BA%25E8%2581%2594%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D1872; __xsptplus30=30.13.1535936715.1535936715.1%231%7Cother%7Ccnt%7C121113803%7C%7C%23%23U81g_UbYclcaARF8xWQDv3CFxW72aBek%23; __utma=269921210.1035819392.1526269927.1535772692.1535936715.35; __utmc=269921210; __utmz=269921210.1535936715.35.24.utmcsr=other|utmccn=121113803|utmcmd=cnt|utmctr=%E6%99%BA%E8%81%94; LastCity=%E6%B7%B1%E5%9C%B3; LastCity%5Fid=765; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1535938320; GUID=5e162a63eac346a29d16403d7a148a8a; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%2246201618-1d75-46c2-8ab5-987dae181bf6-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22//jobs%22:{%22actionid%22:%22a5d22e3a-81b9-4438-85b2-b26f533ada85-jobs%22%2C%22funczone%22:%22dtl_best_for_you%22}}',
        # 'Host': 'fe-api.zhaopin.com',
        # 'Origin': 'https://sou.zhaopin.com',
        # 'Referer': 'https://sou.zhaopin.com/?pageSize=60&jl=765&kw=python&kt=3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    url = 'https://sou.zhaopin.com/?pageSize=60&jl=765&kw=python&kt=3'
    response = requests.get(url, headers=header)

def get_page(page):
    header = {
        # 'Accept': 'application/json, text/plain, */*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Connection': 'keep-alive',
        'Cookie': 'adfbid2=0; sts_deviceid=1644948d85879-00809ff45590d7-3e3d5f01-1049088-1644948d859ff; _ga=GA1.2.1035819392.1526269927; JSSearchModel=0; _jzqa=1.2335851547338655000.1526269928.1535704880.1535767657.15; _jzqx=1.1535442607.1535767657.4.jzqsr=sou%2Ezhaopin%2Ecom|jzqct=/.jzqsr=zhaopin%2Ecom|jzqct=/; LastSearchHistory=%7b%22Id%22%3a%22b1801444-bf65-4a81-9a72-229faebcd6a8%22%2c%22Name%22%3a%22python+%2b+%e6%b7%b1%e5%9c%b3%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d765%26kw%3dpython%26sm%3d0%26p%3d1%22%2c%22SaveTime%22%3a%22%5c%2fDate(1535767686578%2b0800)%5c%2f%22%7d; urlfrom2=121113803; adfcid2=pzzhubiaoti; ZP_OLD_FLAG=false; _jzqy=1.1530237852.1535767706.7.jzqsr=baidu|jzqct=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98.jzqsr=baidu|jzqct=zhilian; urlfrom=121113803; adfcid=pzzhubiaoti; adfbid=0; dywea=95841923.4215651220301152000.1526269927.1535772692.1535936715.28; dywec=95841923; dywez=95841923.1535936715.28.24.dywecsr=other|dyweccn=121113803|dywecmd=cnt|dywectr=%E6%99%BA%E8%81%94; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1535615914,1535682584,1535767705,1535936715; sts_sg=1; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fAhw9s0P7KI0KqiAsjjBckU00000FxNENb00000IK9arW.THLyktAJ0A3qmh7GuZNCUvd-gLKM0Znqrj7hmyF9n16snj0zPWb4u0Kd5Hnzf1bvn1nzrRDLwjDvrHc4fRm1fbnkrj7KrHTznjc10ADqI1YhUyPGujY1nHnzrjDdP1f1FMKzUvwGujYkP6K-5y9YIZ0lQzqLILT8Xh99ULKGUB4WUvYOTv-b5HDznHDkn16snzu1pgw-5gKlXh9dmh-9ULwG0APzm1Y1njRkPs%26tpl%3Dtpl_11535_17772_13457%26l%3D1505613207%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3132815743_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D83%26wd%3D%25E6%2599%25BA%25E8%2581%2594%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D1872; __xsptplus30=30.13.1535936715.1535936715.1%231%7Cother%7Ccnt%7C121113803%7C%7C%23%23U81g_UbYclcaARF8xWQDv3CFxW72aBek%23; __utma=269921210.1035819392.1526269927.1535772692.1535936715.35; __utmc=269921210; __utmz=269921210.1535936715.35.24.utmcsr=other|utmccn=121113803|utmcmd=cnt|utmctr=%E6%99%BA%E8%81%94; LastCity=%E6%B7%B1%E5%9C%B3; LastCity%5Fid=765; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1535938320; GUID=5e162a63eac346a29d16403d7a148a8a; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%2246201618-1d75-46c2-8ab5-987dae181bf6-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22//jobs%22:{%22actionid%22:%22a5d22e3a-81b9-4438-85b2-b26f533ada85-jobs%22%2C%22funczone%22:%22dtl_best_for_you%22}}',
        # 'Host': 'fe-api.zhaopin.com',
        # 'Origin': 'https://sou.zhaopin.com',
        # 'Referer': 'https://sou.zhaopin.com/?pageSize=60&jl=765&kw=python&kt=3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    data = {
        'pageSize': 60,
        'cityId': 765,
        'workExperience': -1,
        'education': -1,
        'companyType': -1,
        'employmentType': -1,
        'jobWelfareTag': -1,
        'kw': 'python',
        'kt': 3,
        'lastUrlQuery': '{"pageSize":"60","jl":"765","kw":"python","kt":"3"}'
    }
    print('----------------第', page, '页----------------')
    # url = 'https://fe-api.zhaopin.com/c/i/sou/page-title?start='+str((60+)-60)+'&pageSize=60&cityId=765&areaId=&businessarea=%7B%7D&industry=&salary=&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&jobType=-1&sortType=&kw=python&kt=3&bj=&sj=&lastUrlQuery=%7B%22pageSize%22:%2260%22,%22jl%22:%22765%22,%22kw%22:%22python%22,%22kt%22:%223%22%7D'
    url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize='+str(page * 60)+'&cityId=765&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&lastUrlQuery=%7B%22pageSize%22:%2260%22,%22jl%22:%22765%22,%22kw%22:%22python%22,%22kt%22:%223%22%7D'
    response = requests.get(url, headers=header)
    #网页用Ajax渲染，故用response.json()进行转化为字典对象
    return response.json()

def parse(info):
    results = info['data']['results']
    for result in results:
        job = {
            'jobName': result['jobName'],
            'salary': result['salary'],
            'city': result['city']['display'],
            'company': result['company']['name'],
            'eduLevel': result['eduLevel']['name'],
            'emplType': result['emplType'],
            'workingExp': result['workingExp']['name']
        }
        save_to_mongo(job) #保存到数据库


if __name__ == '__main__':
    for i in range(1, 100):
        infomation = get_page(i)
        parse(infomation)