import sys
def nhap_du_lieu():
    try:
        loai_do_uong = input("Nhập loại đồ uống (Cà phê, Trà, Nước ép): ")
        so_luong_ly = int(input("Nhập số lượng ly: "))
        gia_ly = float(input("Nhập giá mỗi ly: "))
        return loai_do_uong, so_luong_ly, gia_ly
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")
        sys.exit()

def tinh_tong_tien(so_luong_ly, gia_ly):
    tong_tien = so_luong_ly * gia_ly
    giam_gia = so_luong_ly >= 5
    return tong_tien, giam_gia

def in_ket_qua(loai_do_uong, so_luong_ly, tong_tien, giam_gia):
    if giam_gia:
        tong_tien *= 0.9
        print("Bạn được giảm giá 10% vì mua từ 5 ly trở lên.")
    print(f"hoa don: {loai_do_uong} - Số lượng: {so_luong_ly} - Tổng tiền: {dinh_dang_tien(tong_tien)}")

def dinh_dang_tien(tien):
    return "{:,.0f}".format(tien).replace(",", ".") + " VNĐ"


loai_do_uong, so_luong_ly, gia_ly = nhap_du_lieu()
tong_tien, giam_gia = tinh_tong_tien(so_luong_ly, gia_ly)
in_ket_qua(loai_do_uong, so_luong_ly, tong_tien, giam_gia)
