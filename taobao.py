from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from bs4 import BeautifulSoup
import pymongo
from selenium.common.exceptions import TimeoutException

MONGO_URL='localhost'
MONGO_DB='Taobao'

KEYWORD='美食'
browser = webdriver.Chrome()#声明浏览器
wait = WebDriverWait(browser,10)#显式延时等待

client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]

def save_to_mongo(info):
    if db[KEYWORD].insert(info):
        print('保存成功',info)
    else:
        print('失败',info)

#进入首页，进行搜索
def get_search():
    url = 'https://www.taobao.com'#首页的url
    browser.get(url)#输入url
    try:
        # 查找搜索框的节点，判断搜索框是否已经加载好
        inputs = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#q')))
        #查找搜索按钮，判断是否已经具备点击功能
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
        inputs.send_keys(KEYWORD)#输入搜索的关键字
        button.click()#点击按钮
        # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager .wraper .inner.clearfix')))
        #判断页面是否已经加载好，并提取页码信息
        page=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total'))).text.strip()
        page = re.search('\d+',page).group()
        get_information(browser.page_source)#提取当前页的信息
        return int(page)
    except TimeoutException:
        print('get_search()出现TimeoutException')
        return get_search()

#获取当前页的商品信息
def get_information(html):
    soup = BeautifulSoup(html,'lxml')
    results=soup.select('#mainsrp-itemlist .items .item')#查找所有商品信息所在节点
    #提取信息
    for result in results:
        info={
            'price':result.select('.price strong')[0].string,#价格
            'deal-cnt':result.select('.deal-cnt')[0].string[:-3],#交易数量
            'title':result.select('.title a')[0].get_text().strip(),#商品的标题
            'shop':result.select('.shop a')[0].get_text().strip(),#商店名
            'location':result.select('.location')[0].string,#地理位置
            'img_url': result.select('.pic a img')[0].attrs['data-src']#图片链接
        }
        save_to_mongo(info)

def next_page(page):
    try:
        inputs = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.form > input')))#定位到页码的输入框
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div.form > span.btn.J_Submit')))#确定按钮
        inputs.clear()#清空
        inputs.send_keys(page)#输入页码
        button.click()#点击按钮
        #判断是否已经翻转到目标页，判断页码是否已经高亮
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.items li.item.active'),str(page)))
        get_information(browser.page_source)#获取当前页
    except TimeoutException:
        print('next_page()出现TimeoutException')
        next_page(page)

def main():
    pages=get_search()#进入淘宝首页，进行关键字的搜索，并返回总页数
    try:
        for page in range(2,pages+1):
            next_page(page)
    except Exception:
        print('出现异常：',str(Exception))
    finally:
        browser.close()

if __name__=='__main__':
    main()