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

## Hàm (function)

- `def ten_ham(tham_so):` định nghĩa hàm; `return` trả giá trị ra ngoài để dùng tiếp
- Biến tạo bên trong hàm là biến cục bộ — ra khỏi hàm là mất, không dùng lại được nếu không return
- Python đọc hết các `def` trong file trước khi chạy code chính → thứ tự định nghĩa hàm trong file không quan trọng, miễn lúc *gọi* hàm thì hàm cần dùng đã được định nghĩa xong
- **Dead code:** đoạn code không đường nào dẫn tới được (vd sau `return`/`sys.exit()` trong cùng nhánh). Không gây lỗi nhưng gây rối người đọc — nên xóa hẳn, đừng để "code không bao giờ chạy" tồn tại trong file
- Tách hàm theo nguyên tắc mỗi hàm làm đúng 1 việc (nhập / tính / hiển thị) giúp code dễ đọc, dễ sửa từng phần

## Git: Branch, Pull Request, đọc diff

- `git checkout -b ten-nhanh` tạo + chuyển nhánh; làm việc trên nhánh riêng, không commit thẳng vào main
- PR cho xem diff: dòng `+` xanh = thêm, `-` đỏ = xóa — đọc diff trước khi merge là thói quen bắt buộc
- **Trước khi tạo branch mới: luôn `git status` (đảm bảo không còn gì chưa commit) và `git log --oneline -3` (xác nhận đang đứng đúng chỗ)** — quên bước này khiến các buổi học bị dồn chung vào 1 commit, làm sai lệch lịch sử
- Code không mất khi quên commit kịp thời (miễn sau đó có push), nhưng lịch sử git sẽ không phản ánh đúng quá trình làm việc thật
---
*Mỗi khái niệm mới thêm vào cuối phần giai đoạn tương ứng, không xóa cái cũ — đây là kho kiến thức tích lũy dần, dùng để ôn lại khi quên.*