from fb_func import xac_thuc_email, luu_thong_tin_nguoi_dung


def tinh_toan(a, b, c):  # a,b argument, parameter
    if c == '+':
        ket_qua = a + b
    elif c == '-':
        ket_qua = a -b
    elif c == '*':
        ket_qua = a*b
    elif c == '/':
        ket_qua = a/b

    return ket_qua


if __name__ == "__main__": #đoạn code này chỉ được thực thi khi developer run trực tiếp từ file này
    # tạo tài khoản facebook
    # 1: Gửi email xác thực vào email đã đăng ký trên tk facebook
    # 2: lưu thông tin các bạn vào cở sở dữ
    print("Cod chay trong file function demo")
    xac_thuc_email()
    luu_thong_tin_nguoi_dung()
    print("hello")
