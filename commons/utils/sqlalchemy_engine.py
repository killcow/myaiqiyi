from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:mysql@127.0.0.1/MovieSpider?charset=utf8')
DB_Session = sessionmaker(bind=engine)
db_session = DB_Session()
