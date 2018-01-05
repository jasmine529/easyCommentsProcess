from urllib import request
from bs4 import BeautifulSoup as bs
import random
import time
import json

def get_movie_id():
    resp = request.urlopen('http://movie.douban.com/nowplaying/shanghai/')
    #获取当前上映影片网页的html
    html_data = resp.read().decode('utf-8')
    print(html_data)
    #解析html代码
    soup = bs(html_data,'html.parser')
    nowplaying_movie = soup.find_all('div',id = 'nowplaying')
    nowplaying_movie_list = nowplaying_movie[0].find_all('li',class_='list-item')
    nowplaying_list = []
    for item in nowplaying_movie_list:
        nowplaying_dict = {}
        nowplaying_dict['id']=item['data-subject']
        for tag_img_item in item.find_all('img'):
            nowplaying_dict['name'] = tag_img_item['alt']
            nowplaying_list.append(nowplaying_dict)
    print (nowplaying_list)





# 寻梦环游记 20495023
# 短评地址 http://movie.douban.com/subject/20495023/comments?start=0&limit=20
def get_comments(movie_id,page_num):
    comment_file = "origin_data"
    f = open(comment_file,'wb+')
    offset= 0
    for i in range(0,page_num):
        offset += 20*i
        req = request.Request('http://movie.douban.com/subject/'+ movie_id + '/comments'+'?'+'start='+str(offset)+'&limit=20')
        resp = request.urlopen(req)
        html_data = resp.read().decode('utf_8')
        soup = bs(html_data,'html.parser')
        comment_div_list = soup.find_all('div',class_= 'comment')
        print (comment_div_list)

        for item in comment_div_list:
            if item.find_all('p')[0].string is not None:
                f.write((item.find_all('p')[0].string).encode('utf8', 'ignore'))
        time.sleep(1)



    f.close()

if __name__ == '__main__':
    #get_movie_id()
    get_comments('20495023',5)




