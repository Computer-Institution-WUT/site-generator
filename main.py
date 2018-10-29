# -*- coding: utf-8 -*-
import jinja2


t_loader = jinja2.FileSystemLoader(searchpath='templates/')
t_env = jinja2.Environment(loader=t_loader)


def publish(name, content):
    with open('release/' + name, 'wb') as f:
        f.write(content.encode('utf8'))


def render_index():
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
    t = t_env.get_template(t_name)
    s = t.render(title='WUTCS',
                 post=post,
                 act=act,
                 knowledge_dic=knowledge_dic,
                 news=news)
    publish('index.html', s)


def main():
    render_index()


if __name__ == '__main__':
    main()
