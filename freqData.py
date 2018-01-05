import jieba.analyse
from collections import Counter
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def sort_freq_segments(infile,outfile):
    fin = open(infile,'r',encoding = 'utf-8')
    fout = open(outfile,'wb+')
    cleaned_comments = fin.read()
    #分词
    segment_words = jieba.lcut(cleaned_comments)
    #统计次频
    data = dict(Counter(segment_words))
    stopwords = [line.strip() for line in open('stopwords_chinese', encoding='utf8').readlines()]
    #去停用词
    new_data = { k:v for k,v in data.items() if k not in stopwords}
    #排序
    sorted_dic = sorted(new_data.items(),key=lambda d:d[1],reverse=True)
    for each_one in sorted_dic:
           fout.write((each_one[0]+' '+str(each_one[1]) + '\n').encode('utf8'))
    fin.close()
    fout.close()

def show_word(infile,num):
    fin = open(infile,'r',encoding = 'utf-8')
    cleaned_comments = fin.read()
    fin.close()
    LOCAL_STOPWORDS = set([line.strip() for line in open('stopwords_chinese', encoding='utf8').readlines()])
    #补充停用词
    NEW_STOPWORDS = STOPWORDS | LOCAL_STOPWORDS
    #分词
    wordlist_after_jieba = jieba.lcut(cleaned_comments)
    wl_space_split = " ".join(wordlist_after_jieba)
    #读入背景图片
    dog_mask = np.array(Image.open('dog.jpg'))
    wc = WordCloud(
        background_color='white', #设置背景颜色
        max_words = num,  #设置最多显示字数
        stopwords = NEW_STOPWORDS, #设置停用词
        font_path="/Users/duxiaojia/System/Library/Fonts/PingFang.ttc", #设置中文字体
        mask=dog_mask, #设置背景图片
        max_font_size=50, #设置字体最大值
        random_state=42)
    wc.generate(cleaned_comments)
    wc.to_file("dog01.jpg")
    plt.imshow(wc,interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    #sort_freq_segments('clean_data','sorted_segments')
    show_word('clean_data',100)
    #print (type(STOPWORDS))