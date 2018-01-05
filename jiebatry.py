import jieba
import jieba.analyse
import jieba.posseg as pseg

def get_topK(infile,topK):
    with open(infile,'r',encoding='utf-8') as f:
        comments = f.read()
        topK_list = jieba.analyse.extract_tags(comments,topK=topK)
    return topK_list

def get_a_set(infile):
    with open(infile,'r',encoding='utf-8') as f:
        comments = f.read()
        words = pseg.cut(comments)
        a_set = set(w.word for w in words if w.flag == 'a' )
        return a_set

def dif_mode():
    text = '我来到北京清华大学'
    default_mode = jieba.cut(text)
    full_mode = jieba.cut(text, cut_all=True)
    search_mode = jieba.cut_for_search(text)
    print ("精确模式:", "/".join(default_mode))
    print ("全模式:", "/".join(full_mode))
    print ("搜索引擎模式:", "/".join(search_mode))

if __name__ == '__main__':
    #print (get_topK('clean_data',20))
    print (get_a_set('clean_data'))
    #dif_mode()