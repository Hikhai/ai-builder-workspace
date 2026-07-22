from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


class Base(DeclarativeBase):
    pass


DUONG_DAN_DB = "sqlite:///./sam.db"

engine = create_engine(DUONG_DAN_DB, echo=True)
SessionLocal = sessionmaker(bind=engine)


def khoi_tao_db():
    # Import ở đây (không phải đầu file) để đảm bảo mọi model đã đăng ký
    # với Base trước khi tạo bảng - tránh lỗi "table not found"
    from app.models import nguoi_dung, ho_so, moc_hoc, nhat_ky  # noqa: F401

    Base.metadata.create_all(engine)