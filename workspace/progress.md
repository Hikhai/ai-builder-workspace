# Nhật ký tiến độ

> Cập nhật cuối mỗi buổi học. AI đọc file này để biết đang ở đâu — không cần đọc lại lịch sử chat.

## Trạng thái hiện tại

- **Giai đoạn:** Giai đoạn 1

## Lịch sử

### Buổi 1 — Biến & kiểu dữ liệu
- Đã hoàn thành: học biến/kiểu dữ liệu cơ bản (int, float, str, bool), làm bài "Hóa đơn cà phê" theo đủ quy trình 6 bước
- Tự phát hiện và sửa 1 bug thật (biến format tính sai thời điểm — không tự cập nhật khi giá trị gốc đổi sau đó), giải quyết bằng cách tự vận dụng hàm dù chưa học chính thức
- Đang mơ hồ: chưa có gì nổi bật ở phần này
- Việc tiếp theo: buổi 2 — xử lý lỗi cơ bản (try/except), hoặc luyện thêm biến/kiểu dữ liệu nếu muốn chắc hơn trước khi qua bài mới

### Buổi 2 — Xử lý lỗi cơ bản (try/except)
- Đã hoàn thành: học try/except, áp dụng vào hoa_don.py để không crash khi nhập sai dữ liệu
- Làm đúng ngay từ lần đầu: chỉ bọc try quanh đúng phần rủi ro (input), không bọc luôn phần tính toán/in kết quả
- Đang mơ hồ: chưa có gì nổi bật
- Việc tiếp theo: buổi 3 — hàm (function), hoặc luyện thêm try/except nếu muốn chắc hơn

### Buổi 3 — Hàm (function)
- Đã hoàn thành: học hàm (def, tham số, return, biến cục bộ), tách hoa_don.py thành 4 hàm rõ trách nhiệm (nhap_du_lieu, tinh_tong_tien, in_ket_qua, dinh_dang_tien)
- Tự phát hiện được vì sao thứ tự định nghĩa hàm trong file không quan trọng (Python đọc hết các def trước khi chạy code chính)
- Tự sửa được dead code (dòng return thừa không bao giờ chạy tới) sau khi được chỉ ra
- Đang mơ hồ: chưa có gì nổi bật
- Việc tiếp theo: buổi 4 — Git/GitHub cơ bản (commit, branch, PR, đọc diff) — đây là khái niệm cuối của Giai đoạn 1

### Buổi 4 — Branch, Pull Request, đọc diff (hoàn thành Giai đoạn 1)
- Đã hoàn thành: học branch/PR/diff, thêm tính năng loại đồ uống qua nhánh riêng + merge PR
- Phát hiện lỗi quy trình thật: quên commit+push buổi 3 trước khi tạo nhánh mới, khiến buổi 3 và 4 bị dồn chung 1 commit — tự dùng git log để chẩn đoán đúng nguyên nhân
- Thói quen mới thêm: chạy git status + git log --oneline -3 trước khi tạo branch mới
- Việc tiếp theo: Giai đoạn 2 — spec-driven, làm việc chuyên nghiệp với AI coding agent

### Giai đoạn 2 — Spec-driven: Trình theo dõi ứng tuyển việc làm
- Đã hoàn thành: viết spec đầy đủ 5 phần qua 3 vòng chỉnh sửa (từ ý tưởng ảo tưởng "tự động cào tin tuyển dụng" thu hẹp về đúng MVP), AI đề xuất kế hoạch code từng bước, review diff từng hàm trước khi ghép
- Xây xong: doc_du_lieu/ghi_du_lieu (CSV, đường dẫn tuyệt đối), hien_thi_danh_sach, them_moi (validate từng ô độc lập), xoa_dong (validate STT), menu (vòng lặp while sống tới khi thoát)
- Phát hiện & tự sửa bug thật: đường dẫn tương đối khiến CSV bị tạo sai thư mục khi chạy script từ nơi khác
- Đang mơ hồ: chưa có gì nổi bật
- Việc tiếp theo: Giai đoạn 3 — LLM API & tích hợp tool
---
*Mỗi mục mới thêm vào cuối file, không xóa lịch sử cũ — để thấy được cả quá trình.*