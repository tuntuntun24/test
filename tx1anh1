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
