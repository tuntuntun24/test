# Hàm nhập dữ liệu sinh viên từ bàn phím
def nhap():
    sv = {}
    n = int(input("Nhập số lượng sinh viên: "))
    for _ in range(n):
        ma_sv = input("Nhập mã sinh viên: ")
        tin_chi = int(input("Nhập số tín chỉ đã học: "))
        sv[ma_sv] = tin_chi
    return sv
sv = nhap()

# Hàm khởi tạo lớp học
def tao_lop():
    return {
        "mon01": "Lập trình python cơ bản",
        "mon02": "Lập trình hướng đối tượng",
        "mon03": "Ứng dụng thuật toán"
    }
lop = tao_lop()
print("Thông tin lớp học phần:", lop)

# Hàm kiểm tra và chỉnh sửa sinh viên
def tim_sv(sv):
    if "2024123456" in sv:
        sv["2024123456"] = 100
    else:
        print("Không tìm thấy mã sinh viên 2024123456. Vui lòng nhập số tín chỉ:")
        sv["2024123456"] = int(input("Nhập số tín chỉ đã học: "))
tim_sv(sv)


================================================================================


# Hàm nhập dữ liệu từ bàn phím
def nhap():
    ds = []
    n = int(input("Nhập số lượng hàng hóa: "))
    for _ in range(n):
        ma = input("Nhập mã hàng: ")
        ten = input("Nhập tên mặt hàng: ")
        sl = int(input("Nhập số lượng: "))
        gia = float(input("Nhập giá tiền: "))
        tong_tien = sl * gia
        ds.append([ma, ten, sl, gia, tong_tien])
    return ds
ds = nhap()

# Hàm hiển thị danh sách hàng hóa
def ht(ds):
    print("Danh sách hàng hóa:")
    print("Mã hàng | Tên mặt hàng | Số lượng | Giá tiền | Tổng tiền")
    for i in ds:
        print(f"{i[0]} | {i[1]} | {i[2]} | {i[3]} VND | {i[4]} VND")
ht(ds)

# Hàm tìm tổng tiền nhỏ nhất
def tim_tong_tien_nho_nhat(ds):
    min_tien = min(hang[4] for hang in ds)
    return min_tien
min_tien = tim_tong_tien_nho_nhat(ds)

# Hàm hiển thị các mặt hàng có tổng tiền nhỏ nhất
def hien_thi_hang_hoa_min(ds, min_tien):
    print("\nMặt hàng có tổng tiền nhỏ nhất:")
    for hang in ds:
        if hang[4] == min_tien:
            print(f"{hang[0]} | {hang[1]} | {hang[2]} | {hang[3]} VND | {hang[4]} VND")
hien_thi_hang_hoa_min(ds, min_tien)

# Hàm đếm số lượng mặt hàng thỏa điều kiện
def dem_hang_hoa_dac_biet(ds):
    count = sum(1 for hang in ds if hang[2] > 5 and hang[4] < 1_000_000)
    return count
so_luong_hang_dac_biet = dem_hang_hoa_dac_biet(ds)
print(f"\nSố lượng mặt hàng có số lượng > 5 và tổng tiền < 1,000,000 VND: {so_luong_hang_dac_biet}")


# Hàm xoá sinh viên có số tín chỉ bằng 0
def xoa_sv(sv):
    sv_xoa = [i for i in sv if sv[i] == 0]
    for i in sv_xoa:
        del sv[i]
xoa_sv(sv)

# Hàm chuyển từ điển sang danh sách
def chuyen_du_lieu(sv):
    a = []
    b = []
    for i in sv.keys():
        a.append(i)
    for j in sv.values():
        b.append(j)
    print("3 phần tử đầu mảng a", a[:3])
    print("3 phần tử cuối mảng b", b[-3:])
chuyen_du_lieu(sv)
