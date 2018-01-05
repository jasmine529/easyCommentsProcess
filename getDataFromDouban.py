from bs4 import BeautifulSoup as bs
import time,requests,random

#先登录下，记下cookie
raw_cookies = 'bid=_m3FKY-Rn34; ll="108296"; ps=y; dbcl2="151695710:U3rTgS8gRAE"; ck=YJnP; push_noty_num=0; push_doumail_num=0'
raw_cookies_02 = 'bid=_m3FKY-Rn34; ll="108296"; ps=y; push_noty_num=0; push_doumail_num=0; dbcl2="79379623:ZDvFYcoy0EM"; ck=ouiZ'
cookies = {}
for line in raw_cookies.split(';'):
    key,value = line.split('=',1)
    cookies[key]=value

header = dict()
header['Accept'] = '*/*'
header['Accept-Encoding'] = 'gzip, deflate, br'
header['Accept-Language'] = 'zh-CN,zh;q=0.9,en;q=0.8'
header['Connection'] = 'keep-alive'
header['Host'] = 'movie.douban.com'
header['Referer'] = 'https://www.douban.com/accounts/login?source=movie'
header['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'


def get_comments(movie_id, page_num, start_page,comment_file='origin_data_more2'):
    if (start_page!=0):
        f= open(comment_file,'ab+')
    else:
        f = open(comment_file, 'wb+')
    offset = start_page*20
    m=start_page
    for i in range(0, page_num):
        offset += 20 * i
        url = 'http://movie.douban.com/subject/' + str(movie_id) + '/comments' + '?' + 'start=' + str(
            offset) + '&limit=20'
        response = requests.get(url,timeout=20,headers = header,cookies=cookies)
        data = response.text
        print(response.status_code)
        #使用beautifulsoap来解析网页
        soup = bs(data, 'html.parser')
        comment_div_list = soup.find_all('div', class_='comment')
        print ('page page page page %s' % (start_page+i))
        print (len(comment_div_list))
        for item in comment_div_list:
             if item.find_all('p')[0].string is not None:
                 f.write((item.find_all('p')[0].string).encode('utf8', 'ignore'))
        time.sleep(random.random())
    f.close()


if __name__ == '__main__':
    # get_movie_id()
    #get_comments('20495023', 10, 0)

    for i in range(10):
        page_start= i * 5
        get_comments('20495023', 5, page_start)
        time.sleep(10)


