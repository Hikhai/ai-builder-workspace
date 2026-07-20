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

### Giai đoạn 2 (làm lại, chậm hơn) — Buổi A: Spec cho "Quản lý task/to-do có deadline"
- Nhận ra Giai đoạn 2 lần đầu (trình theo dõi ứng tuyển) đi quá nhanh trong 1 buổi chat liền mạch, không kịp ngấm — quyết định làm lại chậm hơn với 1 CLI tool khác, chia rõ từng buổi theo từng bước trong quy trình 6 bước
- Đã hoàn thành: viết spec đầy đủ 5 phần cho "Quản lý task/to-do có deadline" qua 2 vòng chỉnh sửa (phát hiện thiếu chức năng cập nhật trạng thái, mâu thuẫn giữa "hỏi lúc thêm" và "giá trị mặc định")
- Việc tiếp theo: Buổi B — Thiết kế (trước khi code)

### Giai đoạn 2 (làm lại) — Buổi B: Thiết kế cho task/to-do
- Đã hoàn thành: thiết kế 7 hàm dạng bảng (nhận vào/trả về), xác định luồng chạy
- Tự phát hiện lỗ hổng thiết kế thật: nếu sắp xếp riêng ở 2 chỗ (lưu file và hiển thị) mà không đồng bộ, STT người dùng thấy trên màn hình có thể lệch với STT dùng để xóa/cập nhật thật — dẫn tới xóa/sửa nhầm công việc
- Giải quyết bằng nguyên tắc: các hàm cần STT (xóa, cập nhật) luôn gọi hien_thi trước để đảm bảo dùng chung đúng 1 bản đã sắp xếp
- Việc tiếp theo: Buổi C — Xây dựng (code)

### Giai đoạn 2 (làm lại) — Buổi C: Xây dựng "Quản lý task/to-do có deadline"
- Đã hoàn thành: code đủ 7 hàm theo đúng thiết kế đã chốt (đọc/ghi CSV, sắp xếp theo tuple, thêm/cập nhật/xóa với validate từng ô, menu)
- Học sâu về sorted(key=...) qua nhiều vòng hỏi-đáp: hàm truyền như giá trị (không gọi bằng ()), tuple so sánh kiểu từ điển, vì sao phải ép kiểu datetime trước khi so ngày
- Tự phát hiện 2 vấn đề thật: (1) lỗi trong đoạn code test khiến mất dữ liệu cũ (quên đọc file trước khi ghi đè), (2) lỗ hổng nghiệp vụ trong spec — hạn deadline có thể là ngày trong quá khứ so với ngày thêm việc, do spec chưa từng ràng buộc điều này (rút kinh nghiệm cho spec lần sau, không sửa lại bản này)
- Nguyên tắc thiết kế "gọi hien_thi trước khi xóa/cập nhật để đồng bộ STT" đã được kiểm chứng hoạt động đúng qua test thực tế
- Việc tiếp theo: Giai đoạn 3 — LLM API & tích hợp tool

### Giai đoạn 3 — Buổi 1: Gọi LLM API + Token/Context window
- Đã hoàn thành: setup OpenRouter (API key, .env, .gitignore), gọi API thành công qua thư viện openai với base_url tùy chỉnh
- Gặp lỗi thật: model cụ thể (llama-3.3-70b-instruct:free) bị gỡ khỏi danh sách miễn phí ngay khi test — chuyển sang dùng "openrouter/free" (auto-router) để tránh phụ thuộc vào 1 tên model cụ thể dễ đổi
- Tự đo và tính toán tỷ lệ token/từ cho tiếng Việt (~2.2 token/từ) qua thực nghiệm, ước lượng ban đầu bị lệch xa (đoán "vài chục ngàn" trong khi thực tế ~1500) nhưng tự sửa đúng khi tính có căn cứ
- Phát hiện: model tự suy luận ý định từ nội dung (dán bài thơ → tự phân tích chi tiết dù không yêu cầu), tốn nhiều token hơn hẳn — liên hệ tới Prompt Engineering buổi sau
- Việc tiếp theo: Giai đoạn 3, Buổi 2 — Prompt engineering có hệ thống   

### Giai đoạn 3 — Buổi 2: Prompt engineering có hệ thống
- Đã hoàn thành: học system prompt, few-shot, structured output (JSON), xây hàm trích xuất công việc từ câu tiếng Việt tự nhiên qua LLM
- Tự phát hiện bug thật: model tính sai phép cộng ngày tháng ("tuần sau" ra ngày vẫn thuộc tuần này) dù system prompt đã cho đúng ngày hôm nay — 1/2 câu test đúng, 1/2 sai
- Bài học quan trọng: LLM suy luận bằng ngôn ngữ, không đảm bảo tính toán chính xác (ngày tháng, số học) dù có đủ dữ kiện đúng — cần tự kiểm chứng bằng code, không tin tuyệt đối
- Việc tiếp theo: Giai đoạn 3, Buổi 3 — Function calling / tool use cơ bản

### Giai đoạn 3 — Buổi 3 (mở rộng): Tự kiểm chứng function calling qua nhiều case khó
- Sau khi hoàn thành function calling cơ bản, tự test thêm nhiều câu hỏi mơ hồ/không dấu, phát hiện 2 lớp lỗi mới ngoài dự kiến ban đầu
- Lỗi 1 (đã sửa): model "bịa" lại kết quả cuối cùng khác với kết quả thật tool trả về (vd tool trả 20/08 nhưng model nói 1/8) — sửa bằng cách thêm dòng in "Kết quả thật từ hàm" để luôn đối chiếu được, và thêm vòng lặp xử lý nhiều lượt gọi tool (sửa luôn bug in ra None khi model cần gọi tool nhiều lần)
- Lỗi 2 (đã sửa): hàm tinh_ngay ban đầu không tính thứ trong tuần, khiến model phải tự đoán (sai) hoặc từ chối trả lời — sửa bằng cách để Python tính luôn thứ bằng datetime.weekday(), không để model tự suy luận
- Lỗi 3 (chưa sửa, ghi nhận làm bài học): tool tinh_ngay chỉ nhận tham số "số ngày" — khi câu hỏi nói bằng "tháng" (vd "20 tháng nữa"), model phải tự quy đổi tháng→ngày và làm sai. Phát hiện sâu hơn: quy đổi tháng→ngày về bản chất không chính xác vì độ dài tháng khác nhau — đây là lỗi thiết kế tool (chọn sai loại tham số), không phải lỗi model tính dở
- Quyết định: không mở rộng thêm tool cho "theo tháng" ở bài mini này, theo đúng nguyên tắc không thêm cấu trúc khi chưa cần
- Việc tiếp theo: Giai đoạn 4 — Dự án lớn: AI Hub tích hợp nhiều model
---
*Mỗi mục mới thêm vào cuối file, không xóa lịch sử cũ — để thấy được cả quá trình.*