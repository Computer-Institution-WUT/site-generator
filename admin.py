from flask import Flask, render_template, request
from data_provider import DataProvider
from generator import SiteGenerator
import psutil
import logging


provider = DataProvider()
generator = SiteGenerator()
app = Flask(__name__)


@app.route('/')
def serve_main_page():
    server_status = {
        'cpu': str(psutil.cpu_percent()),
        'memory': [str(psutil.virtual_memory()[1] / 1024 ** 2)[:6], str(psutil.virtual_memory()[0] / 1024 ** 2)[:6]],
        'disk': [str(psutil.disk_usage('/')[2] / 1024 ** 3)[:6], str(psutil.disk_usage('/')[0] / 1024 ** 3)[:6]],
        'ip': '***',
        'os': 'Ubuntu 18.04 x64'
    }
    site_status = {
        'today': '0',
        'hour': '0'
    }
    return render_template(
        'admin.html',
        server=server_status,
        site=site_status
    )


@app.route('/news', methods=['POST'])
def serve_news_request():
    try:
        _title = request.form['title']
        _content = request.form['content']
        provider.add_news(_title, _content)
        return '0'
    except Exception as e:
        logging.error(str(e))
        return '1'


@app.route('/act', methods=['POST'])
def serve_act_request():
    try:
        _title = request.form['title']
        _date = request.form['date']
        _content = request.form['content']
        provider.add_act(_title, _content, _date)
        return '0'
    except Exception as e:
        logging.error(str(e))
        return '1'


@app.route('/action', methods=['POST'])
def serve_action_request():
    try:
        _action = request.form['action']
        if _action == 'index':
            post = {
                'title': 'test',
                'date': 'Oct. 29',
                'intro': 'this is a test post',
                'link': '#'
            }
            knowledge_dic = {
                'C': '',
                'C++': '',
                'Python': '',
                'Linux': ''
            }
            news = provider.get_news()[-1]
            act = provider.get_act()
            generator.generate_index(post, act, knowledge_dic, news)
        return '0'
    except Exception as e:
        logging.error(str(e))
        return '1'


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=8081)
