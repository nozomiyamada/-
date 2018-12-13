import re  # for 1.4)
import collections  # for 2)
import pkuseg  # for 2)
import thulac # for 3)


# 1.1) split the text into 3 pieces
def split_text():
    """
    open the 'Dream of Red Mansion' and split
    search the word '第一回', '第四十回', ...

    split_text('红楼梦.txt')
    >> part1.txt, part2.txt, part3.txt will be output
    """

    open_file = open('红楼梦.txt', 'r', encoding='utf-8')  # open file in read mode
    part1_file = open('part1.txt', 'w', encoding='utf-8')  # make part1.txt in write mode
    part2_file = open('part2.txt', 'w', encoding='utf-8')  # make part2.txt in write mode
    part3_file = open('part3.txt', 'w', encoding='utf-8')  # make part3.txt in write mode

    text = open_file.read()  # read all text

    part1_start_index = text.find('第一回')  # search the start of 第一回
    part2_start_index = text.find('第四十一回')
    part3_start_index = text.find('第八十一回')

    part1_file.write(text[part1_start_index: part2_start_index])
    part2_file.write(text[part2_start_index: part3_start_index])
    part3_file.write(text[part3_start_index:])

    open_file.close()
    part1_file.close()
    part2_file.close()
    part3_file.close()


# 1.2) count adverbs in 3 documents
def count_adverb():
    """
    count 越发、难道、可巧、不曾、原是
    make local function 'count_from_one_file' in advance
    count them in each document by using local function 3 times and print

    count_adverb() # no argument
    >>
    part1.txt
    [('越发', 72), ('难道', 87), ('可巧', 47), ('不曾', 51), ('原是', 51)]
    part2.txt
    [('越发', 88), ('难道', 68), ('可巧', 40), ('不曾', 52), ('原是', 78)]
    part3.txt
    [('越发', 38), ('难道', 33), ('可巧', 1), ('不曾', 14), ('原是', 45)]
    """

    # local function for count adverb in one file
    def count_from_one_file(file_name):
        open_file = open(file_name, 'r', encoding='utf-8')
        text = open_file.read()
        adverbs = ['越发', '难道', '可巧', '不曾', '原是']  # list of adverbs
        count_list = []  # initialize list
        for adverb in adverbs:
            number = text.count(adverb)  # count the each adverb
            count_list.append((adverb, number))  # make tuple (word, number) and append to list
        open_file.close()
        return str(count_list)
    
    write_file = open('result.txt', 'a', encoding='utf-8')
    write_file.write('1.2)'+'\n')
    write_file.write('part1'+'\n')
    write_file.write(count_from_one_file('part1.txt')+'\n')
    write_file.write('part2'+'\n')
    write_file.write(count_from_one_file('part2.txt')+'\n')
    write_file.write('part3'+'\n')
    write_file.write(count_from_one_file('part3.txt')+'\n')
    write_file.close()


# 1.3) count function words in 3 documents and calculate frequency
def count_function_word():
    """
    count 或、亦、方、即、皆、仍、故、尚、呀、吗、咧、罢、么、呢、让、向、往、就、但、 越、再、更、很、偏
    make local function 'count_from_one_file' in advance
    1. count all 汉字 but not count symbol > use variable 'count_all_letter'
    2. count ( 汉字 and function word ) > use variable 'count function word'
    count them in each document by using local function 3 times and print

    count_function_word() # no argument
    >>
    part1
    频率: 2.75%
    part2
    频率: 2.49%
    part3
    频率: 2.66%
    """

    # local function for count function word in one file
    def count_from_one_file(file_name):
        open_file = open(file_name, 'r', encoding='utf-8')
        text = open_file.read()
        words = ['或', '亦', '方', '即', '皆', '仍', '故', '尚', '呀', '吗', '咧', '罢', '么',
                 '呢', '让', '向', '往', '就', '但', '越', '再', '更', '很', '偏']
        count_all_letter = 0  # counter for all 汉字
        count_function_word = 0  # counter for functional word
        for letter in text:  # for loop each letter
            if letter.isalpha() == True:  # if and only if the letter is 汉字 (not count symbol)
                count_all_letter += 1
                if letter in words:  # if the letter is 汉字 and functional word
                    count_function_word += 1
        open_file.close()
        return str('频率: {}%'.format(round(count_function_word * 100 / count_all_letter, 2)))  # calculate

    write_file = open('result.txt', 'a', encoding='utf-8')
    write_file.write('\n'+'1.3)'+'\n')
    write_file.write('part1'+'\n')
    write_file.write(count_from_one_file('part1.txt')+'\n')
    write_file.write('part2'+'\n')
    write_file.write(count_from_one_file('part2.txt')+'\n')
    write_file.write('part3'+'\n')
    write_file.write(count_from_one_file('part3.txt')+'\n')
    write_file.close()


# 1.4) count average paragraph and sentence length
def average_length():
    """
    count length of both paragraph and sentence and calculate average
    1. list of paragraphs: split text with '\n'
    2. list of sentences: split text with '．' '。' or '\n' (must use regular expression)
    3. count length of each element in list by using len()
        and make new list that contains only int
        e.g. ['你好', '我爱你',...] > [2, 3,...]
        at the same time, strip white space ' ' in head (or tail) of the sentence
    4. calculate average: (sum of the integers in the list) / (length of the list)

    average_length() # no argument
    >>
    part1
    平均段落长度: 235.26
    平均句子长度: 26.34
    part2
    平均段落长度: 343.24
    平均句子长度: 25.84
    part3
    平均段落长度: 420.65
    平均句子长度: 26.57
    """

    # local function for count average length in one file
    def count_from_one_file(file_name):
        open_file = open(file_name, 'r')
        text = open_file.read()
        paragraph_list = text.splitlines()
        sentence_list = re.split('[．。\n]', text)
        paragraph_length = [len(paragraph.strip(' ')) for paragraph in paragraph_list]
        sentence_length = [len(sentence.strip(' ')) for sentence in sentence_list]
        average_paragraph = sum(paragraph_length) / len(paragraph_length)
        average_sentence = sum(sentence_length) / len(sentence_length)
        open_file.close()
        result1 = str('平均段落长度: {}'.format(round(average_paragraph, 2)))
        result2 = str('平均句子长度: {}'.format(round(average_sentence, 2)))
        return result1 + '\n' + result2

    write_file = open('result.txt', 'a', encoding='utf-8')
    write_file.write('\n'+'1.4)'+'\n')
    write_file.write('part1'+'\n')
    write_file.write(count_from_one_file('part1.txt')+'\n')
    write_file.write('part2'+'\n')
    write_file.write(count_from_one_file('part2.txt')+'\n')
    write_file.write('part3'+'\n')
    write_file.write(count_from_one_file('part3.txt')+'\n')
    write_file.close()


# 2) segmentation & 2-gram (=word pair)
def word_pair():
    """
    count top 100 frequent word pair
    1. segmentation with toolkit pkuseg (method .cut())
    2. make counter for word pair (must import collections)
    3. counter +1 if and only if both the two words are 汉字
    4. print top 100 word pair

    word_pair()
    >>
    part1.txt
    [(('笑', '道'), 837), (('袭', '人'), 371), (('听', '了'), 326)...]
    part2.txt
    [(('笑', '道'), 1089), (('了', '一'), 416), (('听', '了'), 397)...]
    part3.txt
    [(('了', '一'), 373), (('袭', '人'), 356), (('黛', '玉'), 283)...]
    """
    number_of_pair = 100  # search how many frequent pairs
    seg = pkuseg.pkuseg()  # segmentation processor

    # local function for count average length in one file
    def count_from_one_file(file_name):
        open_file = open(file_name, 'r')
        text = open_file.read()
        word_list = seg.cut(text)  # segmentation (make word list)
        pair_counter = collections.Counter()  # make counter for tuple
        for i, word in enumerate(word_list):
            if word[0].isalpha() and word_list[i + 1][0].isalpha():  # iff two words begin with 汉字
                pair_counter[(word, word_list[i + 1])] += 1  # count occurrence
        return str(pair_counter.most_common(number_of_pair))  # print top 100

    write_file = open('result.txt', 'a', encoding='utf-8')
    write_file.write('\n'+'2)'+'\n')
    write_file.write('part1'+'\n')
    write_file.write(count_from_one_file('part1.txt')+'\n')
    write_file.write('part2'+'\n')
    write_file.write(count_from_one_file('part2.txt')+'\n')
    write_file.write('part3'+'\n')
    write_file.write(count_from_one_file('part3.txt')+'\n')
    write_file.close()
    
    
# 3)
    
def pos_count():
    """
    count the number of major 6 pos and calculate frequency:
    the number of pos / the number of total words 
    """
    def count_from_one_file(file_name):
        open_file = open(file_name, 'r')
        text = open_file.read()
        tagger = thulac.thulac()
        word_list = tagger.cut(text)
        pos_counter = collections.Counter()
        word_counter = 0
        for word in word_list:
            if word[0][0].isalpha():
                pos_counter[word[1]] += 1
                word_counter += 1
            
        v = str('动词: {}%'.format(round(pos_counter['v']*100/word_counter, 2)))
        n = str('名词: {}%'.format(round(pos_counter['n']*100/word_counter, 2)))
        d = str('副词: {}%'.format(round(pos_counter['d']*100/word_counter, 2)))
        u = str('助词: {}%'.format(round(pos_counter['u']*100/word_counter, 2)))
        r = str('代词: {}%'.format(round(pos_counter['r']*100/word_counter, 2)))
        a = str('形容词: {}%'.format(round(pos_counter['a']*100/word_counter, 2)))
        open_file.close()
        return v + '\n' + n + '\n' + d + '\n' + u + '\n' + r + '\n' + a
        
    write_file = open('result.txt', 'a', encoding='utf-8')
    write_file.write('\n'+'3)'+'\n')
    write_file.write('part1'+'\n')
    write_file.write(count_from_one_file('part1.txt')+'\n')
    write_file.write('part2'+'\n')
    write_file.write(count_from_one_file('part2.txt')+'\n')
    write_file.write('part3'+'\n')
    write_file.write(count_from_one_file('part3.txt')+'\n')
    write_file.close()
    
def make_result():
    count_adverb()
    count_function_word()
    average_length()
    word_pair()
    pos_count()
    