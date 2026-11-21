# Phân công Lab 13 cho nhóm 4 người

Điền tên thành viên tương ứng với Người 1–4 trong `TEAM.md`. Phân công theo file; mỗi file chỉ có một người trực tiếp sửa tại một thời điểm.

## 1. Phần việc và file phụ trách

Các file báo cáo trong bảng nằm trong `report/team/`, trừ đường dẫn được ghi đầy đủ.

| Thành viên | Công việc | File trực tiếp sửa |
| --- | --- | --- |
| **Người 1 — Code đầu buổi, chỉ số cuối buổi** | CP1: viết A1–A4. CP2: viết B1–B4, gửi kết quả cho Người 2 kiểm tra và điền bảng. Sau giải lao bàn giao code cho Người 2. CP5: tính ba chỉ số, đề xuất thêm một chỉ số dùng và một chỉ số an toàn, liệt kê ít nhất sáu event có `trace_id`, viết ít nhất hai rủi ro kinh tế lấy số từ bảng độ nhạy. | `src/lab13.py` **trước bàn giao**; `chi_so.md` |
| **Người 2 — Kiểm số, code sau giải lao, pilot** | CP1–CP2: tính tay đối chiếu ít nhất một kết quả, điền bảng A và B cùng các câu trả lời. Sau giải lao tiếp quản code, tự tính lại ít nhất một kết quả chi phí, hoàn thiện CP2 nếu còn thiếu. CP4: viết phần tính D1, cùng nhóm thống nhất D2 và kế hoạch pilot; điền YAML. | `bang_chi_phi.md`; `src/lab13.py` **sau bàn giao**; `pilot_plan.yaml` |
| **Người 3 — Gắn nhãn 1, bảng lỗi, thư ký hội đồng** | CP3: gắn độc lập đủ 20 ca; so với Người 4, tính đồng thuận, ghi quy tắc cho ca bất đồng và bảng khắc phục năm ca đủ năm loại. CP5: ghi phiếu nhóm mình chấm nhóm khác theo thảo luận và bằng chứng thực tế. | `bang_loi.md`; `phieu_cham.md` |
| **Người 4 — Gắn nhãn 2, giữ hồ sơ, tổng hợp nộp** | Điền hồ sơ launch dần từ đầu buổi. CP3: gắn độc lập đủ 20 ca. CP5: tổng hợp bảy mục, ghi đề xuất cuối theo quyết định nhóm. Thu thập thông tin và đóng góp, viết báo cáo nhóm, phụ trách merge và kiểm tra bản nộp. | `ho_so_launch_v0.md`; `group_report.md`; `TEAM.md` |

Mỗi người tự copy `report/team/MSSV_HoTen.md` thành báo cáo cá nhân có tên riêng, ví dụ `report/team/20241234_NguyenVanAn.md`. Giữ nguyên file mẫu. Mỗi báo cáo ghi phần việc, bằng chứng, công cụ AI đã dùng và cách tự kiểm tra.

## 2. Thứ tự phối hợp

Giờ dưới đây theo lịch mẫu trong repo; nếu lớp học giờ khác, giữ thứ tự và theo thông báo của coach.

| Giai đoạn | Người 1 | Người 2 | Người 3 | Người 4 |
| --- | --- | --- | --- | --- |
| CP1 — 14:10–14:53 | Viết A1–A4 | Kiểm số, điền bảng A | Đọc yêu cầu, kiểm tra điều kiện hoàn thành | Điền `TEAM.md`, dựng khung hồ sơ |
| CP2 — 14:53–15:20 | Viết B1–B4 | Kiểm số, điền bảng B | Soát các câu trả lời theo yêu cầu đề | Cập nhật hồ sơ từ kết quả đã kiểm |
| Giải lao — 15:20–15:35 | Commit, merge và bàn giao code | Pull bản đã merge, tiếp nhận code | Chuẩn bị gắn nhãn | Chuẩn bị gắn nhãn |
| CP3 — 15:35–16:08 | Hỗ trợ kiểm kết quả CP2, chuẩn bị chỉ số | Tự tính lại chi phí, hoàn thiện CP2 | Gắn độc lập 20 ca trong 8 phút; sau đó tổng hợp bảng lỗi | Gắn độc lập 20 ca trong 8 phút; sau đó cùng đối chiếu |
| CP4 — 16:08–16:36 | Kiểm tra chi phí và chuẩn bị `chi_so.md` | Tính D1, ghi D2 và hoàn thiện YAML | Góp ý an toàn, luật dừng từ bảng lỗi | Cập nhật hồ sơ, cùng nhóm chốt thiết kế pilot |
| CP5 — 16:36–17:00 | Hoàn thiện chỉ số, event, rủi ro | Soát số liệu và pilot | Soát bảng lỗi, chuẩn bị duyệt chéo | Hoàn thiện hồ sơ một trang, đủ bảy mục để gửi hội đồng |
| Duyệt chéo — 17:00–17:45 | Giải thích chỉ số và rủi ro | Giải thích chi phí và cỡ mẫu | Ghi phiếu chấm nhóm khác | Điều phối trình bày, ghi nhận góp ý |
| Đóng gói — 17:45–18:00 | Hoàn thiện báo cáo cá nhân | Hoàn thiện báo cáo cá nhân | Hoàn thiện báo cáo cá nhân | Tổng hợp báo cáo nhóm, hoàn thiện báo cáo cá nhân, kiểm tra merge và push |

## 3. Quy tắc tránh conflict

1. **Một file, một người ghi.** Thành viên khác đọc, review và gửi góp ý để người phụ trách nhập. Không tự sửa file ngoài phạm vi được giao.
2. **Không sửa đồng thời `src/lab13.py`.** Trước giải lao Người 1 phụ trách; sau bàn giao Người 2 phụ trách. Repo yêu cầu đổi người viết code sau giải lao để ít nhất hai người tự tay tính được chi phí.
3. **Bàn giao code bằng bản đã merge:** Người 1 commit phần hiện có, ghi rõ phần hoàn thành và phần còn thiếu; Người 4 merge; Người 2 pull bản mới rồi mới tiếp tục sửa. Người 1 dừng sửa file này sau bàn giao.
4. **Mỗi người một branch**, gợi ý `nguoi-1`, `nguoi-2`, `nguoi-3`, `nguoi-4`. Tạo branch từ bản `main` mới nhất; chỉ stage và commit các file được giao, tránh `git add .`.
5. **Người 4 merge lần lượt.** Khi cần chuyển quyền sửa một file, phải commit và merge phần trước, rồi người nhận cập nhật bản mới trước khi sửa.
6. **Hai bộ nhãn CP3 phải độc lập.** Người 3 và Người 4 ghi riêng trên giấy hoặc file riêng, không xem nhãn của nhau trước khi hoàn thành. Sau khi so, Người 3 nhập nguyên hai bộ nhãn ban đầu và kết quả thống nhất vào `bang_loi.md`; không sửa lại bộ nhãn độc lập.
7. **Số liệu có nguồn thống nhất.** Kết quả từ code do Người 2 kiểm tra và ghi vào bảng chi phí hoặc kế hoạch pilot; Người 1 và Người 4 dùng bản đã kiểm cho chỉ số, rủi ro và hồ sơ. Nếu đổi số, báo cho các thành viên đang dùng số đó.
8. **Giữ nguyên dữ liệu và bản khởi đầu.** Không sửa `src/logix_runs.csv`, `src/logix_requests.csv` và `src/lab13_starter.py`. Không force-push hoặc xóa commit.

## 4. CP5 có cần làm chung trên một máy không?

Theo hướng dẫn repo, CP5 là phần cả nhóm tổng hợp và duyệt chéo; không có yêu cầu bắt buộc chỉ dùng một máy. Nhóm có thể ngồi chung, dùng máy của Người 4 để chốt `ho_so_launch_v0.md` và đề xuất cuối:

- Người 1 cung cấp chỉ số, event và rủi ro kinh tế.
- Người 2 kiểm chi phí, cỡ mẫu, phạm vi và luật dừng.
- Người 3 kiểm bảng lỗi và ghi `phieu_cham.md` khi nhóm làm hội đồng.
- Người 4 nhập hồ sơ cuối và tổng hợp bản nộp.

Các file vẫn do người phụ trách trong bảng sửa. Phiếu chấm chỉ được điền sau khi thực sự đọc và duyệt hồ sơ nhóm khác.

## 5. Checklist trước khi nộp

- [ ] Chạy `python lab13.py` trong thư mục `src/` trên **một máy khác trong nhóm**; code chạy hết, ba phép thử A1 in ĐẠT.
- [ ] Đủ sáu file hồ sơ, báo cáo nhóm, bốn báo cáo cá nhân và thông tin đóng góp trong `TEAM.md`.
- [ ] Bảng chi phí có đủ phần A và B; mọi số từ cột `_simulated` có nhãn `simulated`.
- [ ] Bảng lỗi giữ đủ hai bộ nhãn độc lập, tỉ lệ đồng thuận và bảng khắc phục năm loại; nếu đồng thuận dưới 80%, ghi rõ việc rà lại định nghĩa theo yêu cầu CP3.
- [ ] `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn dấu `?` ngoài chú thích; có ít nhất ba luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ.
- [ ] Chỉ số có ít nhất sáu event với `trace_id` và ít nhất hai dòng rủi ro kinh tế có số liệu.
- [ ] Hồ sơ launch một trang, đủ bảy mục, có số liệu, trạng thái, vai trò phụ trách và đề xuất cuối.
- [ ] Không dùng từ bị cấm theo `RULES.md` trong hồ sơ; không commit `.env`, secret hoặc `.venv/`.
- [ ] Đã push bản cuối; mỗi thành viên tự nộp cùng link repo trên LMS trước deadline của lớp.

## 6. Tài liệu đối chiếu

- [TEAM.md](TEAM.md): vai trò và yêu cầu đổi người viết code sau giải lao.
- [CHECKPOINTS.md](CHECKPOINTS.md): đầu việc, sản phẩm và điều kiện hoàn thành CP1–CP5.
- [RULES.md](RULES.md): tính độc lập của nhãn, nguồn số liệu và quy tắc làm bài.
- [SUBMISSION.md](SUBMISSION.md): cấu trúc bài nộp, kiểm tra trên máy khác và nộp LMS.
