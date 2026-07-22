from datetime import datetime

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class HoSo(Base):
    __tablename__ = "ho_so"

    id: Mapped[int] = mapped_column(primary_key=True)
    nguoi_dung_id: Mapped[int] = mapped_column(ForeignKey("nguoi_dung.id"))

    trinh_do: Mapped[str] = mapped_column(String(50))
    muc_tieu: Mapped[str] = mapped_column(Text)
    ly_do_hoc: Mapped[str] = mapped_column(Text, nullable=True)
    thoi_gian_ranh_phut: Mapped[int] = mapped_column()
    cach_hoc_ua_thich: Mapped[str] = mapped_column(Text)

    ngay_tao: Mapped[datetime] = mapped_column(default=datetime.now)
    ngay_cap_nhat: Mapped[datetime] = mapped_column(
        default=datetime.now, onupdate=datetime.now
    )

    nguoi_dung: Mapped["NguoiDung"] = relationship(back_populates="ho_so")
    lo_trinh: Mapped[list["MocHoc"]] = relationship(
        back_populates="ho_so", order_by="MocHoc.thu_tu"
    )
    nhat_ky: Mapped[list["NhatKy"]] = relationship(back_populates="ho_so")