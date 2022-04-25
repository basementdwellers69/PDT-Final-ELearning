from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('mysql+mysqldb://root:@localhost/pdt')
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))
def init_db():
    metadata.create_all(bind=engine)