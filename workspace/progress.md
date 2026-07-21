# Nhật ký tiến độ

> Cập nhật cuối mỗi buổi học. AI đọc file này để biết đang ở đâu — không cần đọc lại lịch sử chat.

## Trạng thái hiện tại

- **Giai đoạn:** Giai đoạn 3 — đã hoàn thành, sẵn sàng sang Giai đoạn 4

## Lịch sử

### Buổi 1 — Biến & kiểu dữ liệu
- Đã hoàn thành: học biến/kiểu dữ liệu cơ bản (int, float, str, bool), làm bài "Hóa đơn cà phê" theo đủ quy trình 6 bước
- Tự phát hiện và sửa 1 bug thật (biến format tính sai thời điểm — không tự cập nhật khi giá trị gốc đổi sau đó), giải quyết bằng cách tự vận dụng hàm dù chưa học chính thức
- Việc tiếp theo: buổi 2 — xử lý lỗi cơ bản (try/except)

### Buổi 2 — Xử lý lỗi cơ bản (try/except)
- Đã hoàn thành: học try/except, áp dụng vào hoa_don.py để không crash khi nhập sai dữ liệu
- Làm đúng ngay từ lần đầu: chỉ bọc try quanh đúng phần rủi ro (input), không bọc luôn phần tính toán/in kết quả
- Việc tiếp theo: buổi 3 — hàm (function)

### Buổi 3 — Hàm (function)
- Đã hoàn thành: học hàm (def, tham số, return, biến cục bộ), tách hoa_don.py thành 4 hàm rõ trách nhiệm (nhap_du_lieu, tinh_tong_tien, in_ket_qua, dinh_dang_tien)
- Tự phát hiện được vì sao thứ tự định nghĩa hàm trong file không quan trọng
- Tự sửa được dead code (dòng return thừa không bao giờ chạy tới) sau khi được chỉ ra
- Việc tiếp theo: buổi 4 — Git/GitHub cơ bản

### Buổi 4 — Branch, Pull Request, đọc diff (hoàn thành Giai đoạn 1)
- Đã hoàn thành: học branch/PR/diff, thêm tính năng loại đồ uống qua nhánh riêng + merge PR
- Phát hiện lỗi quy trình thật: quên commit+push buổi 3 trước khi tạo nhánh mới, khiến buổi 3 và 4 bị dồn chung 1 commit
- Thói quen mới thêm: chạy git status + git log --oneline -3 trước khi tạo branch mới
- Việc tiếp theo: Giai đoạn 2 — spec-driven

### Giai đoạn 2 (lần 1) — Spec-driven: Trình theo dõi ứng tuyển việc làm
- Đã hoàn thành: viết spec đầy đủ 5 phần qua 3 vòng chỉnh sửa, AI đề xuất kế hoạch code từng bước, review diff từng hàm trước khi ghép
- Xây xong: doc_du_lieu/ghi_du_lieu (CSV, đường dẫn tuyệt đối), hien_thi_danh_sach, them_moi (validate từng ô độc lập), xoa_dong (validate STT), menu
- Phát hiện & tự sửa bug thật: đường dẫn tương đối khiến CSV bị tạo sai thư mục khi chạy script từ nơi khác
- Nhận xét quan trọng: cả giai đoạn làm liền 1 buổi chat dài, không kịp ngấm — quyết định làm lại chậm hơn với CLI tool khác

### Giai đoạn 2 (làm lại) — Buổi A: Spec cho "Quản lý task/to-do có deadline"
- Đã hoàn thành: viết spec đầy đủ 5 phần qua 2 vòng chỉnh sửa (phát hiện thiếu chức năng cập nhật trạng thái, mâu thuẫn giữa "hỏi lúc thêm" và "giá trị mặc định")
- Việc tiếp theo: Buổi B — Thiết kế

### Giai đoạn 2 (làm lại) — Buổi B: Thiết kế cho task/to-do
- Đã hoàn thành: thiết kế 7 hàm dạng bảng (nhận vào/trả về), xác định luồng chạy
- Tự phát hiện lỗ hổng thiết kế thật: nếu sắp xếp riêng ở 2 chỗ (lưu file và hiển thị) mà không đồng bộ, STT hiển thị có thể lệch với STT dùng để xóa/cập nhật
- Giải quyết bằng nguyên tắc: các hàm cần STT luôn gọi hien_thi trước để dùng chung đúng 1 bản đã sắp xếp
- Việc tiếp theo: Buổi C — Xây dựng

### Giai đoạn 2 (làm lại) — Buổi C: Xây dựng "Quản lý task/to-do có deadline" (hoàn thành Giai đoạn 2)
- Đã hoàn thành: code đủ 7 hàm theo đúng thiết kế đã chốt
- Học sâu về sorted(key=...): hàm truyền như giá trị, tuple so sánh kiểu từ điển, vì sao phải ép kiểu datetime trước khi so ngày
- Tự phát hiện 2 vấn đề thật: (1) lỗi trong đoạn code test khiến mất dữ liệu cũ, (2) lỗ hổng nghiệp vụ trong spec — hạn deadline có thể là ngày trong quá khứ so với ngày thêm việc (rút kinh nghiệm cho spec lần sau)
- Nguyên tắc "gọi hien_thi trước khi xóa/cập nhật để đồng bộ STT" đã được kiểm chứng đúng qua test thực tế
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

### Giai đoạn 3 — Buổi 3: Function calling / tool use (hoàn thành Giai đoạn 3)
- Đã hoàn thành: học function calling (khai báo tools, model yêu cầu gọi hàm, Python thực thi, gửi kết quả gọi lại lần 2), áp dụng để sửa đúng lỗi tính ngày sai đã phát hiện ở Buổi 2
- Xác nhận qua test: model gọi đúng tool khi cần (câu hỏi về ngày), sẽ trả lời thẳng qua nhánh else khi không liên quan (tự trả lời đúng, không cần chạy thử thêm)
- Hiểu rõ luồng 4 bước: gửi câu hỏi + tools → model yêu cầu gọi hàm (không tự chạy) → Python thực thi hàm thật → gửi kết quả + tool_call_id khớp đúng → gọi lại API lần 2 để model diễn đạt câu trả lời cuối
- Việc tiếp theo: Giai đoạn 4 — Dự án lớn: Ý tưởng → MVP → Ra mắt (AI Hub tích hợp nhiều model)

### Giai đoạn 3 — Buổi 3 (mở rộng): Tự kiểm chứng function calling qua nhiều case khó
- Sau khi hoàn thành function calling cơ bản, tự test thêm nhiều câu hỏi mơ hồ/không dấu, phát hiện 2 lớp lỗi mới ngoài dự kiến ban đầu
- Lỗi 1 (đã sửa): model "bịa" lại kết quả cuối cùng khác với kết quả thật tool trả về (vd tool trả 20/08 nhưng model nói 1/8) — sửa bằng cách thêm dòng in "Kết quả thật từ hàm" để luôn đối chiếu được, và thêm vòng lặp xử lý nhiều lượt gọi tool (sửa luôn bug in ra None khi model cần gọi tool nhiều lần)
- Lỗi 2 (đã sửa): hàm tinh_ngay ban đầu không tính thứ trong tuần, khiến model phải tự đoán (sai) hoặc từ chối trả lời — sửa bằng cách để Python tính luôn thứ bằng datetime.weekday(), không để model tự suy luận
- Lỗi 3 (chưa sửa, ghi nhận làm bài học): tool tinh_ngay chỉ nhận tham số "số ngày" — khi câu hỏi nói bằng "tháng" (vd "20 tháng nữa"), model phải tự quy đổi tháng→ngày và làm sai (dùng số cố định 31 cho mọi trường hợp). Phát hiện sâu hơn: quy đổi tháng→ngày về bản chất không chính xác vì độ dài tháng khác nhau — đây là lỗi thiết kế tool (chọn sai loại tham số), không phải lỗi model tính dở
- Quyết định: không mở rộng thêm tool cho "theo tháng" ở bài mini này, theo đúng nguyên tắc không thêm cấu trúc khi chưa cần — để dành cho dự án AI Hub ở Giai đoạn 4
- Việc tiếp theo: Giai đoạn 4 — Dự án lớn: AI Hub tích hợp nhiều model

### Chốt kế hoạch trước Giai đoạn 4: Nâng tầm dự án AI Hub
- Người học chia sẻ: dự án AI Hub (Giai đoạn 5, trước đây gọi Giai đoạn 4) là ý tưởng ấp ủ lâu, muốn làm nghiêm túc, bài bản, có thể mở rộng và đưa ra cộng đồng người dùng, tương lai xa hơn là mobile app
- Đã chốt kiến trúc: web app giao diện tùy chỉnh đẹp (không dùng Streamlit/Gradio vì rập khuôn), mỗi người dùng tự nhập API key riêng (BYOK) thay vì dùng chung 1 key
- Phát hiện khoảng cách kỹ năng: roadmap từ đầu tới giờ chỉ có Python CLI, chưa có frontend/backend web — quyết định chèn thêm Giai đoạn 4 mới (nền tảng Web: HTML/CSS/JS, Flask/FastAPI, kết nối frontend-backend) trước khi vào dự án AI Hub (dời thành Giai đoạn 5)
- Người học từng học qua Frontend/Backend cơ bản trước đây nhưng quên gần hết, tương tự tình trạng với Python lúc đầu khóa học
- Việc tiếp theo: Giai đoạn 4, Buổi 1 — HTML/CSS cơ bản

### Giai đoạn 4 — Buổi 1: HTML/CSS cơ bản (ôn lại)
- Đã hoàn thành: ôn HTML/CSS cơ bản (thẻ, class, flexbox), làm trang profile card tĩnh (tên, giới thiệu, danh sách kỹ năng ngang) qua 3 vòng chỉnh sửa
- Tự phát hiện qua nhắc nhở: text-align: center (căn chữ) khác với margin: auto (căn cả khối) — 2 khái niệm dễ nhầm khi mới ôn lại
- Học lại: justify-content/align-items chỉ có tác dụng trên phần tử là flex container, đặt nhầm trên phần tử con không chứa gì thêm sẽ vô tác dụng (liên hệ bài học "dead code" ở Python)
- Việc tiếp theo: Giai đoạn 4, Buổi 2 — JavaScript cơ bản

### Giai đoạn 4 — Buổi 2: JavaScript cơ bản (ôn lại)
- Đã hoàn thành: ôn JS cơ bản (let/const, arrow function, DOM API, addEventListener), thêm nút "Thêm kỹ năng" động vào trang profile card
- Tự áp dụng đúng nguyên tắc "truyền hàm như giá trị" đã học ở Python (addEventListener nhận tên hàm, không gọi bằng ()) sang ngôn ngữ mới
- Học quy ước đặt tên camelCase của JS (khác snake_case quen thuộc từ Python)
- Việc tiếp theo: Giai đoạn 4, Buổi 3 — Backend API với Flask/FastAPI

### Giai đoạn 4 — Buổi 3: Backend API với FastAPI (hoàn thành Giai đoạn 4)
- Đã hoàn thành: xây API POST /trich-xuat, tái sử dụng thành công logic trich_xuat() từ Giai đoạn 3 vào kiến trúc backend mới
- Tự phát hiện lỗi thiết kế route: dùng GET + tham số URL thay vì POST + body — đã sửa đúng, hiểu được lý do bản chất (GET để lấy dữ liệu, POST để gửi dữ liệu xử lý; tiếng Việt có dấu không phù hợp nhét vào URL)
- Học Pydantic model để validate tự động dữ liệu đầu vào của request
- Sửa xử lý lỗi: từ "return None" âm thầm (HTTP 200 kèm null) sang "raise HTTPException" đúng chuẩn (HTTP 500 kèm thông báo rõ ràng) — tự kiểm chứng bằng cách cố tình gây lỗi model rồi khôi phục lại
- Việc tiếp theo: Giai đoạn 5 — Dự án lớn: AI Hub (web app hướng cộng đồng người dùng)

### Giai đoạn 5 — Pivot & Spec: AI Đồng Hành Học Tập
- Người học tiết lộ dự án thật (khác "AI Hub multi-model" đã bàn trước đó): ứng dụng AI mentor cá nhân hóa giúp học tập/phát triển bản thân, giải quyết vấn đề "nhiều kiến thức nhưng ít người học đến cùng" — không phải nền tảng bán khóa học
- Đã chốt spec MVP: người dùng đầu tiên là chính người học, thử nghiệm với việc học tiếng Anh; onboarding qua hội thoại tự nhiên (AI trích xuất hồ sơ), tạo lộ trình cá nhân hóa, phiên học có ghi nhận tiến độ, AI nhớ qua các lần mở app
- Insight quan trọng: bộ workspace file (profile/progress/knowledge) của chính khóa học này là 1 phiên bản thủ công của ý tưởng "AI nhớ tiến độ" — dùng làm cảm hứng thiết kế bộ nhớ MVP (dữ liệu có cấu trúc, không cần vector DB/RAG ngay)
- Đã nghiên cứu tham khảo kiến trúc từ repo DeepTutor (HKUDS) — học theo mô hình tách Tools/Capabilities để dễ mở rộng
- Đã chốt tech stack: FastAPI + WebSocket (backend), SQLite + SQLAlchemy ORM (database), React + Vite + Framer Motion (frontend)
- Đã chốt cách làm việc: backend/database người học tự code (AI review), frontend React để AI viết nhiều hơn, người học học qua đọc/review trong lúc xây dựng thật
- Việc tiếp theo: thiết kế chi tiết database schema (SQLAlchemy models)

---
*Mỗi mục mới thêm vào cuối file, không xóa lịch sử cũ — để thấy được cả quá trình.*