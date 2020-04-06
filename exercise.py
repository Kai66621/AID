"""
    Exercise01
"""
def dictionary(fb, word):
    for i in fb:
        if i.split(' ')[0] > word:
            return '未找到该单词'
        if i.split(' ')[0] == word:
            return ' '.join(i.split(' ')[1:]).lstrip()
    return '未找到该单词'
fb01 = open('dict.txt')
word01 = input('请输入查找单词：')
print(dictionary(fb01, word01))

"""
    Homework01
"""
# def copy_file(file_name):
#     file = open(file_name, 'rb')
#     name_list = file_name.split('.')
#     name_list.insert(-1, '_copy.')
#     copy_name = ''.join(name_list)
#     file_copy = open(copy_name, 'wb')
#     while True:
#         data = file.read(1024)
#         if not data:
#             break
#         file_copy.write(data)
# copy_file('img.jpg')

"""
    Homework02
"""
import time
def timer(file_str):
    count = data = 0
    file = open(file_str, 'a+')
    file.seek(data)
    for i in file:
        if not i:
            break
        data = i
    if data.split('.')[0].isdigit():
        count = int(data.split('.')[0])
    while True:
        count += 1
        t = time.localtime()
        file.write('\n%d.  %d-%d-%d  %d:%d:%d' % (count, t[0], t[1], t[2], t[3], t[4], t[5]))
        file.flush()
        time.sleep(1)
timer('material')