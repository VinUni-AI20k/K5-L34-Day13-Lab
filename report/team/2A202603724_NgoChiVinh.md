# Báo cáo cá nhân — NgoChiVinh-2A202603724

## 1. Thông tin thành viên

- Họ tên: Ngô Chí Vĩnh
- MSSV: 2A202603724
- Email: 26ai.vinhnc2@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người kiểm số; phụ trách Nhiệm vụ D (cỡ mẫu, thiết kế pilot, luật dừng)

## 2. Phần việc phụ trách

- Nhiệm vụ D: phần D1 trong `src/lab13.py` (hàm `co_mau`, `he_so_thiet_ke`, `co_mau_hieu_dung`, `m_toi_thieu`, `nhiem_vu_d`) và file `report/team/pilot_plan.yaml`.
- Vai người kiểm số: tính tay một con số của Nhiệm vụ A để đối chiếu với code của người viết code.

## 3. Đóng góp cụ thể

- **D1 · Cỡ mẫu:** tính năm câu và ghi vào phần chú thích đầu `pilot_plan.yaml`.

  | Câu | Cách chia | Kết quả |
  | --- | --- | --- |
  | a | Chia theo yêu cầu | 1.251 mỗi nhóm |
  | b | Theo nhân viên, m = 75 | DE 2,48; cần 3.103 mỗi nhóm, tức 42 người mỗi nhóm; tổng 84 > 40 nên không đủ người |
  | c | 20 nhân viên mỗi nhóm | hiệu dụng tối đa 1.000 < 1.251 |
  | d | 6 depot mỗi nhóm | hiệu dụng tối đa 300 |
  | e | Mức chênh 6 điểm, 20 nhân viên mỗi nhóm | m ≥ 299 yêu cầu mỗi người, DE 6,96 |

- **Chọn cách chia:** theo nhân viên, 20 + 20, bốc thăm phân tầng theo depot.
  - Lý do: tách được tác động và đủ 20 cụm mỗi nhóm.
  - Đánh đổi đã ghi rõ: chỉ phát hiện được mức chênh 6 điểm; nếu tác động thật là 5 điểm thì power còn 0,64.
- **D2:** trả lời năm câu kiểm tra "tách được tác động" trong phần chú thích của file.
- **D3 · Luật dừng:** tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại trước khi đặt luật an toàn: 4,25% toàn mẫu, 3,97% trong phạm vi noi_dia + hang_nang.
  - Vì vậy dùng ngưỡng so với nhóm đối chứng (+2 điểm), kèm trần tuyệt đối 6%.
  - Viết 4 luật dừng theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ: an toàn (mở lại), an toàn (hoàn trùng hoặc sổ cái), chi phí (8.000 đ, simulated), mức độ sử dụng (bỏ qua gợi ý 40%).
- **Phần còn lại của file:** điền rollout, rollback, decision_date và danh sách `simulated_inputs`.
- **Kiểm số Nhiệm vụ A:** [cần điền: con số đã tính tay, cách tính, kết quả so với code]

## 4. Bằng chứng

- `src/lab13.py`, hàm `nhiem_vu_d`: in năm câu D1, power 0,64 và các tỉ lệ hiện tại (4,25%; 3,97%; 4,89% làm lại; 27,12% bỏ qua gợi ý).
- `report/team/pilot_plan.yaml`:
  - Đọc được bằng `yaml.safe_load`.
  - `grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'` không in gì.
  - Có 4 luật dừng đủ bốn vế.
- Commit: [cần điền mã commit sau khi push]

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude (Claude Code trong VS Code).
- **Dùng vào việc gì:**
  - Đọc và tóm tắt yêu cầu bài lab.
  - Góp ý phân công nhóm.
  - Viết code D1 trong `src/lab13.py`.
  - Soạn bản nháp `pilot_plan.yaml` và báo cáo này.
- **Cách tự kiểm tra:**
  - Đối chiếu năm số D1 với công thức trong `docs/du_lieu_va_cong_thuc.md`.
  - Tính tay câu e: 20m ≥ 859 × (0,98 + 0,02m) → m ≥ 298,5 → 299.
  - Chạy `yaml.safe_load` và lệnh grep kiểm tra dấu `?`.
  - Tự đọc lại từng luật dừng để chắc ngưỡng không làm pilot dừng ngay tuần đầu.
  - Đối chiếu các số A3/A4 trích sang `pilot_plan.yaml` với `bang_chi_phi.md` của nhóm.
- Mọi con số đều do code tính từ hai file CSV của lab, không lấy số do AI tự đưa ra.

## 6. Tự đánh giá

- **Làm tốt:** [tự điền]
- **Còn hạn chế:** [tự điền; ví dụ chưa thử chia theo yêu cầu kết hợp phân tầng, ngày bắt đầu pilot là giả định]
- **Điều học được:** khi chia theo cụm, số cụm quyết định cỡ mẫu hiệu dụng (trần c / ICC), không phải tổng số yêu cầu.
