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

## Spec là gì và vì sao quan trọng

**Spec (đặc tả)** là bản mô tả bằng chữ, viết ra *trước khi code*, nói rõ: chương trình này làm gì, nhận vào gì, trả ra gì, xử lý ra sao trong mọi tình huống. Giống như bản vẽ thiết kế nhà trước khi xây, hoặc tờ order rõ ràng trước khi vào bếp nấu — không phải vừa nấu vừa đoán khách muốn gì.

**Vì sao cần, dù chỉ 1 mình làm:** Nếu không viết ra, đầu óc sẽ tự lấp đầy chỗ trống bằng giả định — và giả định của bạn lúc 9h sáng có thể khác giả định lúc 3h chiều. Còn khi nhờ AI code hộ, AI *chỉ biết đúng những gì bạn viết ra* — không viết rõ, AI sẽ tự đoán thay, và đoán của AI chưa chắc đúng ý bạn (giống việc bạn từng viết "lọc bài chất lượng" — AI/con người đều không biết "chất lượng" nghĩa là gì nếu không có tiêu chí cụ thể).

**5 phần, áp dụng vào ví dụ Trình theo dõi ứng tuyển vừa làm xong:**

1. **Mục tiêu** — vấn đề gì, cho ai. *(Lưu lại các nơi đã nộp CV — cho chính bạn dùng)*
2. **Input/Output** — dữ liệu vào ra chính xác kiểu gì, định dạng gì. *(Vào: tên công ty, link, lương, trạng thái. Ra: bảng hiển thị + file CSV lưu lâu dài)*
3. **Quy tắc nghiệp vụ** — logic xử lý chính. *(Xem danh sách / thêm mới / xóa theo STT)*
4. **Trường hợp biên & lỗi** — liệt kê từng tình huống bất thường và cách xử lý, càng cụ thể càng tốt. *(Lương âm → báo lỗi cụ thể "không được âm", không phải chung chung "xử lý lỗi nhập sai")*
5. **Tiêu chí hoàn thành** — sao biết là xong đúng, phải đo được. *(Thêm 3 dòng, tắt mở lại vẫn còn — không phải "chạy không lỗi" chung chung)*

**Sai lầm hay gặp nhất — chính bạn đã gặp:** bỏ sót hoặc viết mơ hồ phần 4. Lần đầu viết spec, bạn chỉ ghi "xử lý các lỗi về bài tuyển dụng" — nghe hợp lý nhưng không đủ để biết phải code gì. Phải cụ thể tới mức: *sai ở trường nào, giá trị gì được coi là sai, xử lý ra sao (báo lỗi rồi dừng, hay báo lỗi rồi cho nhập lại)*. Thiếu sự cụ thể này, dù bạn tự code hay để AI code, đều phải tự đoán — và đoán thì dễ sai.

**Spec không cần đúng ngay từ lần đầu.** Bạn viết spec này qua 3 vòng sửa (từ ý tưởng quá rộng "tự động cào tin tuyển dụng" → thu hẹp đúng MVP "tự ghi lại CV đã nộp") — đó là quy trình bình thường, không phải thất bại. Viết ra được rồi mới thấy chỗ chưa hợp lý để sửa; nghĩ trong đầu thì không bao giờ tự lộ ra lỗ hổng.

## Viết spec chuyên nghiệp (5 phần)
Mục tiêu / Input-Output / Quy tắc nghiệp vụ / Trường hợp biên & lỗi / Tiêu chí hoàn thành. Phần "trường hợp biên" hay bị bỏ sót nhất — cần liệt kê cụ thể theo từng trường dữ liệu, không viết chung chung ("xử lý lỗi nhập sai" mơ hồ, "lương âm/chữ → báo lỗi, cho nhập lại" mới đủ rõ để code theo).

## Đọc file bằng đường dẫn tuyệt đối
`os.path.dirname(os.path.abspath(__file__))` lấy thư mục chứa script hiện tại, ghép với `os.path.join()` — để file dữ liệu luôn nằm đúng chỗ bất kể chạy lệnh từ thư mục nào. Đường dẫn tương đối (`"ten_file.csv"`) phụ thuộc vào *nơi đứng khi chạy lệnh*, không phải nơi chứa file `.py`.

## Validate từng ô độc lập trong 1 form
Mỗi ô có hàm nhập riêng, tự lặp `while True` tới khi đúng mới `return` — sai ô nào chỉ ô đó hỏi lại, giữ nguyên các ô đã nhập đúng trước đó. Tránh gộp chung validate cả form vào 1 khối, vì sẽ buộc người dùng nhập lại từ đầu khi chỉ sai 1 ô.

## Chương trình dạng menu sống liên tục
`while True` + nhánh thoát bằng `break` — khác với script Giai đoạn 1 (chạy 1 lần rồi kết thúc). Đọc dữ liệu 1 lần lúc mở chương trình, giữ trong biến, mọi thao tác sửa trực tiếp lên biến đó + ghi file ngay sau mỗi thay đổi.

## Bài học từ việc viết spec lần 2 (task/to-do)
- Khi liệt kê Quy tắc nghiệp vụ, dễ quên 1 chức năng cốt lõi nếu không đối chiếu lại với Mục tiêu ban đầu (thiếu hẳn "cập nhật trạng thái" dù mục tiêu đã nói rõ)
- Tự mâu thuẫn hay xảy ra giữa các phần spec khi thêm chi tiết dần dần (vd: vừa nói "hỏi lúc thêm mới" vừa nói "có giá trị mặc định" cho cùng 1 trường) — cần đọc lại toàn bộ spec sau khi sửa để bắt các mâu thuẫn này, không chỉ sửa từng chỗ riêng lẻ

## Bẫy thiết kế: sắp xếp ở nhiều nơi độc lập gây lệch dữ liệu
Nếu 2 hàm khác nhau (vd lưu file và hiển thị) tự sắp xếp riêng một danh sách, dễ tạo ra 2 "phiên bản thứ tự" khác nhau tồn tại song song trong chương trình. Khi 1 thao tác khác (xóa/cập nhật) dựa vào STT hiển thị nhưng lại thao tác trên bản chưa đồng bộ, sẽ gây lỗi ngầm (xóa/sửa nhầm) — không crash, không báo lỗi, chỉ sai âm thầm. Cách phòng tránh: chỉ giữ **1 nguồn sự thật** (single source of truth) — mọi thao tác cần STT phải dựa trên đúng bản vừa hiển thị gần nhất.

## sorted() với key — hàm như một giá trị
`key=ten_ham` (không ngoặc) nghĩa là đưa cho sorted() *chính hàm đó* để nó tự gọi lại cho từng phần tử — khác `ten_ham()` (có ngoặc) là gọi ngay lập tức. `key=ten_ham()` sẽ lỗi (thiếu tham số bắt buộc), hoặc nếu gọi có tham số cụ thể sẽ lỗi "not callable" vì sorted() cần một hàm để gọi lặp lại, không phải 1 giá trị cố định.

## Tuple và so sánh kiểu từ điển
`(a, b)` là tuple — gom nhiều giá trị thành 1 khối, giữ thứ tự, không sửa được. Python so 2 tuple bằng cách so từng phần tử từ trái sang phải, chỉ xét phần tử tiếp theo khi phần tử trước bằng nhau (giống so từ trong từ điển). Đây là cách "sắp theo tiêu chí A trước, tiêu chí B sau" được hiện thực mà không cần if/else phức tạp.

## Ép kiểu ngày tháng trước khi so sánh
So sánh 2 chuỗi ngày dạng text (`"20/07/2026"` vs `"05/08/2026"`) sẽ so theo ký tự, cho kết quả sai hoàn toàn. Phải dùng `datetime.strptime(chuoi, "%d/%m/%Y")` ép thành kiểu `datetime` thật trước khi so sánh. `datetime.now().strftime(...)` là chiều ngược — lấy ngày hệ thống, định dạng thành chuỗi.

## Dict trong list là tham chiếu, không phải bản sao
`cong_viec = danh_sach[i]` rồi sửa `cong_viec["truong"] = ...` sẽ tự động sửa luôn phần tử trong `danh_sach` gốc — không cần gán ngược lại. Vì dict là kiểu dữ liệu tham chiếu trong Python.

## Bài học spec: liệt kê rõ ràng buộc giữa các trường
Nếu 2 trường có quan hệ logic với nhau trong thực tế (vd hạn deadline nên sau ngày thêm việc), phải ghi rõ ràng buộc đó ngay trong spec — code sẽ không tự suy ra được, dù không có ràng buộc thì code vẫn "chạy đúng" theo nghĩa không lỗi, chỉ là kết quả không hợp lý ngoài đời thực.
---
*Mỗi khái niệm mới thêm vào cuối phần giai đoạn tương ứng, không xóa cái cũ — đây là kho kiến thức tích lũy dần, dùng để ôn lại khi quên.*