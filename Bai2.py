#ở levi thì code chạy được nhưng sofm thì code bị lỗi vì ở levi có đầy đủ thông tin ở 3 vị trí index khác nhau còn với sofm thì chỉ có 2 thông tin ở vị trí index đầu bị thiếu thông tin dữ liệu ở vị trí index cuối
#khi đến optimus bị lỗi ở dòng b = (m * 10) + (int(r) * 0.5) vì ở vị trí index thứ 2 thông tin dữ liệu của optimus nó lại lưu dưới dạng chuỗi là chữ nên sẽ gây ra lỗi khi thực hiện tính toán
# dòng code sẽ in từng dòng cho thấy đang xử lý đến tuyển thủ nào và rất dễ để biết được rằng tuyển thủ nào đang gây lỗi cho chương trình
#
# Dữ liệu từ API: (Tên, Số trận, MMR)
data = [
    ("Levi", 120, 2500),      # Dữ liệu chuẩn
    ("SofM", 150),            # Lỗi API: Bị thiếu mất trường MMR (Tuple chỉ có 2 phần tử)
    ("Optimus", 100, "N/A")   # Lỗi dữ liệu: Điểm MMR bị ghi chữ "N/A"
]

# Hàm xử lý dồn cục, không có cơ chế bẫy lỗi
def process(ds):
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    for player in ds:
        print("Đang xử lý:", player)
        
        
        # Tính toán tiền thưởng
        try:
            name_player = p[0]
            matchs = p[1]
            rp_point = p[2]  # Lấy điểm MMR
            bbr = (matchs * 10) + (int(rp_point) * 0.5)
            print("Tuyển thủ", name_player, "nhận được", bbr, "RP")
        except ValueError:
            print(f'Tuyển thủ {name_player} Lỗi - Dữ liệu MMR không hợp lệ')
        except IndexError:
            print(f'Tuyển thủ {name_player} Lỗi - Hồ sơ bị thiếu thông tin')
# Chạy hệ thống
process(data)
