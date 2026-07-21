# Lộ trình

> Số tuần dưới đây là **ước lượng**, không phải deadline cứng — xem nguyên tắc "nhịp học đi theo thực tế" trong `principles.md`. Mọi bài tập/dự án đều áp dụng **quy trình 6 bước** (Ý tưởng → Spec → Thiết kế → Xây dựng → Kiểm thử & Review → Hoàn thiện & Ghi lại), quy mô tăng dần theo độ phức tạp.

## Giai đoạn 1 — Nền tảng + tập quy trình (ước lượng 3 tuần)

Mỗi khái niệm học riêng 1 buổi, có bài luyện thêm, chỉ qua khái niệm mới khi đã vững.

- Biến, kiểu dữ liệu, input/output
- Xử lý lỗi cơ bản (try/except)
- Hàm (function)
- Git/GitHub cơ bản (commit, branch, PR, đọc diff)

Mỗi bài tập nhỏ đều làm đủ quy trình 6 bước ở quy mô mini (ví dụ Spec chỉ cần 2-3 dòng) — để quy trình này trở thành phản xạ chứ không phải thứ học riêng sau này.

**Deliverable:** vài script nhỏ trong `projects/giai-doan-1/`, mỗi cái có spec ngắn viết trước khi code

## Giai đoạn 2 — Spec-driven: làm việc chuyên nghiệp với AI coding agent (ước lượng 3 tuần)

- Viết spec chi tiết hơn: input/output rõ ràng, ràng buộc, trường hợp lỗi cần xử lý
- Thiết kế đơn giản trước khi code: vẽ luồng, chia module — tập thói quen thiết kế trước khi build
- Quy trình chuẩn khi làm với AI: AI đề xuất kế hoạch → mình duyệt → AI code từng bước → mình review diff trước khi chấp nhận
- Đặt câu hỏi khi không hiểu đoạn code AI viết ra — không bao giờ chấp nhận code mình không giải thích được

**Deliverable:** 1 CLI tool có spec + thiết kế viết tay trước khi code, AI hỗ trợ phần lớn code

## Giai đoạn 3 — LLM API & tích hợp tool (ước lượng 2-3 tuần)

- Gọi LLM API bằng Python, hiểu token/context window
- Prompt engineering có hệ thống (few-shot, structured output/JSON mode)
- Function calling / tool use cơ bản — nền tảng của "agent"
- Vẫn áp dụng đầy đủ quy trình 6 bước

**Deliverable:** 1 ứng dụng nhỏ có gọi LLM API thật (ví dụ: chatbot CLI trả lời dựa trên 1 file dữ liệu riêng)

## Giai đoạn 4 — Nền tảng Web (ước lượng 2 tuần)

Bổ sung do quyết định mới: dự án Giai đoạn 5 (AI Hub) sẽ là web app có giao diện đẹp, thân thiện — không dùng Streamlit/Gradio để tránh giao diện rập khuôn. Cần học nền tảng web trước khi xây dựng nghiêm túc.

- HTML/CSS cơ bản: cấu trúc trang, bố cục, styling
- JavaScript cơ bản: tương tác, gọi API từ trình duyệt (fetch)
- Backend API với Flask hoặc FastAPI: nhận request, trả response, kết nối với code Python đã biết (gọi LLM API, function calling...)
- Kết nối frontend ↔ backend: frontend gọi vào backend qua API, hiển thị kết quả động (không load lại trang)
- Vẫn áp dụng đầy đủ quy trình 6 bước, mỗi khái niệm 1 buổi, có thực hành nhỏ

**Deliverable:** 1 trang web nhỏ có backend Flask/FastAPI thật, frontend gọi API và hiển thị kết quả — làm nền để Giai đoạn 5 xây trên đó

## Giai đoạn 5 — Dự án lớn: AI đồng hành học tập cá nhân hóa (ước lượng 4-6 tuần)

Đây là dự án quan trọng nhất khóa học — ý tưởng ấp ủ lâu dài của người học. Không phải nền tảng bán khóa học, mà giải quyết vấn đề "có nhiều kiến thức để học nhưng ít người học đến cùng" bằng AI đóng vai trò mentor cá nhân: tìm hiểu người dùng qua hội thoại, tạo lộ trình riêng, nhớ tiến độ, điều chỉnh liên tục, học không áp lực.

**MVP:** phục vụ chính người sáng lập làm người dùng đầu tiên, thử nghiệm với việc học tiếng Anh. Xem chi tiết spec tại `projects/giai-doan-5/SPEC.md`.

**Quyết định kiến trúc đã chốt:**
- Web app giao diện tùy chỉnh (không dùng Streamlit/Gradio), theo `projects/giai-doan-5/DESIGN_GUIDELINES.md`
- Chạy local cho MVP, chưa deploy công khai
- Onboarding qua hội thoại tự nhiên, AI tự trích xuất thông tin (không dùng form cố định)
- "Bộ nhớ" mentor ở mức MVP dùng dữ liệu có cấu trúc (SQLite), không cần vector DB/RAG phức tạp ngay từ đầu — lấy cảm hứng từ chính bộ workspace file của khóa học này

**Việc cần làm:**
- Ý tưởng thật + spec đầy đủ (không phải bài tập giả)
- Thiết kế kiến trúc: backend (FastAPI) xử lý onboarding, tạo lộ trình, chat mentor, lưu tiến độ; frontend đẹp, thân thiện theo đúng quy tắc thiết kế riêng
- Build, test, review như một dự án thật
- README chuẩn, đẩy lên GitHub, coi như "ra mắt" (bản MVP cho chính người sáng lập dùng)

**Ngoài phạm vi MVP:** deploy công khai, đa người dùng, mobile app, chia sẻ API key có kiểm soát — để dành giai đoạn phát triển sau

**Deliverable:** sản phẩm thật, người sáng lập tự dùng được để học tiếng Anh, có nền tảng để mở rộng thêm tính năng và người dùng sau này — không phải bài tập nộp cho xong

---

## Sau khi hoàn thành

Tổng kết portfolio: những gì đã xây, học được gì, còn thiếu gì để đi tiếp. Với AI Hub, cân nhắc bước phát triển tiếp theo (mobile app, mô hình chia sẻ API key có kiểm soát, thêm tính năng cộng đồng). Quyết định hướng đi chung (đào sâu RAG/Agent, hay đi làm/thực tập).

---
*Cập nhật file này khi có thay đổi thực tế về kế hoạch — điều đó bình thường, không phải thất bại.*