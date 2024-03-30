from utils.db_api.models import FileChunk, FileRepository, User
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from data.config import engine, Base

chunk_size = 262144
FILE_SIZE = 5242880


def create_file_chunk(image: bytes, file_uuid: str):
    session = sessionmaker(bind=engine)()
    try:
        current_chunk = 0
        done_reading = False
        while not done_reading:
            bfr = image[current_chunk * chunk_size: (current_chunk + 1) * chunk_size]
            if not bfr:
                done_reading = True
                break
            result = FileChunk(file_id=file_uuid, chunk=bytearray(bfr))
            session.add(result)
            session.commit()
            session.refresh(result)
            current_chunk += 1
    except Exception as e:
        return e
    finally:
        session.close()


def create_file(**kwargs):
    session = sessionmaker(bind=engine)()
    try:
        print(kwargs['contract_type'])
        print(kwargs)
        result = FileRepository(**kwargs)
        session.add(result)
        session.commit()
        session.refresh(result)
        session.close()
        return result.file_id
    except Exception as e:
        return e
    finally:
        session.close()
        print('file yaratildi!!!')


def create_user_info(**kwargs):
    session = sessionmaker(bind=engine)()
    try:
        print(kwargs)
        print('-----------------------123132312231')
        result = User(**kwargs)
        session.add(result)
        print(result)
        session.commit()
        session.refresh(result)
        session.close()
        return result.user_id
    except Exception as e:
        return e
    finally:
        session.close()


def get_user_info(user_id: str):
    session = sessionmaker(bind=engine)()
    try:
        result = session.query(User).filter_by(user_id=user_id).first()
        session.close()
        return result
    except Exception as e:
        return e
    finally:
        session.close()


def get_user_by_id(telegram_id: str):
    session = sessionmaker(bind=engine)()
    try:
        result = session.query(User).filter_by(telegram_id=telegram_id).first()
        session.close()
        return result
    except Exception as e:
        return e
    finally:
        session.close()


def get_file(file_uuid: str, path_: str):
    session = sessionmaker(bind=engine)()
    try:
        result = session.query(FileChunk).filter_by(file_id=file_uuid).all()
        session.close()
        return result
    except IntegrityError:
        return "Malumot topilmadi!"
    finally:
        session.close()


def get_files(user_id: int):
    session = sessionmaker(bind=engine)()
    try:
        result = session.query(FileRepository).filter_by(user_id=user_id).all()
        session.close()
        return result
    except Exception as e:
        return e


def get_file_(file_uuid: str):
    session = sessionmaker(bind=engine)()
    try:
        result = session.query(FileRepository).filter_by(file_id=file_uuid).first()
        session.close()
        return result
    except Exception as e:
        return e
    finally:
        session.close()
