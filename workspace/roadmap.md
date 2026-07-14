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

## Giai đoạn 4 — Dự án lớn: Ý tưởng → MVP → Ra mắt (ước lượng 2-3 tuần)

Đây là lúc áp dụng toàn bộ quy trình ở quy mô thật, và quay lại ý tưởng ban đầu của bạn: build "AI Hub" tích hợp nhiều model mã nguồn mở/miễn phí (qua OpenRouter, LiteLLM...) — lúc này đã đủ nền tảng để làm nghiêm túc.

- Ý tưởng thật + spec đầy đủ (không phải bài tập giả)
- Thiết kế kiến trúc: điểm vào gọi được nhiều model qua API tương thích OpenAI, xử lý lỗi, rate limit, fallback
- Build, test, review như một dự án thật
- README chuẩn, đẩy lên GitHub, coi như "ra mắt"

**Deliverable:** sản phẩm thật, dùng được lâu dài — không phải bài tập nộp cho xong

---

## Sau khi hoàn thành

Tổng kết portfolio: những gì đã xây, học được gì, còn thiếu gì để đi tiếp. Quyết định bước kế tiếp (đào sâu RAG/Agent, hay đi làm/thực tập).

---
*Cập nhật file này khi có thay đổi thực tế về kế hoạch — điều đó bình thường, không phải thất bại.*