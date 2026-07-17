# Nhật ký kiến thức

> Ghi lại kiến thức đã học, tách riêng khỏi `progress.md` (progress.md ghi *tiến độ*, file này ghi *nội dung đã học được*). AI soạn sẵn nội dung cần thêm sau mỗi buổi học — trước khi bắt đầu bài mới — để copy-paste thủ công vào đây.

## Giai đoạn 1 — Nền tảng + tập quy trình

## Biến & kiểu dữ liệu

- 4 kiểu cơ bản: `int`, `float`, `str`, `bool`
- `input()` luôn trả về `str` — cần ép kiểu `int(...)` / `float(...)` khi cần dùng làm số
- f-string: `f"...{bien}..."` để chèn biến vào chuỗi
- Format số: `:.0f` làm tròn số nguyên, `:,.0f` thêm dấu phẩy ngăn nghìn (kiểu Mỹ), `.replace(",", ".")` đổi sang kiểu Việt Nam (dấu chấm ngăn nghìn)
- **Bài học quan trọng:** biến nhận giá trị tại đúng thời điểm dòng lệnh chạy — không tự cập nhật theo biến khác đổi sau đó. Nếu cần giá trị luôn mới nhất, tính lại ngay trước khi dùng (ví dụ gọi hàm ngay tại chỗ `print`) thay vì gán sẵn vào biến trung gian rồi dùng lại

## Xử lý lỗi cơ bản (try/except)

- `try:` — thử chạy đoạn code có khả năng lỗi
- `except ValueError:` — bắt lỗi khi ép kiểu thất bại (vd chữ → số), chạy đoạn xử lý thay vì để chương trình crash
- Nguyên tắc: chỉ bọc `try` quanh đúng dòng rủi ro, không bọc luôn các dòng an toàn phía sau — tránh nuốt nhầm lỗi không liên quan, khó debug về sau
- Dừng chương trình sau khi báo lỗi: dùng `sys.exit()` (cần `import sys`), không dùng `exit()` — `exit()` chỉ đảm bảo hoạt động ổn định trong chế độ tương tác, không chuẩn cho script/chương trình thật
---
*Mỗi khái niệm mới thêm vào cuối phần giai đoạn tương ứng, không xóa cái cũ — đây là kho kiến thức tích lũy dần, dùng để ôn lại khi quên.*