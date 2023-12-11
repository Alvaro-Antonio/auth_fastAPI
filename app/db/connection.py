from decouple import config #ajuda importa variaveis de ambiente
from sqlalchemy import create_engine #criar sessões no banco
from sqlalchemy.orm import sessionmaker

DB_URL = config('DB_URL')

engine = create_engine(DB_URL, pool_pre_ping=True) # pool prepin faz teste de está funcinanco

Session =sessionmaker(bind=engine)