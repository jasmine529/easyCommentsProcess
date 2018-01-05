import re
import jieba

def remove_punctuations(infile,outfile):
    fin = open(infile,encoding='utf8')
    origin_data = fin.readlines()
    comments=''
    for each_line in origin_data:
        comments=comments+each_line.strip()
    #print (comments)
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern,comments)
    cleaned_comments = ''.join(filterdata)
    #print (cleaned_comments)
    fout = open(outfile, 'wb+')
    fout.write(cleaned_comments.encode('utf8', 'ignore'))
    fin.close()
    fout.close()

def segment_comments(infile,outfile):

    fin = open(infile,encoding='utf8')
    cleaned_comments = fin.read()
    segment = jieba.lcut(cleaned_comments)
    stopwords = [line.strip() for line in open('stopwords_chinese',encoding='utf8').readlines()]
    segment_nostopwords = set(segment) - set(stopwords)
    fout = open(outfile,'wb+')
    for each_item in segment_nostopwords:
        fout.write(each_item.encode('utf8')+'\n'.encode('utf8'))
    fin.close()
    fout.close()


if __name__ == '__main__':
    remove_punctuations('origin_data','clean_data')
    #segment_comments('clean_data','segments_set')
