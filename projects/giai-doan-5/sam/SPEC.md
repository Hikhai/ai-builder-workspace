# Spec — Sam (MVP)

> AI đồng hành học tập cá nhân hóa. Không phải nền tảng bán khóa học — giải quyết vấn đề "có nhiều kiến thức để học nhưng ít người học đến cùng".

## 1. Mục tiêu
AI đóng vai trò mentor cá nhân giúp người dùng học tiếng Anh — tìm hiểu người dùng qua hội thoại, tạo lộ trình riêng, nhớ tiến độ qua từng lần mở app, điều chỉnh theo thời gian, học không áp lực (bước nhỏ, đều đặn).

## 2. Đối tượng & phạm vi MVP
Chỉ 1 người dùng (người sáng lập), chạy local, chỉ tiếng Anh (không tổng quát hóa sang kỹ năng khác ở MVP này).

## 3. Tính năng MVP
- **Onboarding (1 lần đầu):** hội thoại tự nhiên với AI — hỏi dần về trình độ, mục tiêu, thời gian rảnh, cách học ưa thích — trích xuất thành hồ sơ có cấu trúc, lưu vào DB
- **Tạo lộ trình:** dựa trên hồ sơ, AI sinh danh sách các bước học (milestone) có cấu trúc
- **Phiên học (mỗi lần mở app):** AI đọc lại hồ sơ + lộ trình + tiến độ, hiển thị bước tiếp theo, trò chuyện, gợi ý bài tập nhỏ
- **Ghi nhận tiến độ:** sau mỗi phiên, AI tự cập nhật trạng thái (đã học gì, điểm mạnh/yếu, ghi chú)
- **Điều chỉnh lộ trình:** phản hồi của người dùng (khó/dễ) → AI cập nhật các bước tiếp theo

## 4. Kiến trúc kỹ thuật
Xem chi tiết `ARCHITECTURE.md`.

## 5. Trường hợp biên & lỗi
- Model trích xuất hồ sơ sai định dạng → hỏi lại, không lưu dữ liệu rác
- Chưa hoàn thành onboarding mà vào thẳng phiên học → chặn lại, dẫn về onboarding
- Mất kết nối API giữa chừng → không mất dữ liệu đã nhập trước đó

## 6. Tiêu chí hoàn thành
Hoàn thành onboarding qua hội thoại tự nhiên → nhận lộ trình cá nhân hóa → có ít nhất 1 phiên học hoàn chỉnh (trò chuyện + ghi nhận tiến độ) → tắt mở lại app, AI vẫn nhớ đúng tiến độ, không hỏi lại từ đầu.

## Ngoài phạm vi MVP
Đa người dùng, deploy công khai, mở rộng sang kỹ năng khác, bộ nhớ dạng vector/RAG phức tạp.