#  coding:utf-8

import requests

from bs4 import BeautifulSoup

__author__ = 'CHEN Zhao'


def get_soup(url):
    r = requests.get(url)
    return BeautifulSoup(r.text)


def main():
    resultf = file('conferences.txt', 'w')
    root_soup = get_soup('http://www.ccf.org.cn/sites/ccf/paiming.jsp')
    for category_a_tag in root_soup('table', align='left')[0]('a'):
        cate_name, cate_url = category_a_tag.text, category_a_tag['href']
        cate_soup = get_soup(cate_url)
        for ranking, table_soup in zip(['A', 'B', 'C'], cate_soup('table', width='850')[3:6]):
            for conf_tr in table_soup('tr')[1:]:
                idx, abbr, fullname = map(lambda x:' '.join(x.text.split()), conf_tr('td'))[:-2]
                web_url = conf_tr('td')[-1].a['href']
                resultf.write((','.join([cate_name, ranking, idx, abbr, fullname, web_url])+'\n').encode('utf-8'))


if __name__ == '__main__':
    main()
