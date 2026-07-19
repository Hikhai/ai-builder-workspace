import csv
import os
from datetime import datetime

THU_MUC_HIEN_TAI = os.path.dirname(os.path.abspath(__file__))
TEN_FILE = os.path.join(THU_MUC_HIEN_TAI, "task.csv")
CAC_COT = ["ten_cong_viec", "ngay_them", "tien_do", "trang_thai", "do_quan_trong", "han_deadline"]

TRANG_THAI_HOP_LE = ["Chưa làm", "Đang làm", "Đã xong"]
QUAN_TRONG_HOP_LE = ["Gấp", "Không gấp"]

def doc_du_lieu():
    if not os.path.exists(TEN_FILE):
        return []
    with open(TEN_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def ghi_file(danh_sach):
    with open(TEN_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CAC_COT)
        writer.writeheader()
        writer.writerows(danh_sach)

def sap_xep(danh_sach):
    def khoa_sap_xep(cong_viec):
        han = datetime.strptime(cong_viec["han_deadline"], "%d/%m/%Y")
        do_uu_tien_gap = 0 if cong_viec["do_quan_trong"] == "Gấp" else 1
        return (han, do_uu_tien_gap)
    return sorted(danh_sach, key=khoa_sap_xep)

def nhap_khong_rong(nhan):
    while True:
        gia_tri = input(nhan)
        if gia_tri.strip() == "":
            print("Không được để trống. Vui lòng nhập lại.")
            continue
        return gia_tri

def nhap_lua_chon(nhan, danh_sach_hop_le):
    while True:
        gia_tri = input(f"{nhan} ({'/'.join(danh_sach_hop_le)}): ")
        if gia_tri not in danh_sach_hop_le:
            print("Giá trị không hợp lệ. Vui lòng nhập lại.")
            continue
        return gia_tri

def nhap_ngay(nhan):
    while True:
        gia_tri = input(nhan)
        try:
            datetime.strptime(gia_tri, "%d/%m/%Y")
        except ValueError:
            print("Ngày không hợp lệ. Vui lòng nhập đúng định dạng dd/mm/yyyy.")
            continue
        return gia_tri

def them_moi(danh_sach):
    ten_cong_viec = nhap_khong_rong("Nhập tên công việc: ")
    do_quan_trong = nhap_lua_chon("Nhập mức độ quan trọng", QUAN_TRONG_HOP_LE)
    han_deadline = nhap_ngay("Nhập hạn deadline (dd/mm/yyyy): ")
    ngay_them = datetime.now().strftime("%d/%m/%Y")

    danh_sach.append({
        "ten_cong_viec": ten_cong_viec,
        "ngay_them": ngay_them,
        "tien_do": "Chưa có dữ liệu",
        "trang_thai": "Chưa làm",
        "do_quan_trong": do_quan_trong,
        "han_deadline": han_deadline,
    })
    print("Đã thêm thành công.")
    return danh_sach

def hien_thi(danh_sach):
    danh_sach_da_sap_xep = sap_xep(danh_sach)
    if not danh_sach_da_sap_xep:
        print("Chưa có công việc nào.")
        return danh_sach_da_sap_xep

    print(f"{'STT':<4}{'Tên công việc':<20}{'Ngày thêm':<12}{'Tiến độ':<20}{'Trạng thái':<12}{'Q.trọng':<10}{'Hạn':<12}")
    for i, cv in enumerate(danh_sach_da_sap_xep, start=1):
        print(f"{i:<4}{cv['ten_cong_viec']:<20}{cv['ngay_them']:<12}{cv['tien_do']:<20}{cv['trang_thai']:<12}{cv['do_quan_trong']:<10}{cv['han_deadline']:<12}")
    return danh_sach_da_sap_xep

def xoa(danh_sach):
    danh_sach = hien_thi(danh_sach)
    if not danh_sach:
        return danh_sach

    while True:
        gia_tri = input("Nhập STT công việc muốn xóa: ")
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
    print(f"Đã xóa: {da_xoa['ten_cong_viec']}")
    return danh_sach

def cap_nhat(danh_sach):
    danh_sach = hien_thi(danh_sach)
    if not danh_sach:
        return danh_sach

    while True:
        gia_tri = input("Nhập STT công việc muốn cập nhật: ")
        try:
            stt = int(gia_tri)
        except ValueError:
            print("STT phải là số. Vui lòng nhập lại.")
            continue
        if stt < 1 or stt > len(danh_sach):
            print(f"STT không hợp lệ. Vui lòng nhập từ 1 đến {len(danh_sach)}.")
            continue
        break

    cong_viec = danh_sach[stt - 1]

    tien_do_moi = input(f"Tiến độ mới (Enter để giữ '{cong_viec['tien_do']}'): ")
    if tien_do_moi.strip() != "":
        cong_viec["tien_do"] = tien_do_moi

    while True:
        trang_thai_moi = input(f"Trạng thái mới ({'/'.join(TRANG_THAI_HOP_LE)}) (Enter để giữ '{cong_viec['trang_thai']}'): ")
        if trang_thai_moi.strip() == "":
            break
        if trang_thai_moi not in TRANG_THAI_HOP_LE:
            print("Giá trị không hợp lệ. Vui lòng nhập lại.")
            continue
        cong_viec["trang_thai"] = trang_thai_moi
        break

    while True:
        han_moi = input(f"Hạn deadline mới (dd/mm/yyyy) (Enter để giữ '{cong_viec['han_deadline']}'): ")
        if han_moi.strip() == "":
            break
        try:
            datetime.strptime(han_moi, "%d/%m/%Y")
        except ValueError:
            print("Ngày không hợp lệ. Vui lòng nhập đúng định dạng dd/mm/yyyy.")
            continue
        cong_viec["han_deadline"] = han_moi
        break

    print("Đã cập nhật thành công.")
    return danh_sach

def menu():
    danh_sach = doc_du_lieu()
    while True:
        print("\n--- QUẢN LÝ CÔNG VIỆC ---")
        print("1. Xem danh sách")
        print("2. Thêm mới")
        print("3. Cập nhật")
        print("4. Xóa")
        print("5. Thoát")
        lua_chon = input("Chọn: ")
        if lua_chon == "1":
            danh_sach = hien_thi(danh_sach)
        elif lua_chon == "2":
            danh_sach = them_moi(danh_sach)
            ghi_file(danh_sach)
        elif lua_chon == "3":
            danh_sach = cap_nhat(danh_sach)
            ghi_file(danh_sach)
        elif lua_chon == "4":
            danh_sach = xoa(danh_sach)
            ghi_file(danh_sach)
        elif lua_chon == "5":
            print("Tạm biệt.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn 1-5.")

if __name__ == "__main__":
    menu()