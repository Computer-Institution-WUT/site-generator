# -*- coding: utf-8 -*-
import jinja2
from distutils.dir_util import copy_tree
import os
from markdown2 import Markdown


class SiteGenerator():
    def __init__(self):
        self.t_loader = jinja2.FileSystemLoader(searchpath='templates/')
        self.t_env = jinja2.Environment(loader=self.t_loader)

    def publish(self, name, content, location=None):
        if location:
            pass
        else:
            location = './'
        with open(location + name, 'wb') as f:
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
    
    def generate_post(self):
        _dir = './post_example/'
        for root, dirs, files in os.walk(_dir, topdown=False):
            for name in files:
                html_str = self.render_page(_dir + name)
                # print(html_str)
                t_name = 'article_content.html'
                t = self.t_env.get_template(t_name)
                s = t.render(title='Post1',
                             article={
                                 'title': name,
                                 'date': 'Oct. 31',
                                 'author': 'LYP',
                                 'content': html_str
                             })
                self.publish('post1.html', s, 'static_files/')
    
    def render_page(self, filename):
        md_text = b''
        md_converter = Markdown(extras=["fenced-code-blocks", "toc"])
        with open(filename, 'rb') as f:
            md_text = f.read()
            md_text = md_text.decode('utf8')
        html_str = md_converter.convert(md_text)
        return html_str

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
    s.generate_post()
