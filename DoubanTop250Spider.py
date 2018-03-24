#获取豆瓣电影Top250电影名称，将其排名和名称写入当前目录下的DoubanTop250.csv文件
import requests
import csv
import re

dick = list(range(250))

def get_rankDict():
    Movies = []
    
    for i in range(1,11):
        i = (i - 1) * 25
        html = requests.get('https://movie.douban.com/top250?start=%d&filter=' % i).content
        #匹配不以&开头的元素内容
        result = re.findall('<span class="title">([^\&].*)</span>', html.decode())
        Movies.extend(result)

    for i in range(0, 250):
        dick[i] = {'Rank':(i+1), 'MovieName':Movies[i]}

def write_csv():
    #csvfile = file('DoubanTop250.csv', 'wb')
    with open('DoubanTop250.csv', "w") as csvFile:
        fieldnames = ['Rank', 'MovieName']
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(dick)):
            writer.writerow(dick[i])

def main():
    get_rankDict()
    print("finish get_rankDict")
    write_csv()

if __name__ == '__main__':
    main()
