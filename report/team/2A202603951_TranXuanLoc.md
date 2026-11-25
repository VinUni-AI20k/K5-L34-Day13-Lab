# Báo cáo cá nhân — TranXuanLoc-2A202603951

## 1. Thông tin thành viên

- Họ tên: Trần Xuân Lộc
- MSSV: 2A202603951
- Email: xuanloca2tv@gmail.com
- Vai trong nhóm: P3 — Người gắn nhãn 1

## 2. Phần việc phụ trách

- **Nhiệm vụ C (`report/team/bang_loi.md`):** Đọc 20 ca lỗi trong đề bài, gắn nhãn độc lập theo 5 loại Google PAIR (cột Nhãn người 1), phối hợp với P4 đối chiếu tỉ lệ đồng thuận, viết quy tắc phân biệt các ca dễ nhầm và lập bảng khắc phục 5 ca đại diện (mỗi loại 1 ca).
- **Nhiệm vụ D (`report/team/pilot_plan.yaml`):** Tiếp nhận số liệu cỡ mẫu D1 và tỉ lệ mở lại 7 ngày từ P2 để hoàn thiện toàn bộ file `pilot_plan.yaml` (phần chú thích D1, D2, đánh đổi MDE +6 điểm, thông số `primary_metric`, `identifiability`, 3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`, phương án `rollback` và `simulated_inputs`).
- **Nhiệm vụ E1 (`report/team/chi_so.md`):** Xây dựng danh sách event theo dõi có gắn `trace_id` và kiểm tra chéo ánh xạ event với từng chỉ số trong bảng E1.
- Tham gia duyệt chéo Gate 2a cùng nhóm và hoàn thiện báo cáo cá nhân.

## 3. Đóng góp cụ thể

- Hoàn thành gắn nhãn độc lập 20/20 ca lỗi (cột Nhãn người 1), đối chiếu với P4 đạt đồng thuận `20/20` (`100%` ≥ `80%`), bổ sung 5 quy tắc phân biệt nguyên nhân gốc (ca 6, 8, 9, 12, 13, 15, 18) và bảng khắc phục 5 ca (Ca 9, 7, 18, 4, 17) có cách phát hiện đo được (event, ngưỡng, tần suất) và vai trò phụ trách cụ thể.
- Hoàn thiện toàn bộ `report/team/pilot_plan.yaml` chọn phương án chia ngẫu nhiên theo nhân viên (`20 + 20`, phân tầng theo depot), ghi rõ đánh đổi nâng MDE lên `+6 điểm` (`n = 859/nhóm`, `DE = 6,96`, `m ≥ 299` yêu cầu/người; power còn `0,64` nếu tác động thật `+5 điểm`), thiết lập 3 luật dừng (an toàn dựa trên nền `4,25%` / `3,97%`, chi phí `> 8.000 đ`, bỏ qua gợi ý `> 40%`) và quy trình rollback 30 phút.
- Thiết kế 10 event có `trace_id` (vượt yêu cầu tối thiểu 6 event) trong `report/team/chi_so.md` cùng phần kiểm tra chéo đảm bảo đo được toàn bộ 5 chỉ số E1 và thay thế thời gian `simulated` bằng thời gian đo thực tế trong pilot.

## 4. Bằng chứng

- Nhánh `feat/loc/gan_nhan_1` đã merge vào `main` qua PR #2 (`8bc87ae`), gồm 3 commit:
  - `69c3f3b` — `feat(D): complete pilot_plan.yaml with D1 sample size, D2 and stop rules`
  - `aa30f3e` — `feat(E1): add event list with trace_id and metric cross-check in chi_so.md`
  - `8b52b3b` — `feat(C): add P3 independent error labels and 5-case mitigation table in bang_loi.md`
- Các file đóng góp:
  - [report/team/bang_loi.md](bang_loi.md)
  - [report/team/pilot_plan.yaml](pilot_plan.yaml)
  - [report/team/chi_so.md](chi_so.md)
  - [report/team/2A202603951_TranXuanLoc.md](2A202603951_TranXuanLoc.md)

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (trợ lý AI trong IDE).
- **Mục đích sử dụng:** Rà soát checklist yêu cầu của lab, trích xuất danh sách 20 ca lỗi từ file `.docx`, hỗ trợ cấu trúc hóa bảng 10 event có `trace_id`, định dạng `pilot_plan.yaml` và kiểm tra các quy tắc cấm từ hoặc thiếu dấu hỏi.
- **Cách tự kiểm tra:** Đối chiếu trực tiếp mọi con số D1 (`1.251`, `DE = 2,48`, `n_hiệu_dụng = 1.000`, `m ≥ 299`, `DE = 6,96`, power `0,64`) và tỉ lệ mở lại (`4,25%` / `3,97%`) từ kết quả P2 bàn giao; đối chiếu nhãn lỗi 20 ca với định nghĩa 5 loại Google PAIR và so chéo với P4; chạy kiểm tra tự động đảm bảo `0` dấu `?` ngoài dòng chú thích trong `pilot_plan.yaml` và `0` từ `"production"` trong toàn bộ `report/team/`.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ và đầy đủ toàn bộ đầu việc được phân công cho vai P3, không gây xung đột Git nhờ tách nhánh riêng và chia rõ phạm vi chỉnh sửa từng file với P1, P2, P4.
- Nắm chắc lý do phải chia cụm theo nhân viên (`20 + 20`) thay vì chia theo depot (chỉ 6 cụm) hay theo yêu cầu (tràn tác động), cũng như nguyên tắc gắn nhãn theo nguyên nhân gốc và đặt ngưỡng dừng an toàn dựa trên tỉ lệ mở lại thực tế.
