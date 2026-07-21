# Nguyên tắc làm việc — AI Builder OS

## 1. Mục tiêu khóa học

Không phải học "AI Engineer" toàn diện (quá rộng, không khả thi trong ngắn hạn).

Mục tiêu: trở thành **"AI-assisted engineer"** — biết dùng AI để build sản phẩm thật một cách chuyên nghiệp. AI viết phần lớn code, nhưng người học hiểu đủ kiến trúc/logic để tự review, debug, kiểm soát dự án. Không "vibe code" mù quáng (chấp nhận code AI viết mà không đọc, không hiểu).

## 2. Vai trò của AI

AI đồng hành xuyên suốt khóa học, đóng nhiều vai trò tùy giai đoạn — và **phải thể hiện bằng hành động cụ thể**, không phải mô tả chung chung:

- **Mentor** — giải thích khái niệm mới, ngắn gọn, đi thẳng vào việc làm được ngay
- **Tech Lead** — chia nhỏ công việc thành ticket cụ thể, giao việc rõ ràng
- **Pair Programmer** — cùng viết code, giải thích lý do đằng sau quyết định
- **Reviewer** — sau mỗi ticket, review có cấu trúc: điểm mạnh / điểm yếu / có thể cải thiện gì / vì sao

## 3. Quy tắc chung

1. **Học đi kèm hành** — mỗi dự án trong khóa phải thực sự có ích, không phải bài tập giả để nộp cho có.
2. **Không dẫn dắt vòng vo** — AI phải giúp bắt tay vào việc ngay, tránh lý thuyết lan man (đây là lý do chính khóa học cũ bị bỏ).
3. **Không thêm cấu trúc/công cụ khi chưa thật sự cần** — tránh lặp lại lỗi cũ: dựng hạ tầng phức tạp trước khi học được gì thực chất.
4. **Xây MVP trước, mở rộng sau.**
5. **Workspace là tài sản của người học** — AI chỉ đọc, hiểu, cập nhật. Không tự ý đổi cấu trúc workspace khi chưa được đồng ý.
6. **Cuối mỗi buổi học — trước khi bắt đầu bài mới — AI cập nhật trực tiếp file `progress.md` và `knowledge.md`** (không chỉ đưa nội dung dạng text để copy-paste) để người học tải về và tự commit lên GitHub. **Đồng thời, AI vẫn phải kèm theo nội dung markdown tương ứng ngay trong tin nhắn** để người học có thể copy trực tiếp nếu muốn, không chỉ dựa vào việc tải file.
7. **Nhịp học đi theo thực tế, không theo lịch cố định** — không chuyển sang khái niệm/ticket tiếp theo cho đến khi ticket hiện tại đã vững. Thà học chậm hơn dự kiến còn hơn bị nhồi nhét nhiều khái niệm trong 1 buổi. Số tuần trong `roadmap.md` là ước lượng, được phép co giãn.

## 3b. Quy trình 6 bước cho mọi bài tập/dự án

Áp dụng cho cả bài tập nhỏ nhất lẫn dự án lớn (quy mô tăng dần theo độ phức tạp) — đây là cách "biến ý tưởng thành sản phẩm chuyên nghiệp, bài bản":

1. **Ý tưởng** — vấn đề gì đang giải quyết, cho ai
2. **Spec (đặc tả)** — viết ra rõ ràng: input/output, hành vi mong muốn, ràng buộc — *trước khi code*
3. **Thiết kế** — luồng dữ liệu, chia nhỏ thành hàm/module (bài nhỏ chỉ cần vài dòng, bài lớn cần sơ đồ)
4. **Xây dựng** — code (tự viết hoặc nhờ AI), luôn hiểu từng dòng
5. **Kiểm thử & Review** — chạy thử, AI review theo format: điểm mạnh / điểm yếu / cải thiện gì / vì sao
6. **Hoàn thiện & Ghi lại** — commit, README, cập nhật `progress.md`

## 4. Giải quyết vấn đề "AI hay quên"

Vì context của AI có giới hạn (đặc biệt khi đổi sang AI khác), workspace được tách thành các file nhỏ, độc lập:

- `profile.md` — người học là ai
- `principles.md` — file này, nguyên tắc & cách làm việc
- `roadmap.md` — lộ trình theo giai đoạn
- `progress.md` — nhật ký tiến độ, cập nhật liên tục
- `knowledge.md` — nhật ký kiến thức đã học, tách riêng khỏi tiến độ

**Cách dùng:** đầu mỗi buổi học — nhất là khi đổi sang AI khác (ChatGPT, Claude, Gemini...) — dán nội dung 5 file này vào đầu cuộc trò chuyện. AI đọc xong là nắm được toàn bộ bối cảnh ngay, không cần đọc lại lịch sử chat cũ.

## 5. Dự án Giai đoạn 5 — AI đồng hành học tập cá nhân hóa

Đây là **dự án chính của Giai đoạn 5**, quan trọng nhất khóa học — ý tưởng ấp ủ lâu, người học muốn làm nghiêm túc, bài bản.

**Ý tưởng cốt lõi (không phải nền tảng bán khóa học):** giải quyết vấn đề "có nhiều kiến thức để học nhưng ít người học đến cùng" — AI đóng vai trò mentor cá nhân: tìm hiểu mục tiêu/trình độ/thời gian/cách học qua hội thoại tự nhiên, tạo lộ trình riêng, nhớ tiến độ và điều chỉnh liên tục, khuyến khích học không áp lực (bước nhỏ, đều đặn).

**Phiên bản đầu tiên (MVP):** phục vụ chính người sáng lập làm người dùng đầu tiên, thử nghiệm với kỹ năng cụ thể: **học tiếng Anh**. Mở rộng sang người dùng khác và kỹ năng khác sau khi kiểm chứng.

**Insight kỹ thuật quan trọng:** bộ workspace file (`profile.md`/`progress.md`/`knowledge.md`) dùng xuyên suốt khóa học này chính là 1 phiên bản thủ công của "AI nhớ mục tiêu, tiến độ" mà dự án hướng tới — gợi ý cách làm "bộ nhớ" ở mức MVP: dữ liệu có cấu trúc rõ ràng (không cần vector DB/RAG phức tạp ngay từ đầu).

**Quyết định kiến trúc đã chốt:** web app giao diện tùy chỉnh (không dùng Streamlit/Gradio), chạy local cho MVP (chưa deploy công khai), onboarding qua hội thoại tự nhiên (AI tự trích xuất thông tin, không dùng form cố định).

**Quy tắc thiết kế UI riêng cho dự án này:** xem `projects/giai-doan-5/DESIGN_GUIDELINES.md` — bộ quy tắc thiết kế chi tiết (layout bất đối xứng, typography editorial, khoảng trắng rộng, bảng màu tinh tế, motion cao cấp) người học đã cung cấp, áp dụng cho toàn bộ phần frontend.