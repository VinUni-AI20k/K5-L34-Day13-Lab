# Phân công Lab 13 · GroupN

Repo nhóm: https://github.com/buiductuan2884-max/K5-L34-Day13-GroupN-LaunchEconomics (sẽ đổi tên thành `K5-L3B-DAY13-GroupN-LaunchEconomics`; link cũ GitHub tự chuyển hướng).

Hạn nộp: **23h59 GMT+7 ngày lab**. Mỗi người tự nộp link repo nhóm trên LMS, ai không nộp thì không có điểm.

## Ai làm gì

| Người | Vai trong lab | File phụ trách | Nhiệm vụ |
| --- | --- | --- | --- |
| MinhNGD76 | Người viết code | `src/lab13.py` (phần A, B), `report/team/bang_chi_phi.md` | A, B |
| NguyenGL03 | Người kiểm số | `src/lab13.py` (phần D1, sau khi A đã merge), `report/team/pilot_plan.yaml` | Tính tay đối chiếu A2, D |
| NMCcg | Người gắn nhãn 1 | `report/team/bang_loi.md`, `report/team/phieu_cham.md` | C, duyệt chéo |
| buiductuan2884-max (Tuấn) | Người gắn nhãn 2, kiêm giữ hồ sơ | `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `TEAM.md`, `report/team/group_report.md`; merge PR | C (nhãn 2), E |

Mỗi người thêm: báo cáo cá nhân `report/team/MSSV_HoTenKhongDau.md` (copy từ `MSSV_HoTen.md`, giữ nguyên file mẫu), ghi công cụ AI đã dùng và cách tự kiểm tra.

## Việc cụ thể từng người

### MinhNGD76 · Người viết code (A, B)

1. Cài môi trường theo `src/README.md`, chạy `python lab13.py`.
2. Viết ba hàm A1 cho tới khi in `Ba phép thử đáp án biết trước: ĐẠT` (1,20 · 1,25 · 1,25).
3. Viết `mo_hinh(...)` (A2), gọi lại theo từng `loai` (A3), cộng chi phí cố định 40 triệu cho `noi_dia` + `hang_nang` (A4).
4. Viết 9 kịch bản B1, cặp B2, giới hạn 1/2/3 lần B3, xem lại 100% B4 (dòng `TODO CP2`).
5. Chép số vào `bang_chi_phi.md`. Mọi số từ cột `_simulated` ghi `[simulated]`.
6. Tự đối chiếu với `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, lệch không quá 2%.

**Làm xong A thì mở PR ngay** (chưa cần B), để NguyenGL03 và Tuấn có số dùng.

### NguyenGL03 · Người kiểm số (D)

1. Tính tay một con số A2 để đối chiếu với code của MinhNGD76: chi phí mỗi việc thành công = (token + tool + xem lại + làm lại) / số việc thành công. Ghi cách tính vào báo cáo cá nhân.
2. Sau khi PR phần A được merge: `git pull` rồi mới viết D1 ở dòng `TODO CP4` trong `src/lab13.py` (để không đè code A, B).
3. Tính 5 câu D1 (a–e), trả lời 5 câu D2, tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại trước khi đặt luật an toàn.
4. Điền hết dấu `?` trong `pilot_plan.yaml`, ít nhất 3 luật dừng (an toàn, chi phí, mức dùng) đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ.
5. Tự kiểm tra (trong `src/`):
   - `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml', encoding='utf-8'))"` không lỗi.
   - Ngoài dòng chú thích không còn dấu `?`.

### NMCcg · Người gắn nhãn 1 (C) và duyệt chéo

1. Đọc 20 ca trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, mục "Hai mươi ca lỗi".
2. **Tự gắn nhãn cả 20 ca trong 8 phút, không trao đổi với Tuấn, không xem bảng nhãn tham khảo trong `docs/`.** Gửi bộ nhãn cho Tuấn qua tin nhắn nhóm (để có giờ gửi làm bằng chứng).
3. Nhận bộ nhãn của Tuấn, điền cả hai cột vào `bang_loi.md`, tính tỉ lệ đồng thuận (cần ≥ 16/20). Ca nào lệch: hai người thống nhất, ghi một câu quy tắc phân biệt.
4. Chọn 5 ca, mỗi loại một ca, điền bảng khắc phục: cách phát hiện đo được (event, ngưỡng, tần suất) và một vai trò phụ trách (không ghi "cả đội").
5. Duyệt chéo: chấm hồ sơ nhóm được phân công vào `phieu_cham.md`.

### Tuấn · Người gắn nhãn 2, kiêm giữ hồ sơ (E)

1. Gắn nhãn 20 ca độc lập (như bước 2 của NMCcg), gửi cho NMCcg.
2. `chi_so.md`: tính thử 3 chỉ số, thêm 1 chỉ số dùng và 1 chỉ số an toàn tự đề xuất, ≥ 6 event có `trace_id`, ≥ 2 dòng rủi ro kinh tế lấy số từ bảng độ nhạy.
3. `ho_so_launch_v0.md`: đủ 7 mục, mỗi mục có con số, trạng thái, một vai trò phụ trách; dòng cuối là Go / Go có điều kiện / No-go.
4. `TEAM.md`, `group_report.md`; review và merge PR của mọi người.

## Thứ tự phụ thuộc

```
MinhNGD76: A ──PR──► NguyenGL03: D1 code ──PR──┐
           └─ B ─PR──────────────────────────► Tuấn: chi_so, ho_so ──► nộp
NMCcg + Tuấn: gắn nhãn độc lập ──► NMCcg: bang_loi ──PR──┘
```

Hồ sơ của Tuấn cần số từ cả ba người kia, nên mọi người mở PR sớm nhất có thể.

## Cách làm với git

1. Clone repo nhóm (không làm trên repo đề bài):
   ```
   git clone https://github.com/buiductuan2884-max/K5-L34-Day13-GroupN-LaunchEconomics.git
   ```
2. Tạo nhánh riêng: `git checkout -b ten-ban/phan-viec` (ví dụ `minh/cp1-chi-phi`).
3. Chỉ sửa file của mình. Commit, push nhánh, mở Pull Request vào `main`. Tuấn review và merge.
4. Trước khi làm tiếp sau mỗi lần merge: `git checkout main && git pull`.
5. Không force-push, không commit `.venv/` hay `.env`, không sửa hai file CSV, không dùng từ "production" trong hồ sơ.

## Gửi cho Tuấn để điền `TEAM.md`

Họ tên, MSSV, GitHub, và phần việc đã làm (kèm link PR/commit làm bằng chứng).
