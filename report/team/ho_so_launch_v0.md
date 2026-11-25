# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi **Giả lập**. Người phụ trách là một vai trò cụ thể, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot.

Nhóm: LuckyTeam · Lớp: [Điền L3A hoặc L3B]

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | [Điền sau merge `p1-A`: chi phí/việc thành công (simulated), bội số so với hoá đơn token+tool, chi phí đã cộng cố định 40 triệu/tháng ở quy mô đầy đủ và 1/2 khối lượng] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | [Điền sau merge `p2-B`: xếp hạng 1–2–3 và % biến động từ bảng độ nhạy B1/B2 (simulated)] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | [Điền sau merge `p1-A` & `p2-B`: chi phí cả hệ thống/yêu cầu so với 12.000 đ, phạm vi `noi_dia` + `hang_nang`, và kịch bản xem lại 100% B4 (simulated)] | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử (1.200 yc): Chính **82,83%** (994/1.200); Dùng — bỏ qua gợi ý **27,12%** (48/177); An toàn — mở lại 7 ngày **4,25%** (51/1.200). Phạm vi pilot (982 yc): 92,26% · 21,09% · 3,97%. Đủ 10 event có `trace_id` đo đủ 5 chỉ số. | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | [Điền sau merge `p3-CD`: tỉ lệ đồng thuận 2 người gắn nhãn (/20), 5 ca khắc phục đủ 5 loại Google PAIR] | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | [Điền sau merge `p3-CD`: phạm vi `noi_dia` + `hang_nang`, đơn vị chia cụm, MDE, power, số cụm/nhóm, 3 luật dừng NẾU–TRONG–THÌ–KHÔNG THÌ] | Chưa | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | [Điền sau merge `p2-B`: tóm tắt ít nhất 2 rủi ro kinh tế kèm tác động đã tính từ bảng B (simulated)] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất (nháp — chốt lại sau khi merge đủ số A–D):** **Go có điều kiện** cho kế hoạch pilot phạm vi `noi_dia` và `hang_nang` (loại `quoc_te` và `doi_tac`).

- **Điều kiện 1 (An toàn hệ thống):** Bổ sung khoá chống trùng lệnh hoàn tiền và cơ chế đối soát sổ cái hằng giờ (khắc phục lỗi ca 7 và ca 20) trước khi mở pilot. — *Người phụ trách:* Kỹ sư trưởng agent · *Ngày kiểm tra:* trước ngày bắt đầu pilot.
- **Điều kiện 2 (Thiết kế thống kê):** Phê duyệt bằng văn bản đánh đổi cỡ mẫu/MDE của phương án chia cụm theo `pilot_plan.yaml`. — *Người phụ trách:* Giám đốc vận hành LogiX-VN · *Ngày kiểm tra:* trước ngày bắt đầu pilot.
- **Điều kiện 3 (Đo lường thực tế):** Bật đủ 10 event có `trace_id` trong `chi_so.md` và thay hai cột phút `simulated` bằng thời gian xem lại, làm lại đo thật (`phut_xem_lai_thuc`, `phut_lam_lai_thuc`). — *Người phụ trách:* PM trợ lý hoàn phí · *Ngày kiểm tra:* cuối tuần 1 pilot.
- **Điều kiện 4 (Kiểm soát chi phí xem lại):** Có lộ trình hạ tỉ lệ xem lại theo bậc dựa trên tỉ lệ sửa/bỏ thực tế, tránh duy trì xem lại 100% kéo dài. — *Người phụ trách:* Trưởng nhóm CSKH · *Ngày kiểm tra:* cuối bước rollout 0.25.
