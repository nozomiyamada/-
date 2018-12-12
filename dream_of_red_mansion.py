# 1.1) split the text into 3 pieces
def split_text(file_name):
    """
    open the 'Dream of Red Mansion' and split
    search the word '第一回', '第四十回', ...

    split_text('dream_of_red_mansion.txt')
    >> part1.txt, part2.txt, part3.txt will be output
    """

    open_file = open(file_name, 'r')  # open file in read mode
    part1_file = open('part1.txt', 'w')  # make part1.txt in write mode
    part2_file = open('part2.txt', 'w')  # make part1.txt in write mode
    part3_file = open('part3.txt', 'w')  # make part1.txt in write mode

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

    count_adverb()
    >>
    """

    # local function for count adverb only in one file
    def count_from_one_file(file_name):
        open_file = open(file_name, 'r')
        text = open_file.read()
        adverbs = ['越发', '难道', '可巧', '不曾', '原是']  # list of adverbs
        count_list = []  # initialize list
        for adverb in adverbs:
            number = text.count(adverb)  # count the each adverb
            count_list.append((adverb, number))  # make tuple (word, number) and append to list
        open_file.close()
        print(file_name)
        print(count_list)

    count_from_one_file('part1.txt')
    count_from_one_file('part2.txt')
    count_from_one_file('part3.txt')