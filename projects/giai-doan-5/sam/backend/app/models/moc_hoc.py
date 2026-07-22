from datetime import datetime
from enum import Enum

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class TrangThaiMoc(str, Enum):
    CHUA_BAT_DAU = "Chưa bắt đầu"
    DANG_HOC = "Đang học"
    HOAN_THANH = "Hoàn thành"


class MocHoc(Base):
    __tablename__ = "moc_hoc"

    id: Mapped[int] = mapped_column(primary_key=True)
    ho_so_id: Mapped[int] = mapped_column(ForeignKey("ho_so.id"))

    thu_tu: Mapped[int] = mapped_column()
    tieu_de: Mapped[str] = mapped_column(String(200))
    mo_ta: Mapped[str] = mapped_column(Text)
    trang_thai: Mapped[TrangThaiMoc] = mapped_column(default=TrangThaiMoc.CHUA_BAT_DAU)

    ngay_bat_dau: Mapped[datetime] = mapped_column(nullable=True)
    ngay_hoan_thanh: Mapped[datetime] = mapped_column(nullable=True)

    ho_so: Mapped["HoSo"] = relationship(back_populates="lo_trinh")