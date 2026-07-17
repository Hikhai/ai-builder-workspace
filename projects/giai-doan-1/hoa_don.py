import sys
def dinh_dang_tien(tien):
    return "{:,.0f}".format(tien).replace(",", ".") + " VNĐ"

try:
    so_luong_ly = int(input("Nhập số lượng ly: "))
    gia_ly = float(input("Nhập giá mỗi ly: "))
except ValueError:
    print("Vui lòng nhập số hợp lệ.")
    sys.exit()

tong_tien = so_luong_ly * gia_ly

if so_luong_ly >= 5:
    tong_tien *= 0.9
    print("Bạn được giảm giá 10% vì mua từ 5 ly trở lên.")
    print(f"Tổng tiền sau khi giảm giá: {dinh_dang_tien(tong_tien)}")
else:
    print(f"Tổng tiền: {dinh_dang_tien(tong_tien)}")