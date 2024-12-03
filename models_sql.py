# models.py

from sqlalchemy import Column, String, Integer, Float, ARRAY, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

from werkzeug.security import generate_password_hash, check_password_hash

# Déclarer la base pour les modèles SQLAlchemy
Base = declarative_base()

#DATABASE_URL = "postgresql://postgres:postgre@localhost/db_pco"
#engine = create_engine(DATABASE_URL)

# Assurer que la table existe (sans conflit)
#Base.metadata.create_all(engine)

# MODELE TABLE OFFRES_EXTRACT
class OffresExtract(Base):
    __tablename__ = 'offres_extract'

    id = Column(Integer, primary_key=True)
    id_offre = Column(String, primary_key=True)
    intitule = Column(String, nullable=False)
    description = Column(Text, nullable=True)

# MODELES DES TABLES DE MONITORING
class ImportSegmentContxt(Base):
    __tablename__ = 'table_monitoring_contxt'

    id = Column(Integer, primary_key=True)
    ref_user = Column(String)
    segment = Column(String)
    prediction_contxt = Column(Integer)
    feedback_user = Column(String)
    embedding = Column(ARRAY(Float))

class ImportSegmentComp(Base):
    __tablename__ = 'table_monitoring_comp'

    id = Column(Integer, primary_key=True)
    ref_user = Column(String)
    segment = Column(String)
    prediction = Column(Integer)
    feedback_user = Column(String)
    embedding = Column(ARRAY(Float))

# MODELE TABLE USERS
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(150), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)