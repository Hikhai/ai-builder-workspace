# Kiến trúc kỹ thuật — AI Đồng Hành Học Tập (MVP)

## Tech stack đã chốt

| Thành phần | Công nghệ | Lý do |
|---|---|---|
| Backend | FastAPI + WebSocket | Đã học FastAPI (Giai đoạn 4); WebSocket cho chat real-time thay vì REST polling |
| Database | SQLite + SQLAlchemy (ORM) | Nhẹ cho MVP; ORM giúp đổi sang PostgreSQL sau này không cần viết lại logic |
| Frontend | React + Vite | Cần cho Framer Motion (theo DESIGN_GUIDELINES.md); quản lý nhiều màn hình (onboarding/lộ trình/chat/tiến độ) dễ hơn JS thuần khi app lớn dần |
| Animation | Framer Motion | Theo yêu cầu DESIGN_GUIDELINES.md |

## Cách làm việc với từng phần (đã thống nhất)

- **Backend, Database:** người học tự code, AI review từng bước (đúng quy trình đã quen suốt khóa)
- **Frontend (React):** AI viết phần lớn code, người học đọc/review/hỏi trong lúc xây dựng thật — không học lý thuyết React riêng trước. Vẫn phải tự test và hiểu luồng dữ liệu chính, không chấp nhận code không hiểu.

## Kiến trúc phân lớp (lấy cảm hứng từ DeepTutor — HKUDS)

Tách riêng 2 lớp để dễ mở rộng sau này mà không sửa code cũ:

- **`tools/`** — các hàm LLM gọi được (kỹ thuật function calling đã học Giai đoạn 3): `trich_xuat_ho_so()`, `tao_lo_trinh()`, `cap_nhat_tien_do()`
- **`capabilities/`** — luồng nghiệp vụ cấp cao, dùng nhiều Tools: `OnboardingFlow`, `MentorSessionFlow`

## Database schema (dự kiến, sẽ chốt chi tiết khi thiết kế)

- `ho_so` — hồ sơ người học (trình độ, mục tiêu, thời gian rảnh, cách học ưa thích)
- `lo_trinh` — danh sách milestone học tập + trạng thái
- `nhat_ky` — lịch sử phiên học, tóm tắt mỗi buổi (tương tự progress.md/knowledge.md của khóa học này)