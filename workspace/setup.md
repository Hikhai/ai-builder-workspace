# Hướng dẫn Setup — AI Builder OS

## 1. Cài Python

- **Windows:** vào [python.org/downloads](https://www.python.org/downloads/), tải bản mới nhất, khi cài **nhớ tick "Add python.exe to PATH"**
- **macOS:** mở Terminal, gõ `python3 --version` — nếu chưa có, cài qua [python.org](https://www.python.org/downloads/) hoặc `brew install python`
- Kiểm tra: mở terminal/cmd, gõ `python --version` (hoặc `python3 --version`) — thấy số phiên bản là ok

## 2. Cài Git + tạo tài khoản GitHub

- Tải Git: [git-scm.com/downloads](https://git-scm.com/downloads)
- Kiểm tra: `git --version`
- Tạo tài khoản tại [github.com](https://github.com) nếu chưa có
- Cấu hình lần đầu:
  ```
  git config --global user.name "Tên của bạn"
  git config --global user.email "email@vidu.com"
  ```

## 3. Cài VS Code

- Tải tại [code.visualstudio.com](https://code.visualstudio.com)
- Cài extension "Python" (của Microsoft) để có gợi ý code, debug

## 4. Tạo repo cho dự án

1. Trên GitHub, tạo repo mới tên `ai-builder-os` (public hoặc private tùy bạn)
2. Trên máy, tạo thư mục và đưa 4 file workspace vào:
   ```
   ai-builder-os/
     workspace/
       profile.md
       principles.md
       roadmap.md
       progress.md
       knowledge.md
     projects/
       giai-doan-1/
       giai-doan-2/
       ...
     README.md
   ```
   Tất cả bài tập/dự án trong khóa học nằm chung trong `projects/` của repo này — không tách thành repo riêng cho từng bài, để giữ đúng tinh thần "một workspace duy nhất, AI nào đọc vào cũng nắm được toàn bộ".
3. Đẩy lên GitHub:
   ```
   cd ai-builder-os
   git init
   git add .
   git commit -m "Khởi tạo workspace"
   git branch -M main
   git remote add origin https://github.com/<username>/ai-builder-os.git
   git push -u origin main
   ```

## 5. Cách dùng workspace mỗi buổi học

- **Đầu buổi:** mở 4 file trong `workspace/`, dán nội dung vào đầu cuộc trò chuyện với AI (Claude, ChatGPT, hoặc AI khác) — AI sẽ nắm được toàn bộ bối cảnh ngay
- **Cuối buổi:** cập nhật `progress.md` (tiến độ, kiến thức mới, việc tiếp theo), commit lại:
  ```
  git add workspace/progress.md
  git commit -m "Cập nhật tiến độ ngày ..."
  git push
  ```

## 6. Sẵn sàng cho Tuần 1

Không cần cài thêm gì phức tạp ở giai đoạn này. Tuần 7-8 (dự án AI Hub) mới cần thêm API key từ OpenRouter hoặc tương tự — lúc đó sẽ hướng dẫn cụ thể.