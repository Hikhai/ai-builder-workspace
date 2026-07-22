from datetime import datetime

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class NhatKy(Base):
    __tablename__ = "nhat_ky"

    id: Mapped[int] = mapped_column(primary_key=True)
    ho_so_id: Mapped[int] = mapped_column(ForeignKey("ho_so.id"))
    moc_hoc_id: Mapped[int] = mapped_column(ForeignKey("moc_hoc.id"), nullable=True)

    ngay: Mapped[datetime] = mapped_column(default=datetime.now)
    tom_tat: Mapped[str] = mapped_column(Text)
    diem_manh: Mapped[str] = mapped_column(Text, nullable=True)
    diem_yeu: Mapped[str] = mapped_column(Text, nullable=True)
    dieu_chinh_lo_trinh: Mapped[str] = mapped_column(Text, nullable=True)

    ho_so: Mapped["HoSo"] = relationship(back_populates="nhat_ky")