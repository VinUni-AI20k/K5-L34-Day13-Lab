# Báo cáo cá nhân — NguyenVanMinh-2A202603771

## 1. Thông tin thành viên

- Họ tên: Nguyễn Văn Minh
- MSSV: 2A202603771
- Email: 26ai.minhnv7@vinuni.edu.vn
- Vai trong nhóm: **P2** · người kiểm số (trước giải lao), người viết code (sau giải lao)

## 2. Phần việc phụ trách

- Trước giải lao: kiểm tay số của nhiệm vụ A, tính A4 (chi phí cố định) và so sánh với nhân viên ở cấp cả hệ thống, kiểm B1–B4 và trả lời B3.
- Sau giải lao: viết phần D1 (cỡ mẫu), tỉ lệ mở lại hiện tại và E1 (ba chỉ số) trong `src/lab13.py`. Gửi số cho P3 (`pilot_plan.yaml`) và P4 (`bang_chi_phi.md`, `chi_so.md`, hồ sơ).
- Soát số của các nhiệm vụ A, B, D, E trước khi đóng gói.

## 3. Đóng góp cụ thể

- **Kiểm tay A2:** tính độc lập với code của P1, chỉ dùng module `csv` chuẩn, không dùng `mo_hinh`. Kết quả: 245.585 + 84.000 + 1.780.000 + 2.264.000 = 4.373.585 đ; chia 978 việc thành công được 4.472 đ/việc, gấp 16,3× hoá đơn/yêu cầu (274,7 đ) [simulated]. Khi P1 push code, tôi so từng khoản và thấy khớp hoàn toàn.
- **A4 · chi phí cố định:** phạm vi noi_dia + hang_nang có 900 việc thành công, cps 3.414 đ. Ở 45.000 yêu cầu/tháng: 33.750 việc thành công/tháng, cố định 1.185 đ/việc, cộng lại 4.599 đ = 0,38×. Ở một nửa khối lượng: 2.370 đ/việc, cộng lại 5.784 đ = 0,48× [simulated].
- **So với nhân viên tự làm, cấp cả hệ thống:** (4.373.585 + 222 × 12.000) / 1.200 = 5.865 đ/yêu cầu = 0,49× [simulated]. Không dùng con số 0,37×, vì con số đó chưa cộng các ca chuyển nhân viên.
- **Kiểm B:** kịch bản "giảm một nửa" đúng bằng nửa mức tăng của kịch bản "gấp đôi" (+5,6/−2,8; +40,7/−20,3; +51,8/−25,9). Trả lời B3: giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ), khác với giới hạn 1 lần có cps thấp nhất (4.111 đ), vì giới hạn 1 lần đẩy thêm 85 ca sang nhân viên [simulated].
- **D1 · cỡ mẫu** (`co_mau`, `he_so_thiet_ke`, `bang_d1`): a) 1.251 yêu cầu mỗi nhóm · b) 3.103 mỗi nhóm, cần 84 người > 40 · c) tối đa 1.000 < 1.251 · d) tối đa 300 · e) mức chênh 6 điểm, n = 859, m ≥ 299 (DE 6,96). Đánh đổi: nếu tác động thật chỉ 5 điểm thì power ≈ 0,64.
- **Tỉ lệ mở lại 7 ngày hiện tại:** 4,25% (51/1.200), trong phạm vi 3,97% (39/982). Đây là cơ sở để P3 đặt luật dừng an toàn: so với đối chứng (+2 điểm) kèm trần 6%, không đặt ngưỡng 3%.
- **E1 · ba chỉ số trong đợt chạy thử:** chính 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177) · an toàn 4,25% (51/1.200).

## 4. Bằng chứng

- Commit `6bdda32` trên nhánh `P2` (chỉ sửa `src/lab13.py`), PR #2: https://github.com/ddkhoa2605/K5-L3B-DAY13-MKTT-LaunchEconomics/pull/2
- Các hàm `bang_a4`, `co_mau`, `he_so_thiet_ke`, `bang_d1`, `ti_le_mo_lai`, `bang_e1` trong `src/lab13.py`. Chạy `cd src && python lab13.py` sẽ in đủ A1–A4, B1–B4, D1, tỉ lệ mở lại, E1.
- Đã sửa một lỗi làm tròn ở câu D1b: 1.251 × 2,48 = 3.102,48, phải làm tròn lên thành 3.103.
- Giải tay câu e: 20m ≥ 859 × (0,98 + 0,02m) → 2,82m ≥ 841,82 → m ≥ 298,5 → **299**.

## 5. Công cụ AI đã dùng

- **Claude Code:** dùng để đọc đề và tóm tắt việc của P2, viết script kiểm tay A2/A4 (chỉ dùng thư viện chuẩn, tính độc lập với `lab13.py`), và viết các hàm A4, D1, tỉ lệ mở lại, E1 trong `lab13.py`.
- **Cách tự kiểm tra:**
  - So mọi số với bảng đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`. Tất cả lệch ≤ 0,02%, trong ngưỡng 2%.
  - So hai nguồn độc lập với nhau: script kiểm tay và code của P1 cho cùng số A2.
  - Tự bấm máy lại phép cộng tổng A2, phép chia 40.000.000 / 33.750 và câu D1e.
- Không dùng AI để bịa số. Mọi số trong báo cáo đều do `lab13.py` in ra hoặc tính tay có ghi cách tính ở trên.

## 6. Tự đánh giá

- Đã làm xong phần việc của P2 trong kế hoạch nhóm, và số khớp đáp án.
- Hiểu được: tử số tính mọi lần chạy kể cả lần lỗi, còn mẫu số chỉ đếm việc thành công. Khi chia theo cụm, cỡ mẫu hiệu dụng bị chặn bởi c / ICC, nên số cụm quyết định chứ không phải tổng số yêu cầu.
- Cần cải thiện:
  - **Tự viết lại được phần code đã nhờ AI hỗ trợ:** viết lại hàm `co_mau` và giải bài toán m ≥ 299 mà không cần trợ giúp. Giải thích được vì sao chia theo nhân viên với m = 75 cần 84 người, trong khi nhóm chỉ có 40.
  - **Đưa số vào code sớm hơn:** A4 nên có trong `lab13.py` ngay từ CP1. Lần này A4 chỉ có trong script kiểm tay tới khi đổi vai sau giải lao.
  - **Bàn giao số nhanh hơn:** gửi số cho P3 và P4 ngay sau khi kiểm xong từng bảng, không gom tới cuối checkpoint, để người giữ hồ sơ điền dần được.
  - **Soát cả phần diễn giải, không chỉ con số:** khi review PR #3, các con số đều đúng, nhưng phần chữ đi kèm lại có lỗi: 15,3 phút làm lại bị ghi thành phút xem lại, và khoản "chạy lại" bị đếm hai lần trong luật dừng chi phí. Lần sau, bước soát A, B, D, E cuối buổi cần đọc cả phần diễn giải, vì đây là chỗ hội đồng dễ bắt lỗi nhất.
