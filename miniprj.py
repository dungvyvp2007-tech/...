# Câu 1:
while True: 
    try:
        while True:
            try:
                price_per_product = float(input("Nhập đơn giá của sản phẩm: "))
                if price_per_product < 0:
                    print('Vui lòng nhập giá lớn hơn 0!')
                    continue
                break
            except ValueError:
                print('Vui lòng nhập số nguyên!')
        while True:
            try:
                quantity = int(input('Nhập số lượng mua: '))
                if quantity < 0 :
                    print('Vui lòng nhập giá lớn hơn 0!')
                    continue
                break
            except ValueError:
                print('Vui lòng nhập số nguyên!')
            
        total_price = price_per_product * quantity
        if total_price >= 1000000 :
            total_price = total_price *0.9
    
        print(f'Số tiền khách phải thanh toán là: {total_price}')
        break
    except ValueError:
        print('Vui lòng nhập số nguyên!')

    
# Câu 2:
password = '123456'
count = 0
for i in range(3) :
    try:
        password_input = input('Nhập mật khẩu: ')

        if password_input == '123456' :
            print('Đăng nhập thành công!')
            break
        else :
            print('Mật khẩu sai vui lòng nhập lại!')
            count += 1

        if count == 3:
            print('Tài khoản đã bị khóa!')
            break

    except ValueError:
        print('Vui lòng nhập số nguyên!')

# Câu 3:
tong_san_pham = 0       
so_thung_hop_le = 0    

print("--- HỆ THỐNG THỐNG KÊ LÔ HÀNG NHẬP ---")
print("Nhập số lượng sản phẩm cho từng thùng. Nhập số 0 để kết thúc.\n")
while True:
    so_luong = int(input("Nhập số lượng sản phẩm của thùng tiếp theo: "))
    
    if so_luong < 0:
        print("Số lượng không hợp lệ, bỏ qua thùng này!")
        
    elif so_luong == 0:
        print("Đã nhận tín hiệu kiểm đếm xong. Đang tổng hợp dữ liệu...\n")
        break
        
    else:
        tong_san_pham += so_luong
        so_thung_hop_le += 1
print("--- KẾT QUẢ THỐNG KÊ ---")
print(f"Tổng số thùng hàng hợp lệ đã đếm: {so_thung_hop_le} thùng")
print(f"Tổng số lượng sản phẩm thu được: {tong_san_pham} sản phẩm")