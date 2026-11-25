# Rubric

Điểm giữ nguyên như đề bài gốc: **70 điểm đối chiếu đáp án** (trợ giảng chấm, C1–C5) và **30 điểm hội đồng** (nhóm khác chấm khi duyệt chéo Gate 2a, C6–C8). Số của nhóm được nhận nếu lệch không quá 2% so với đáp án.

| Tiêu chí | Điểm | Bằng chứng | Ghi chú |
|---|---:|---|---|
| C1 — Nhiệm vụ A: mô hình chi phí (CP1) | 20 | `src/lab13.py` in ba phép thử ĐẠT; bảng A2, A3 trong `report/team/bang_chi_phi.md` | Ba phép thử phải đạt cả ba (1,20 · 1,25 · 1,25); số A2 và A3 lệch không quá 2%. Hai dòng giả lập thiếu nhãn `simulated` bị trừ điểm |
| C2 — Nhiệm vụ B: bảng độ nhạy (CP2) | 15 | Bảng B1, B2, B3, B4 trong `report/team/bang_chi_phi.md` | B1 đủ 9 dòng, lệch không quá 2%; xếp hạng ba yếu tố đúng; B3 và B4 có số |
| C3 — Nhiệm vụ C: bảng lỗi (CP3) | 10 | `report/team/bang_loi.md` | Hai bộ nhãn độc lập, đồng thuận trong nhóm từ 80%; khớp đáp án từ 16/20 ca; bảng khắc phục đủ năm loại, mỗi dòng có cách phát hiện đo được và một vai trò phụ trách |
| C4 — Nhiệm vụ D: pilot_plan.yaml (CP4) | 15 | `report/team/pilot_plan.yaml` (phần chú thích D1, D2 và các trường) | Năm câu D1 đúng; file đọc được bằng `yaml.safe_load`, đủ trường, không còn dấu `?`; ít nhất ba luật dừng đúng mẫu NẾU – TRONG – THÌ – KHÔNG THÌ |
| C5 — Nhiệm vụ E: chỉ số, event, rủi ro, hồ sơ (CP5) | 10 | `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md` | Ba chỉ số tính thử đúng; đủ sáu event có `trace_id`; đủ hai dòng rủi ro; hồ sơ đủ bảy mục |
| C6 — Hội đồng: đề xuất khớp bằng chứng (CP5) | 10 | `report/team/ho_so_launch_v0.md`; phiếu của nhóm hội đồng | 0: mâu thuẫn với số của chính nhóm · 5: khớp nhưng bỏ qua một con số bất lợi · 10: khớp, nêu cả con số bất lợi và cách xử lý |
| C7 — Hội đồng: số giả lập và phạm vi (CP5) | 10 | Các file hồ sơ trong `report/team/`; phiếu của nhóm hội đồng | 0: không nhãn, phạm vi "mọi yêu cầu" · 5: có nhãn hoặc có thu hẹp phạm vi · 10: nhãn ở mọi số giả lập, phạm vi thu hẹp có lý do bằng số |
| C8 — Hội đồng: pilot ra được quyết định (CP4, CP5) | 10 | `report/team/pilot_plan.yaml`; phiếu của nhóm hội đồng | 0: không đối chứng hoặc thiếu cỡ mẫu · 5: đủ cỡ mẫu, luật dừng chung chung · 10: tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng |
| **Tổng điểm chính** | **100** | | |

## Bonus

Lab này không có bonus. Phần "Làm thêm nếu xong sớm" trong đề bài gốc không tính điểm.

## Quy tắc chấm

- Điểm chính tối đa: 100. Bonus ghi riêng, tối đa 10 điểm; lab này không dùng.
- Chấm trên link repo nộp trên LMS và commit cuối trước deadline.
- File hồ sơ sai tên hoặc sai chỗ (không nằm trong `report/team/`) có thể bị coi như chưa nộp.
- Số giả lập thiếu nhãn `simulated` bị trừ điểm.
- Đề xuất phải là một trong ba: Go, Go có điều kiện, No-go. Không dùng từ "production": Gate 2a chỉ duyệt kế hoạch pilot.
- Người phụ trách phải là một vai trò có quyền quyết định, không ghi "cả đội".
- Một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.
