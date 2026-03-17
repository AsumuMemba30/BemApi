from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#defir l url de connexion a MariaDB
#mysql://utilisateur:mot_de_passe@hote:port/nom_de_la_base
SQLACHEMY_URL_DATABASE = "mysql://root:@localhost:3306/bemtech"
#creation du moteur sql
engine = create_engine(SQLACHEMY_URL_DATABASE)
#creer une session local pour effectuer des requettes
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#classe de base pour nos modeles alchemy
Base = declarative_base()
#dependences poir recuperer la base de donnees dans nos routes fastapi
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()