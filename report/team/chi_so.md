# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E

Trần Việt Tiến — 2A202603394 · Nhóm VOI · L3A · Nhiệm vụ E. Dữ liệu của lab là giả lập; số dùng phút nhân viên được ghi nhãn **simulated**.

## E1 · Đặc tả chỉ số

Đơn vị tính là yêu cầu, mỗi `request_id` được đếm một lần. Ba chỉ số tính trên toàn bộ mẫu chạy thử gồm 1.200 yêu cầu.

| Loại | Chỉ số | Công thức | Kết quả |
| --- | --- | --- | --- |
| Chính | Tỉ lệ đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu có `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0` / tổng yêu cầu | 994 / 1.200 = **82,83%** |
| Dùng | Tỉ lệ bỏ qua gợi ý | Trong các yêu cầu có `duoc_xem_lai = 1`, đếm `quyet_dinh_xem_lai` thuộc `sua`, `bo` / số yêu cầu được xem lại | 48 / 177 = **27,12%** |
| An toàn | Tỉ lệ mở lại trong 7 ngày, dùng làm chỉ báo lỗi lọt đến khách theo đề bài | Số yêu cầu có `mo_lai_trong_7_ngay = 1` / tổng yêu cầu | 51 / 1.200 = **4,25%** |
| Dùng, đề xuất thêm | Tỉ lệ sử dụng trợ lý trong phạm vi pilot | Số `request_id` hợp lệ thuộc nhánh can thiệp có ít nhất một `agent_suggestion_shown` / tổng `request_id` hợp lệ thuộc nhánh can thiệp | Chờ log pilot |
| An toàn, đề xuất thêm | Tỉ lệ hoàn sai tiền qua kiểm tra mẫu | Số yêu cầu trong mẫu kiểm toán có tổng tiền thực hoàn khác số tiền đúng / tổng yêu cầu hoàn tiền đã kiểm toán | Chờ kiểm toán pilot |

Chỉ số trong đợt chạy thử là 82,83%; dữ liệu thiếu nhóm đối chứng để xác định mức tác động của trợ lý. Baseline 70% dùng cho bài tính cỡ mẫu là giả định của nhiệm vụ D.

Tỉ lệ mở lại trong phạm vi `noi_dia` + `hang_nang` là 39 / 982 = **3,97%**; tỉ lệ bỏ qua gợi ý cùng phạm vi là 27 / 128 = **21,09%**. Ngưỡng an toàn của pilot đối chiếu phạm vi và nhóm đối chứng cùng thời gian; mỗi ca mở lại cần được điều tra nguyên nhân.

### Cách tái tính từ CSV

Dùng thư viện chuẩn Python, chạy từ thư mục gốc repo. Đây là cách tính độc lập để kiểm tra E1 và bàn giao cho người phụ trách code.

```python
import csv
from pathlib import Path

with Path('src/logix_requests.csv').open(encoding='utf-8', newline='') as file:
    requests = list(csv.DictReader(file))

closed_without_reopen = sum(
    row['dong_trong_24h'] == '1' and row['mo_lai_trong_7_ngay'] == '0'
    for row in requests
)
reviewed = [row for row in requests if row['duoc_xem_lai'] == '1']
overridden = sum(row['quyet_dinh_xem_lai'] in ('sua', 'bo') for row in reviewed)
reopened = sum(row['mo_lai_trong_7_ngay'] == '1' for row in requests)

print(closed_without_reopen, len(requests), closed_without_reopen / len(requests))
print(overridden, len(reviewed), overridden / len(reviewed))
print(reopened, len(requests), reopened / len(requests))
```

### Danh sách event đề xuất cho pilot

Mọi event có `event_id`, `event_time`, `request_id`, `trace_id`, `staff_id`, `depot`, `arm` và `loai`. `event_id` dùng khử bản ghi trùng; `arm` được lưu từ lúc phân nhóm để phân tích theo phân nhóm ban đầu.

| Event | Ai tạo | Thuộc tính bổ sung | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống tiếp nhận | `created_at`, `eligible`, `assignment_unit_id` | Khi nhận yêu cầu, kể cả nhánh đối chứng |
| `input_validation_failed` | Giao diện nhập liệu | `field`, `error_code`, `entered_code_type` | Khi kiểm tra đầu vào thất bại |
| `refund_confirmation_sent` | Dịch vụ thông báo | `transaction_id`, `message_id`, `delivery_status` | Khi gửi xác nhận đã hoàn |
| `agent_run_completed` | Agent | `run_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `model_version` | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `suggestion_id`, `run_id`, `proposed_amount_vnd` | Khi gợi ý hiển thị thành công |
| `staff_review_decision` | Giao diện nhân viên | `suggestion_id`, `decision` thuộc giu/sua/bo, `review_minutes`, `is_final` | Khi chốt quyết định xem lại |
| `staff_rework_completed` | Hệ thống tác nghiệp | `rework_minutes`, `reason` | Khi nhân viên hoàn tất làm lại |
| `refund_ledger_write` | Dịch vụ sổ cái | `transaction_id`, `idempotency_key`, `amount_vnd`, `result` | Sau mỗi lần ghi tiền hoàn |
| `handoff_to_staff` | Agent | `reason`, `attempt`, `summary` | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at` | Mỗi lần đóng yêu cầu |
| `ticket_reopened` | Hệ thống ticket | `reopened_at`, `reason` | Mỗi lần yêu cầu được mở lại |
| `audit_sample_checked` | Công cụ kiểm toán của kế toán | `audit_id`, `total_refunded_vnd`, `correct_amount_vnd`, `policy_version`, `sampling_probability` | Hằng tuần, sau đối soát sổ cái |

Pilot cấp một `trace_id` gốc khi tiếp nhận cho cả hai nhánh. Mỗi lượt chạy thêm `run_id` và liên kết tới `trace_id` gốc; khi nối CSV hiện có, dùng `request_id` vì `trace_id` trong log chạy hiện tại thay đổi theo lượt chạy.

### Đối chiếu event với chỉ số

| Chỉ số | Event và cách tổng hợp |
| --- | --- |
| Đóng trong 24 giờ, không mở lại 7 ngày | `refund_request_created` nối `ticket_closed`, `ticket_reopened` theo `request_id`; kiểm tra lần đóng đầu trong 24 giờ từ lúc nhận và không mở lại trong 7 ngày sau đóng |
| Bỏ qua gợi ý | `staff_review_decision`; mỗi yêu cầu lấy quyết định cuối có `is_final = true`, tử số là sua/bo, mẫu số là tất cả yêu cầu đã chốt xem lại |
| Mở lại trong 7 ngày | `refund_request_created`, `ticket_closed`, `ticket_reopened`; đếm yêu cầu có mở lại trong cửa sổ 7 ngày, chia tổng yêu cầu cùng đoàn hệ đã đủ thời gian theo dõi |
| Sử dụng trợ lý | `refund_request_created` lọc `eligible = true`, `arm = intervention`; nối `agent_suggestion_shown`, đếm yêu cầu duy nhất |
| Hoàn sai tiền qua kiểm toán | `audit_sample_checked` nối `refund_ledger_write`; so tổng tiền thực hoàn với số tiền đúng, đếm mỗi yêu cầu một lần trong mẫu ngẫu nhiên |

Quy ước thời gian trên là đề xuất cần chốt với Người 4 trước pilot vì CSV chỉ cung cấp cờ tổng hợp. Chỉ báo cáo kết quả sau khi đủ 24 giờ xử lý và 7 ngày theo dõi sau đóng; ghi riêng yêu cầu chưa đủ cửa sổ. Đối chứng được theo dõi cùng thời gian. Mẫu kiểm toán lấy ngẫu nhiên từ các yêu cầu đã hoàn tiền của từng nhánh, ghi xác suất chọn nếu phân tầng.

## E2 · Rủi ro kinh tế

Số liệu lấy từ bảng B1 và B4 trong [bang_chi_phi.md](bang_chi_phi.md), đối chiếu với `src/lab13_b.py` và tính kiểm tra từ hai CSV. Phạm vi B1 là toàn mẫu; B4 là nội địa và hàng nặng. Ngưỡng và hành động trong bảng dưới là đề xuất quản trị, cần chủ pilot duyệt trước khi chạy.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi, ngưỡng đề xuất | Hành động đề xuất | Người phụ trách |
| --- | --- | --- | --- | --- |
| Khối lượng làm lại tăng gấp đôi | (4.373.585,132 + 2.264.000) / 978 = **6.787 đ/việc, +51,8%, simulated** | Phút làm lại / yêu cầu vượt 2 × mốc cùng phạm vi trong 1 tuần; mốc phạm vi pilot là 780 / 982 = 0,794 phút/yêu cầu simulated | PM rà 20 trace làm lại trong 3 ngày, thu hẹp về noi_dia trong lúc sửa lỗi | PM trợ lý hoàn phí |
| Khối lượng xem lại tăng gấp đôi | (4.373.585,132 + 1.780.000) / 978 = **6.292 đ/việc, +40,7%, simulated** | Phút xem lại / yêu cầu vượt 2 × mốc cùng phạm vi trong 1 tuần; mốc phạm vi pilot là 644 / 982 = 0,656 phút/yêu cầu simulated | Trưởng nhóm đo thời gian thực, rà 20 quyết định xem lại và đề xuất cách giảm thao tác | Trưởng nhóm CSKH |
| Phải xem lại 100% trong phạm vi nội địa và hàng nặng | (224.513,274 + 948 × 5 × 2.000 + 48 × 9 × 2.000) / 900 = **11.743 đ/việc, simulated**; dùng 15,3 phút làm lại ra **12.415 đ/việc, simulated** | Tỉ lệ xem lại vẫn trên 50% cuối bước rollout 0,25; đo lại phút thực tế theo tuần | Kiểm tra an toàn trước khi giảm xem lại theo bậc; nếu tiếp tục vượt ngân sách thì thu hẹp phạm vi và trình lại Gate 2a | Giám đốc vận hành |

B4 tính trên 948 yêu cầu có lượt chạy ok và 900 việc thành công, giả định xem lại 5 phút/lần. Hai kịch bản làm lại là 9 phút và 15,3 phút/ca theo bảng B; số tiền được làm tròn đến đồng, trước cố định và phần nhân viên xử lý yêu cầu thất bại.

## Rà soát bài nộp

- Đã đối chiếu ba chỉ số với CSV; các số rủi ro khớp bảng B1/B4. Code chạy hết A1–A4, B1–B4, D1; ba phép thử A1 đạt. YAML đọc hợp lệ, có ba luật dừng.
- C đã có 20 nhãn Người 3 và khắc phục năm loại. Báo cáo Người 4 ghi đã xong nhãn, nhưng bảng chung còn chờ bộ nhãn thứ hai và tỉ lệ đồng thuận.
- Hồ sơ E đủ bảy mục, có vai trò và điều kiện. Đề xuất Go có điều kiện và mốc kiểm tra 23/11/2026 cần nhóm xác nhận; ngày quyết định pilot theo D là 05/01/2027.
- Trước nộp, kiểm tra chạy trên máy thứ hai, cập nhật báo cáo nhóm và phiếu duyệt chéo thực tế, xác nhận giữ file mẫu MSSV_HoTen.md đang bị xóa cục bộ. Mỗi thành viên nộp link repo trên LMS trước 23h59 GMT+7 ngày lab.

## Nội dung trình bày Gate 2a

Nhóm VOI đề xuất Go có điều kiện cho pilot nội địa và hàng nặng. Ba chỉ số toàn mẫu là 82,83% đóng đúng hạn và không mở lại, 27,12% sửa hoặc bỏ gợi ý và 4,25% mở lại; pilot sẽ đo riêng hai nhánh để đánh giá tác động.

Chi phí trong phạm vi là 3.414 đ/việc simulated trước cố định, nhưng xem lại 100% có thể lên 12.415 đ/việc simulated. Pilot chia theo nhân viên với 20 cụm mỗi nhánh, chấp nhận mức chênh cần phát hiện 6 điểm; nếu tác động thật chỉ 5 điểm thì power khoảng 0,64.

Trước khi bật, nhóm cần đưa bộ nhãn riêng của Người 4 vào bảng chung và tính đồng thuận, kiểm thử đối soát hoàn trùng và chốt lịch đo đủ mẫu. Code A/B/D1 đã chạy qua trong lần rà soát này. Quyết định cuối và các điều kiện cần được chủ pilot ký duyệt; ngày quyết định dự kiến theo D là 05/01/2027.

Nguồn nội bộ gồm hai CSV trong `src/`, [bảng chi phí A/B](bang_chi_phi.md), [pilot plan D](pilot_plan.yaml), `src/lab13_b.py`, `src/lab13_d.py`, [báo cáo Người 4](2A202603370_PhamVietHung.md), hướng dẫn chi tiết A–E, RUBRIC.md và SUBMISSION.md.
