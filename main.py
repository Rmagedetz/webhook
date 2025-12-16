import datetime
from fastapi import FastAPI, Request
from sqlalchemy import (Column, Integer, String, Date, create_engine, Text)
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError
from contextlib import contextmanager

app = FastAPI()

db_user = 'forms_inserter'
db_password = 'Vttnthrnvtm_T'
db_host = '91.193.182.16'
db_port = "3310"
db_name = 'g_db_3'

sql_connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(sql_connection_string)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Ankets(Base):
    __tablename__ = 'ankets'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=True, default="")
    name = Column(String(50), nullable=False)
    child_birthday = Column(Date, nullable=True, default=None)
    parent_main_name = Column(String(50), nullable=False)
    parent_main_phone = Column(String(50), nullable=False)
    parent_add = Column(Text, nullable=True, default="")
    phone_add = Column(String(20), nullable=True, default="")
    leave = Column(String(10), nullable=True, default="")
    additional_contact = Column(Text, nullable=True, default="")
    addr = Column(String(200), nullable=True, default="")
    disease = Column(Text, nullable=True, default="")
    allergy = Column(Text, nullable=True, default="")
    other = Column(Text, nullable=True, default="")
    physic = Column(Text, nullable=True, default="")
    swimm = Column(String(10), nullable=True, default="")
    jacket_swimm = Column(String(10), nullable=True, default="")
    hobby = Column(Text, nullable=True, default="")
    school = Column(String(100), nullable=True, default="")
    additional_info = Column(Text, nullable=True, default="")
    departures = Column(String(10), nullable=True, default="")
    referer = Column(String(300), nullable=True, default="")
    ok = Column(String(10), nullable=True, default="")
    mailing = Column(Text, nullable=True, default="")
    personal_accept = Column(String(10), nullable=True, default="")
    oms = Column(Text, nullable=True, default="")

    @classmethod
    def add_object(cls, **parameters):
        with session_scope() as session:
            add = cls(**parameters)
            session.add(add)


Base.metadata.create_all(bind=engine)


@contextmanager
def session_scope():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except IntegrityError:
        db.rollback()
        raise
    finally:
        db.close()


@app.post("/tilda-webhook")
async def tilda_webhook(request: Request):
    try:
        form_data = await request.form()
        data = dict(form_data)
        print("Получены данные формы (form-data):", data)
        return {"status": "ok", "source": "form"}
    except Exception:
        json_data = await request.json()
        Ankets.add_object(name='',
                          parent_main_name='',
                          parent_main_phone='')

        # Ankets.add_object(
        #     email=json_data.get('email', ''),
        #     name=json_data.get('name', ''),
        #     child_birthday=(
        #         datetime.datetime.strptime(json_data['dob'], "%d.%m.%Y").date()
        #         if json_data.get('dob') else None
        #     ),
        #     parent_main_name=json_data.get('custom_roditel', ''),
        #     parent_main_phone=json_data.get('custom_telefon', ''),
        #     parent_add='',
        #     phone_add=json_data.get('custom_dopolnitelnyytelefon_2', ''),
        #     leave='',
        #     additional_contact='',
        #     addr=json_data.get('custom_adresprozhivaniya', ''),
        #     disease=json_data.get('custom_disease', ''),
        #     allergy=json_data.get('custom_allergy', ''),
        #     other=json_data.get('custom_other', ''),
        #     physic=json_data.get('custom_physical', ''),
        #     swimm=json_data.get('custom_swimming', ''),
        #     jacket_swimm=json_data.get('custom_jacket_swimm', ''),
        #     hobby='',
        #     school=json_data.get('school', ''),
        #     additional_info=json_data.get('custom_dop', ''),
        #     departures='',
        #     referer=json_data.get('custom_gorodok', ''),
        #     ok='',
        #     mailing=json_data.get('rassylka', ''),
        #     personal_accept=json_data.get('personal-data', ''),
        #     oms=json_data.get('custom_polis', ''),
        # )
        print("Получены данные формы (JSON):", json_data)
        return {"status": "ok", "source": "json"}