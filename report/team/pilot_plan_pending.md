# Ghi chú chuẩn bị và bàn giao CP4 · Người 4

Trạng thái: **Chưa hoàn thành CP4**. D1, thiết kế 20 + 20, đánh đổi power, D2 và hai baseline an toàn đã có bằng chứng. File nộp vẫn còn scope, ngưỡng dừng, SLA rollback và ngày quyết định ở trạng thái `CHỜ_...`; không thay bằng số không có bằng chứng.

## Thiết kế đã có nguồn

| Nội dung | Giá trị có thể dùng | Nguồn |
| --- | --- | --- |
| Owner có quyền dừng | Giám đốc vận hành LogiX-VN | Bối cảnh và yêu cầu owner theo vai trò trong đề bài/CP4 |
| Chỉ số chính | `dong_trong_24h_khong_mo_lai_7_ngay` | Mẫu `pilot_plan.yaml` |
| Baseline | 0,70 | `docs/du_lieu_va_cong_thuc.md`, mục Số liệu dùng chung |
| MDE ban đầu | 0,05 | `docs/du_lieu_va_cong_thuc.md`; phải thay nếu Người 2 chứng minh và nhóm chấp nhận đánh đổi khác |
| Alpha / power / ICC | 0,05 / 0,80 / 0,02 | `docs/du_lieu_va_cong_thuc.md` |
| Quy mô | 40 nhân viên, 12 depot, khoảng 1.500 yêu cầu/ngày | `README.md` và tài liệu dữ liệu |
| Tỉ lệ mở lại hiện tại | 51/1.200 = 4,25% | Tính trực tiếp, chỉ đọc từ `src/logix_requests.csv`: đếm `mo_lai_trong_7_ngay == 1` / tổng số dòng |
| Tỉ lệ mở lại trong phạm vi | 39/982 = 3,97% cho `noi_dia + hang_nang` | Tính trực tiếp từ CSV và được `src/lab13.py` in ra |
| D1 +5 điểm | 1.251/nhóm; staff m=75 cần 3.103/nhóm, 42 người/nhóm; 20 staff có n_eff tối đa <1.000; 6 depot có n_eff tối đa <300 | Output `chay_nhiem_vu_d` trong `src/lab13.py` |
| Thiết kế chọn | Ngẫu nhiên theo nhân viên, 20 đối chứng + 20 can thiệp, phân tầng depot | Output D2 trong `src/lab13.py` |
| Đánh đổi +6 điểm | 859/nhóm; m >=299; DE 6,96; n_eff 859,2; power khoảng 0,64 nếu tác động thật +5 điểm | Output và công thức CP4 trong `src/lab13.py` |
| Khả thi công suất | Khoảng 7,97 ngày nếu tính toàn bộ lưu lượng; khoảng 9,74 ngày nếu ước tính theo tỷ trọng phạm vi 81,83% trong mẫu | Ước tính từ 1.500 yêu cầu/ngày và 40 nhân viên; không phải dữ liệu pilot đo thực tế |
| Rollout mẫu | 0,10 → 0,25 → 0,50, mỗi bước một tuần | Mẫu `pilot_plan.yaml` |
| Interim looks | Chỉ kiểm tra chỉ số an toàn | Mẫu `pilot_plan.yaml` |

## Khung luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ

Ba luật đã được chép vào YAML theo đúng bốn vế; các ngưỡng/cửa sổ chưa có căn cứ vẫn mang tiền tố `CHỜ_` và chưa được coi là đã chốt.

1. **An toàn:** NẾU `[chỉ số an toàn] [toán tử] [ngưỡng so với đối chứng và/hoặc trần tuyệt đối]` TRONG `[cửa sổ thời gian]` THÌ `Giám đốc vận hành [tạm dừng/tắt trợ lý trong thời hạn cụ thể và chuyển sang luồng nhân viên]` KHÔNG THÌ `[không được tăng bước rollout khi chưa đủ cửa sổ quan sát]`.
2. **Chi phí:** NẾU `chi phí mỗi việc thành công [toán tử] [ngưỡng có nguồn từ A/B]` TRONG `[số tuần liên tiếp]` THÌ `[vai trò có quyền] [thu hẹp phạm vi/giới hạn số lần chạy]` KHÔNG THÌ `[không được mở rộng phạm vi]`.
3. **Mức độ sử dụng:** NẾU `[chỉ số sử dụng] [toán tử] [ngưỡng có nguồn từ E1 hoặc baseline]` TRONG `[cửa sổ thời gian]` THÌ `Trưởng nhóm CSKH [điều tra/phỏng vấn và hành động có hạn hoàn thành]` KHÔNG THÌ `[không được chuyển bước rollout]`.

Mỗi luật cuối cùng phải có đủ: chỉ số đo được, toán tử/ngưỡng, thời hạn, hành động cụ thể, một vai trò có quyền, và việc bị cấm ở vế KHÔNG THÌ.

Lưu ý an toàn: baseline quan sát hiện tại là 4,25%, nên không được chọn một trần tuyệt đối thấp hơn mức này mà không có thiết kế so với đối chứng hoặc lý do đã được duyệt; nếu không, pilot có thể dừng ngay từ đầu. Con số này là dữ liệu quan sát, không dùng hai cột `_simulated`.

## Trường đang chờ bàn giao

| Trường / phần | Chờ ai | Bằng chứng cần nhận |
| --- | --- | --- |
| `scope` | Người 1/Người 2 | A3 và B: loại nào có lợi, giới hạn chạy và chi phí theo phạm vi |
| Ngưỡng luật chi phí | Người 1/Người 2 | Baseline và bảng độ nhạy có nhãn `simulated` nếu dùng hai cột `_simulated` |
| Ngưỡng luật sử dụng | Người 3 | Chỉ số dùng, công thức, baseline tính từ dữ liệu và event đo |
| Ngưỡng/cửa sổ luật an toàn | Nhóm trưởng + Người 3 | Baseline đã có; còn cần mức chênh so với đối chứng, trần tuyệt đối và cửa sổ được phê duyệt |
| `rollback` chi tiết | Nhóm trưởng + vai trò vận hành | Owner và luồng thay thế đã có; còn SLA hiệu lực |
| `decision_date` | Nhóm trưởng/coach | Ngày chạy và ngày quyết định thật |
| `simulated_inputs` | Người 1/Người 2 | Danh sách đầy đủ số dùng từ `_simulated` |

## Kiểm tra khi nhận đủ bàn giao

- Thay mọi trường chờ bằng giá trị có bằng chứng; không để `?` ngoài chú thích.
- Giữ ít nhất ba luật dừng đủ bốn vế.
- Chạy `yaml.safe_load`, rồi tìm dấu `?` ngoài chú thích.
- Chỉ đánh dấu CP4 hoàn thành sau khi mọi `CHỜ_...` bắt buộc đã có bằng chứng, YAML hợp lệ và luật dừng có ngưỡng/thời hạn thật.
