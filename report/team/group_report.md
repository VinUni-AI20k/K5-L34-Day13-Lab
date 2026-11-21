# Báo cáo nhóm

## 1. Thông tin nhóm

- Tên nhóm: NguyenTuanBach
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Trả lời bốn câu cho trợ lý hoàn phí của LogiX-VN: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào. Dữ liệu là mẫu 1.200 yêu cầu / 1.624 lần chạy, toàn bộ giả lập; mọi số từ cột `_simulated` ghi nhãn simulated.

## 3. Giải pháp

- A, B: `src/lab13.py` (mô hình chi phí từ trace, độ nhạy) → `bang_chi_phi.md`.
- C: gắn nhãn 20 ca lỗi theo Google PAIR và bảng khắc phục 5 ca → `bang_loi.md`.
- D: cỡ mẫu và `pilot_plan.yaml` (chia theo nhân viên 20 + 20, ba luật dừng).
- E: `chi_so.md`, `ho_so_launch_v0.md`.

## 4. Kết quả

- Chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3× hoá đơn token + tool; cả hệ thống 0,49× của 12.000 đ [simulated].
- Phạm vi pilot: noi_dia (0,22×) và hang_nang (0,69×); loại quoc_te (1,88×, thành công 27,3%) và doi_tac (0,85×).
- Yếu tố nhạy nhất: số ca làm lại (±51,8%), xem lại (±40,7%), lương (+23,1%).
- Đề xuất: **Go có điều kiện**, với mức chênh 6 điểm (power 0,64 nếu tác động thật 5 điểm).
- Duyệt chéo: xem `phieu_cham.md` (phiếu chấm Gate 2a theo ba tiêu chí, 25/30).

## 5. Khó khăn và cách xử lý

Python trên máy chưa có pandas/statsmodels: cài bằng `pip install -r src/requirements.txt`. Không cách chia theo cụm nào đủ mẫu cho mức chênh 5 điểm với 40 nhân viên: chấp nhận mức chênh 6 điểm và ghi rõ đánh đổi.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

Phút xem lại và làm lại là simulated; thay bằng phút đo thật sau tuần 1. Nhiệm vụ C: nhãn gắn theo nguyên nhân gốc; các ca không trùng đã có quy tắc phân biệt trong ``bang_loi.md``. Mẫu chỉ có 20 nhân viên và 6 depot.

## 8. Tài liệu tham khảo

Erol và cộng sự, *Cost-of-Pass* (arxiv.org/abs/2504.13359); Google PAIR, *People + AI Guidebook*; tài liệu statsmodels `NormalIndPower`; `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` để đối chiếu số.
