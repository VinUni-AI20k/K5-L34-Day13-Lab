"""Lab 13 · CP3 · Thành viên 3: so hai bộ nhãn độc lập và tính tỉ lệ đồng thuận.

Script này KHÔNG gắn nhãn. Nó chỉ đọc nguyên hai bộ nhãn do người gắn nhãn 1 (TV1) và
người gắn nhãn 2 (TV2) đã commit, rồi đếm số ca trùng.

Chạy trong thư mục src/:
    python3 tv3_cp3_dong_thuan.py <file_nhan_1> <file_nhan_2> [--bang]

Mỗi file nhãn có thể là:
  - bảng Markdown: các dòng "| <số ca> | ... | <nhãn> |", lấy ô cuối cùng không rỗng làm nhãn
    (ví dụ report/team/tv2_cp3_ban_giao.md); hoặc
  - CSV hai cột: ca,nhan
--bang: in thêm 20 dòng bảng để chép vào report/team/bang_loi.md
        (cột "Nhãn thống nhất" để trống cho ca lệch, vì nhóm phải tự thống nhất).
"""
import csv
import re
import sys
import unicodedata
from pathlib import Path

LOAI = ['Do người dùng', 'Hệ thống', 'Ngữ cảnh', 'Giới hạn hệ thống', 'Ngầm']
SO_CA = 20
NGUONG = 16  # 80% của 20 ca


def bo_dau(s):
    s = unicodedata.normalize('NFD', s.replace('đ', 'd').replace('Đ', 'D'))
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn').lower().strip()


def chuan_hoa(nhan):
    """Đưa cách viết khác nhau về đúng 1 trong 5 loại PAIR; không đoán, sai thì báo lỗi."""
    k = re.sub(r'[\s_\-*`]+', ' ', bo_dau(nhan)).strip()
    if not k:
        return None
    if 'gioi han' in k:                 # phải xét trước "he thong"
        return 'Giới hạn hệ thống'
    if 'nguoi dung' in k:
        return 'Do người dùng'
    if 'ngu canh' in k:
        return 'Ngữ cảnh'
    if k.startswith('ngam') or k == 'an' or 'loi ngam' in k:
        return 'Ngầm'
    if 'he thong' in k:
        return 'Hệ thống'
    raise ValueError(f'nhãn không thuộc 5 loại PAIR: "{nhan}"')


def doc_nhan(duong_dan):
    p = Path(duong_dan)
    nhan = {}
    if p.suffix.lower() == '.csv':
        with p.open(encoding='utf-8') as f:
            for dong in csv.reader(f):
                if len(dong) >= 2 and dong[0].strip().isdigit():
                    nhan[int(dong[0])] = dong[1]
    else:
        for dong in p.read_text(encoding='utf-8').splitlines():
            m = re.match(r'^\|\s*(\d+)\s*\|(.*)\|\s*$', dong)
            if not m:
                continue
            o = [x.strip() for x in m.group(2).split('|')]
            nhan[int(m.group(1))] = o[-1] if o else ''
    ket_qua, loi = {}, []
    for ca in range(1, SO_CA + 1):
        try:
            v = chuan_hoa(nhan.get(ca, ''))
        except ValueError as e:
            loi.append(f'ca {ca}: {e}')
            continue
        if v is None:
            loi.append(f'ca {ca}: chưa có nhãn')
        else:
            ket_qua[ca] = v
    return ket_qua, loi


def kappa(n1, n2):
    """Cohen's kappa, để tham khảo thêm ngoài tỉ lệ đồng thuận của đề."""
    n = len(n1)
    po = sum(n1[c] == n2[c] for c in n1) / n
    pe = sum((list(n1.values()).count(l) / n) * (list(n2.values()).count(l) / n) for l in LOAI)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    n1, loi1 = doc_nhan(argv[1])
    n2, loi2 = doc_nhan(argv[2])
    if loi1 or loi2:
        print('CHƯA ĐỦ NHÃN, không tính đồng thuận:')
        for l in loi1:
            print(f'  [người 1] {l}')
        for l in loi2:
            print(f'  [người 2] {l}')
        return 1

    lech = [c for c in range(1, SO_CA + 1) if n1[c] != n2[c]]
    trung = SO_CA - len(lech)
    print(f'Tỉ lệ đồng thuận: {trung} / {SO_CA} = {trung / SO_CA:.0%}'.replace('.', ','))
    print(f"Cohen's kappa (tham khảo): {kappa(n1, n2):.2f}".replace('.', ','))
    print('ĐẠT ngưỡng 80% (≥ 16/20)' if trung >= NGUONG
          else 'DƯỚI 80%: phải viết lại định nghĩa trước khi đi tiếp')
    if lech:
        print('\nCa lệch (nhóm tự thống nhất, ghi 1 câu quy tắc cho mỗi ca):')
        for c in lech:
            print(f'  ca {c:>2}: người 1 = {n1[c]} · người 2 = {n2[c]}')
    print('\nSố ca mỗi loại (người 1 / người 2):')
    for l in LOAI:
        print(f'  {l:18s} {list(n1.values()).count(l):>2} / {list(n2.values()).count(l):>2}')

    if '--bang' in argv:
        print('\n| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |')
        print('| --: | --- | --- | --- | --- |')
        for c in range(1, SO_CA + 1):
            ok = n1[c] == n2[c]
            print(f'| {c} | {n1[c]} | {n2[c]} | {"Có" if ok else "Không"} | {n1[c] if ok else "(nhóm thống nhất)"} |')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
