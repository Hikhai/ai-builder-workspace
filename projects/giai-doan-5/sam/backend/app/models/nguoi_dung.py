from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class NguoiDung(Base):
    __tablename__ = "nguoi_dung"

    id: Mapped[int] = mapped_column(primary_key=True)
    ten: Mapped[str] = mapped_column(String(100))
    ngay_tao: Mapped[datetime] = mapped_column(default=datetime.now)

    ho_so: Mapped["HoSo"] = relationship(back_populates="nguoi_dung", uselist=False)