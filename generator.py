# -*- coding: utf-8 -*-
import jinja2
from distutils.dir_util import copy_tree


class SiteGenerator():
    def __init__(self):
        self.t_loader = jinja2.FileSystemLoader(searchpath='templates/')
        self.t_env = jinja2.Environment(loader=self.t_loader)

    def publish(self, name, content):
        with open('/var/www/html/' + name, 'wb') as f:
            f.write(content.encode('utf8'))

    def generate_index(self, post, act, knowledge_dic, news):
        t_name = 'index.html'
        t = self.t_env.get_template(t_name)
        s = t.render(title='WUTCS',
                     post=post,
                     act=act,
                     knowledge_dic=knowledge_dic,
                     news=news)
        self.publish('index.html', s)

    def full_generate(self):
        post = {
            'title': 'test',
            'date': 'Oct. 29',
            'intro': 'this is a test post',
            'link': '#'
        }
        act = {
            'title': '义务维修',
            'date': '日期未定',
            'content': '地点： 南湖食堂门口'
        }
        knowledge_dic = {
            'C': '',
            'C++': '',
            'Python': '',
            'Linux': ''
        }
        news = {
            'title': 'test_news',
            'date': 'Oct. 29',
            'content': 'this is a test news',
            'link': '#'
        }
        t_name = 'index.html'
        t = self.t_env.get_template(t_name)
        s = t.render(title='WUTCS',
                     post=post,
                     act=act,
                     knowledge_dic=knowledge_dic,
                     news=news)
        self.publish('index.html', s)

        t_name = 'about.html'
        t = self.t_env.get_template(t_name)
        s = t.render(title='关于')
        self.publish('about.html', s)


if __name__ == '__main__':
    s = SiteGenerator()
    s.full_generate()
