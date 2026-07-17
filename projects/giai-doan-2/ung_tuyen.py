import csv
import os

THU_MUC_HIEN_TAI = os.path.dirname(os.path.abspath(__file__))
TEN_FILE = os.path.join(THU_MUC_HIEN_TAI, "ung_tuyen.csv")
CAC_COT = ["ten_cong_ty", "link", "muc_luong", "trang_thai"]
TRANG_THAI_HOP_LE = ["Đã nộp", "Đang chờ", "Đã PV", "Đậu", "Rớt"]

def nhap_khong_rong(nhan):
    while True:
        gia_tri = input(nhan)
        if gia_tri.strip() == "":
            print("Không được để trống. Vui lòng nhập lại.")
            continue
        return gia_tri

def nhap_luong():
    while True:
        gia_tri = input("Nhập mức lương: ")
        try:
            luong = float(gia_tri)
        except ValueError:
            print("Lương phải là số. Vui lòng nhập lại.")
            continue
        if luong < 0:
            print("Lương không được âm. Vui lòng nhập lại.")
            continue
        return gia_tri

def nhap_trang_thai():
    while True:
        gia_tri = input(f"Nhập trạng thái ({'/'.join(TRANG_THAI_HOP_LE)}): ")
        if gia_tri not in TRANG_THAI_HOP_LE:
            print("Trạng thái không hợp lệ. Vui lòng nhập lại.")
            continue
        return gia_tri

def them_moi(danh_sach):
    ten_cong_ty = nhap_khong_rong("Nhập tên công ty: ")
    link = nhap_khong_rong("Nhập link bài tuyển dụng: ")
    muc_luong = nhap_luong()
    trang_thai = nhap_trang_thai()
    danh_sach.append({
        "ten_cong_ty": ten_cong_ty,
        "link": link,
        "muc_luong": muc_luong,
        "trang_thai": trang_thai,
    })
    ghi_du_lieu(danh_sach)
    print("Đã thêm thành công.")

def doc_du_lieu():
    if not os.path.exists(TEN_FILE):
        return []
    with open(TEN_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def ghi_du_lieu(danh_sach):
    with open(TEN_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CAC_COT)
        writer.writeheader()
        writer.writerows(danh_sach)

def xoa_dong(danh_sach):
    if not danh_sach:
        print("Chưa có dữ liệu để xóa.")
        return
    hien_thi_danh_sach(danh_sach)
    while True:
        gia_tri = input("Nhập STT dòng muốn xóa: ")
        try:
            stt = int(gia_tri)
        except ValueError:
            print("STT phải là số. Vui lòng nhập lại.")
            continue
        if stt < 1 or stt > len(danh_sach):
            print(f"STT không hợp lệ. Vui lòng nhập từ 1 đến {len(danh_sach)}.")
            continue
        break
    da_xoa = danh_sach.pop(stt - 1)
    ghi_du_lieu(danh_sach)
    print(f"Đã xóa: {da_xoa['ten_cong_ty']}")

def hien_thi_danh_sach(danh_sach):
    if not danh_sach:
        print("Chưa có dữ liệu nào.")
        return
    print(f"{'STT':<5}{'Công ty':<20}{'Link':<25}{'Lương':<15}{'Trạng thái':<12}")
    for i, dong in enumerate(danh_sach, start=1):
        print(f"{i:<5}{dong['ten_cong_ty']:<20}{dong['link']:<25}{dong['muc_luong']:<15}{dong['trang_thai']:<12}")

def menu():
    danh_sach = doc_du_lieu()
    while True:
        print("\n--- TRÌNH THEO DÕI ỨNG TUYỂN ---")
        print("1. Xem danh sách")
        print("2. Thêm mới")
        print("3. Xóa")
        print("4. Thoát")
        lua_chon = input("Chọn: ")
        if lua_chon == "1":
            hien_thi_danh_sach(danh_sach)
        elif lua_chon == "2":
            them_moi(danh_sach)
        elif lua_chon == "3":
            xoa_dong(danh_sach)
        elif lua_chon == "4":
            print("Tạm biệt.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn 1-4.")

if __name__ == "__main__":
    menu()