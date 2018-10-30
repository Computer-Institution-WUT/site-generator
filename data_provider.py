from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Text
from sqlalchemy.ext.declarative import declarative_base
import logging
import hashlib
import datetime
SQLBase = declarative_base()


class SQLManager():
    def __init__(self):
        self.engine = create_engine('sqlite:///db/wutcs.db')
        self.DBSession = sessionmaker(bind=self.engine)

    def query(self, model):
        try:
            _session = self.DBSession()
            _results = _session.query(model).all()
        except Exception as e:
            logging.error('DB Query failed...')
            logging.error(str(e))
            _results = 'ERROR'
        finally:
            _session.close()
        return _results

    def add(self, model):
        try:
            _session = self.DBSession()
            _session.add(model)
            _session.commit()
        except Exception as e:
            logging.error('Add to DB failed...')
            logging.error(str(e))
        finally:
            _session.close()

    def delete(self, model, title):
        try:
            _session = self.DBSession()
            _session.query(model).filter(model.title == title).delete()
            _session.commit()
        except Exception as e:
            logging.error('Delete from DB failed...')
            logging.error(str(e))
        finally:
            _session.close()

    def update_news(self, model, name, data):
        _session = self.DBSession()
        sub = _session.query(model).filter(model.name == name).one()
        sub.value = data
        _session.commit()
        _session.close()


class NewsModel(SQLBase):
    __tablename__ = 'news'

    title = Column(Text(), primary_key=True, unique=True)
    date = Column(Text())
    content = Column(Text())
    link = Column(Text())


class ActModel(SQLBase):
    __tablename__ = 'act'

    title = Column(Text(), primary_key=True, unique=True)
    date = Column(Text())
    content = Column(Text())
    index = Column(Text())


class DataProvider():
    def __init__(self):
        self.sql_manager = SQLManager()

    def get_hash(self, data):
        if isinstance(data, str):
            data = data.encode()
        m = hashlib.md5()
        m.update(data)
        return m.hexdigest()

    def get_news(self):
        r = self.sql_manager.query(NewsModel)
        result_list = []
        for i in r:
            news_dic = {
                'title': i.title,
                'date': i.date,
                'content': i.content,
                'link': i.link
            }
            result_list.append(news_dic)
        return result_list

    def add_news(self, title, content, date=None):
        if date:
            _date_str = date
        else:
            _date_str = '@'.join(str(datetime.datetime.now()).split(' '))[:-7]
        _unique_link = self.get_hash(title + _date_str)
        _news_single = NewsModel(
            title=title,
            content=content,
            date=_date_str,
            link=_unique_link
        )
        self.sql_manager.add(_news_single)


if __name__ == '__main__':
    provider = DataProvider()
    print(provider.get_news())
