# Phân công nhóm 4 người · Lab 13 LogiX-VN (Gate 2a)

Mục tiêu: 4 người làm **song song**, không ai ngồi chờ ai. Chốt vai trong `TEAM.md` ngay phút đầu.

## 1. Bốn vai

| Người | Vai | Phụ trách chính | Sau giải lao |
| --- | --- | --- | --- |
| **P1** | Người viết code (lượt 1) | `src/lab13.py`: A1, A2, A3, A4, B1–B4 | Chuyển sang kiểm số |
| **P2** | Người kiểm số | Tính tay đối chiếu, điền `bang_chi_phi.md`, viết code D1 (cỡ mẫu) | Chuyển sang viết code |
| **P3** | Người gắn nhãn 1 | Nhiệm vụ C (gắn nhãn độc lập), D2, luật dừng, rollback trong `pilot_plan.yaml` | Event list trong `chi_so.md` |
| **P4** | Người gắn nhãn 2 + giữ hồ sơ | Nhiệm vụ C (gắn nhãn độc lập), điền dần `ho_so_launch_v0.md`, `TEAM.md`, `group_report.md`, kiểm tra nộp | Đóng gói và push |

**Ba nguyên tắc chống xung đột**
1. Chỉ **một người** (người viết code hiện tại) sửa `src/lab13.py`. Người khác gửi đoạn code qua chat.
2. Mỗi người chỉ sửa file của mình (cột "File" bên dưới). Mỗi người một nhánh `feat/<ten>`, commit nhỏ, `git pull` trước khi push.
3. P3 và P4 **ngồi tách nhau** và không trao đổi khi gắn nhãn C.

---

## 2. Timeline song song

```
Giờ     P1 (code)             P2 (kiểm số)            P3 (nhãn 1)             P4 (nhãn 2 + hồ sơ)
14:00   Cài môi trường, chạy thử   Cài môi trường           Đọc 20 ca lỗi (docx)    Điền TEAM.md, dựng khung hồ sơ
14:10   A1 -> A2 -> A3 -> A4  Kiểm tay A2, điền bảng A    Đọc định nghĩa 5 loại   Điền mục 1, 3 khi có số A
14:53   B1 -> B2 -> B3 -> B4  Điền bảng B, viết code D1   Chuẩn bị gắn nhãn        Điền mục 2, 7 khi có số B
15:20   ---------------- Giải lao 15 phút (đổi người viết code: P2 viết, P1 kiểm số) ----------------
15:35   (hoàn thiện B)        (hoàn thiện B)          C: gắn nhãn độc lập 8'  C: gắn nhãn độc lập 8'
15:46   Hỗ trợ chọn 5 ca      Hỗ trợ                  So nhãn, tính đồng thuận, viết quy tắc, bảng khắc phục (cả P3, P4)
16:08   D: số trong yaml      D: code cỡ mẫu D1       D2, luật dừng, rollback D: điền mục 5, 6 hồ sơ
16:36   E: tính 3 chỉ số      E2: rủi ro từ bảng B    E1: event list, kiểm chéo  Gộp hồ sơ, viết đề xuất
17:00   Duyệt chéo: cả nhóm đọc hồ sơ nhóm bạn, P4 ghi phiếu, 1 người trình bày
17:45   Báo cáo cá nhân       Báo cáo cá nhân         Báo cáo cá nhân         Báo cáo cá nhân, kiểm checklist, push
```

---

## 3. Chi tiết từng người

### P1 · Người viết code (lượt 1)

**File:** `src/lab13.py` (chỉ P1, sau giải lao là P2).

| Bước | Việc | Xong khi | Thời gian |
| --- | --- | --- | --- |
| 1 | Cài venv, `pip install -r requirements.txt`, chạy `python lab13.py` thấy NotImplementedError | In được lỗi mong đợi | 10' |
| 2 | **A1**: viết `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong` | `Ba phép thử đáp án biết trước: ĐẠT` (1,20 · 1,25 · 1,25) | 10' |
| 3 | **A2**: viết `mo_hinh()` (xem lưu ý dưới) | In đủ token, tool, xem_lai, lam_lai, tong, thanh_cong, cps | 20' |
| 4 | **A3**: gọi `mo_hinh` theo từng `loai` (4 dòng) | Có bảng 4 dòng | 5' |
| 5 | **A4**: cộng chi phí cố định 40 triệu/tháng cho phạm vi `noi_dia` + `hang_nang` (khối lượng 45.000 và một nửa) | Có 2 dòng | 5' |
| 6 | **B1**: gọi lại `mo_hinh` cho 9 kịch bản, in % thay đổi | 9 dòng, "giảm một nửa" = nửa mức "gấp đôi" | 12' |
| 7 | **B2, B3, B4**: cặp (giá token ×2 + xem lại ×2), giới hạn 1/2/3 lần kèm chi phí cả hệ thống, xem lại 100% | Có số cho từng câu | 13' |

**Lưu ý kỹ thuật cho `mo_hinh`:**
- Đọc CSV yêu cầu bằng `keep_default_na=False`.
- Tử số cộng **mọi** lần chạy (kể cả `status = loi`); mẫu số chỉ đếm `ket_qua == 'thanh_cong'`.
- Chia 1.000 token trước khi nhân giá.
- Phút `_simulated` × `luong_phut` × hệ số; kết quả phải ghi nhãn `simulated`.
- `max_lan_chay`: bỏ run có `attempt` lớn hơn giới hạn; yêu cầu có `so_lan_chay` lớn hơn giới hạn coi là `chuyen_nhan_vien` và đặt hai cột phút về 0.
- B3: chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công.

**Bàn giao:** gửi output terminal cho P2 (để điền bảng) và P4 (để điền hồ sơ).

---

### P2 · Người kiểm số

**File:** `report/team/bang_chi_phi.md`, phần code D1 (gửi cho người viết code).

| Bước | Việc | Xong khi |
| --- | --- | --- |
| 1 | Cài môi trường; trong lúc P1 viết A1, tự tính tay A1 bằng máy tính (p=0,8) | Khớp 1,20 · 1,25 · 1,25 |
| 2 | **Kiểm tay 1 con số** từ CSV (ví dụ đếm số `thanh_cong`, hoặc tổng `tool_calls` × 15 đ) rồi so với output của P1 | Lệch dưới 2% |
| 3 | Điền A1, A2, A3, A4 vào `bang_chi_phi.md`; hai dòng simulated có nhãn `simulated` | Bảng A2 đủ 9 dòng, A3 đủ 4 dòng |
| 4 | Điền B1 (9 dòng), B2 (xếp hạng 3 yếu tố), B3, B4; mỗi câu trả lời ≤ 3 dòng và có số | Không còn `...` |
| 5 | **Viết code D1** (làm trong lúc chờ): hàm cỡ mẫu 2 tỉ lệ (p1=0,70, p2=0,75, alpha 0,05, power 0,8) bằng `statsmodels` hoặc `NormalDist` | Ra số cho 5 câu a–e |
| 6 | Sau giải lao: nhận `lab13.py` làm người viết code, thêm phần D1 và `mo_lai_trong_7_ngay` trung bình | Chạy hết từ đầu đến cuối |

**Năm câu D1 cần tính:**
- a) Cỡ mẫu mỗi nhóm, chia theo yêu cầu.
- b) Theo nhân viên, m = 75: hệ số thiết kế = 1 + (m − 1) × ICC; cỡ mẫu nhân với hệ số này; đủ người không (tổng 40 nhân viên)?
- c) 20 nhân viên mỗi nhóm: cỡ mẫu hiệu dụng tối đa = 20 ÷ ICC; có ≥ cỡ mẫu a không?
- d) 6 depot mỗi nhóm: tối đa = 6 ÷ ICC.
- e) Mức chênh 6 điểm: giải m sao cho 20m ÷ (1 + (m − 1) × 0,02) ≥ cỡ mẫu mỗi nhóm.

---

### P3 · Người gắn nhãn 1

**File:** `report/team/bang_loi.md` (phần nhãn người 1), `report/team/pilot_plan.yaml` (phần chữ), phần event list trong `report/team/chi_so.md`.

| Bước | Việc | Xong khi | Thời gian |
| --- | --- | --- | --- |
| 1 | 14:10–15:35: đọc mục "Hai mươi ca lỗi" trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và định nghĩa 5 loại PAIR | Hiểu: gắn theo **nguyên nhân gốc**; "hệ thống" khác "ngầm" ở chỗ lỗi đã lộ ra hay chưa | 20' (rảnh) |
| 2 | 15:35: gắn nhãn 20 ca **độc lập**, **không trao đổi với P4** | Điền cột "Nhãn người 1" | 8' |
| 3 | So nhãn với P4, tính đồng thuận (mục tiêu ≥ 16/20) | Điền cột "Trùng?", tỉ lệ % | 3' |
| 4 | Với ca không trùng: thống nhất nhãn, mỗi ca một câu quy tắc phân biệt | Điền "Nhãn thống nhất" và mục quy tắc | 5' |
| 5 | **Bảng khắc phục 5 ca, mỗi loại một ca**: phát hiện bằng gì (event, ngưỡng, tần suất), khắc phục thế nào, ai phụ trách (một vai trò, không ghi "cả đội") | 5 dòng đủ 5 loại | 14' |
| 6 | 16:08: nhận số D1 từ P2, điền **D2 (5 câu)**, owner, scope, rollback, `decision_date` | Không còn dấu `?` | 15' |
| 7 | **Ba luật dừng** đúng mẫu "NẾU … TRONG … THÌ … KHÔNG THÌ …" (an toàn, chi phí, sử dụng), có ngưỡng, thời hạn và tên người có quyền dừng | 3 dòng đủ 4 vế | 10' |
| 8 | 16:36: danh sách ≥ 6 event, mỗi event có `trace_id` | Bảng 6 dòng, ghi event nào dùng cho chỉ số nào | 15' |

**Lưu ý luật dừng:** tính `mo_lai_trong_7_ngay` hiện tại trước (P2 cung cấp). Đừng đặt ngưỡng tuyệt đối thấp hơn mức hiện tại, nếu không pilot dừng ngay tuần đầu. Nên so với nhóm đối chứng kèm trần tuyệt đối.

**Lưu ý chọn cách chia:** theo cỡ mẫu D1, chia theo yêu cầu thì dễ đủ mẫu nhưng nhân viên vừa dùng vừa không dùng (tràn tác động); chia theo depot chỉ có 6 cụm (dưới 20). Chia theo nhân viên là phương án cân bằng nhất, nhưng phải ghi rõ đánh đổi (mức chênh 6 điểm thay vì 5) trong file.

---

### P4 · Người gắn nhãn 2 + giữ hồ sơ

**File:** `TEAM.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/phieu_cham.md`, phần nhãn người 2 trong `bang_loi.md`.

| Bước | Việc | Xong khi |
| --- | --- | --- |
| 1 | 14:00: điền `TEAM.md` (tên nhóm, lớp L3B, thành viên, vai) | Đủ 4 dòng |
| 2 | Đổi tên repo theo mẫu `K5-L3B-DAY13-TenNhom-LaunchEconomics`, mời các thành viên | Mọi người clone được |
| 3 | Dựng khung `ho_so_launch_v0.md` với bảy mục, mỗi mục có một vai trò phụ trách | Không ghi "cả đội" |
| 4 | Khi P1 có số A: điền mục 1 (chi phí mỗi việc thành công), mục 3 (so với 12.000 đ, nhớ cả phần chuyển nhân viên) | Trạng thái: **Giả lập** |
| 5 | Khi có số B: mục 2 (ba yếu tố nhạy nhất), mục 7 (rủi ro) | Có số và nhãn |
| 6 | 15:35: gắn nhãn 20 ca **độc lập** (ngồi tách P3), sau đó cùng P3 so nhãn | Điền cột "Nhãn người 2" |
| 7 | Điền mục 4 (3 chỉ số), mục 5 (bảng lỗi), mục 6 (pilot plan) từ kết quả của P1–P3 | Mỗi mục: con số, trạng thái, người phụ trách |
| 8 | Viết **dòng đề xuất cuối**: một trong Go / Go có điều kiện / No-go. Đề xuất phải khớp số của chính nhóm và nêu cả con số bất lợi | Có lý do bằng số |
| 9 | 17:00: ghi `phieu_cham.md` khi chấm nhóm khác | 3 tiêu chí có điểm và lý do có số |
| 10 | 17:45: chạy checklist cuối (mục 4 bên dưới), push | Repo mở được |

**Cột trạng thái chỉ được là:** `Xong, có bằng chứng` · `Chưa` · `Giả lập`. Mục nào dựa trên cột `_simulated` ghi `Giả lập`.

---

## 4. Checklist chung trước khi nộp (P4 chủ trì)

- [ ] `cd src && python lab13.py` chạy hết, in `Ba phép thử đáp án biết trước: ĐẠT`
- [ ] Sáu file trong `report/team/` đủ tên: `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`, `phieu_cham.md`
- [ ] Mọi số tính từ cột `_simulated` có nhãn `simulated`
- [ ] `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"` chạy không lỗi
- [ ] `grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'` không in gì
- [ ] Ít nhất 3 luật dừng đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ
- [ ] Mỗi mục hồ sơ có người phụ trách là một vai trò (không ghi "cả đội")
- [ ] Đề xuất là một trong ba: Go, Go có điều kiện, No-go
- [ ] `grep -rni production ../report/team` không in gì
- [ ] `TEAM.md` đã điền; `group_report.md` đã điền
- [ ] Mỗi người một file `report/team/MSSV_HoTen.md` (copy từ mẫu, giữ nguyên mẫu)
- [ ] Không commit `.venv/`, `.env`
- [ ] **Mỗi thành viên tự nộp link repo trên LMS** (ai không nộp thì không có điểm), trước 23h59 GMT+7 ngày lab

## 5. Điểm dễ mất (nhắc cả nhóm)

1. Chi phí mỗi việc thành công chỉ gấp 1–2 lần hoá đơn token nghĩa là **quên giờ nhân viên**.
2. Không chia cho 1.000 token trước khi nhân giá.
3. Gắn nhãn C sau khi đã bàn với nhau (mất tính độc lập).
4. Ghi người phụ trách là "cả đội".
5. Đặt ngưỡng dừng mà chưa nhìn tỉ lệ `mo_lai_trong_7_ngay` hiện tại.
6. Viết "trợ lý đã nâng chỉ số" (đợt chạy thử không có nhóm đối chứng; chỉ được viết "chỉ số trong đợt chạy thử là …").
7. Dùng từ "production" (Gate 2a chỉ duyệt kế hoạch pilot).
8. Đề xuất Go nhưng bỏ qua con số bất lợi. No-go có lý do bằng số được điểm cao hơn.

## 6. Cách đối chiếu số khi đã tự làm xong

Chỉ mở sau khi nhóm đã có số của mình: `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` có số tham chiếu cho A–E. Số của nhóm được nhận nếu lệch không quá 2%.
