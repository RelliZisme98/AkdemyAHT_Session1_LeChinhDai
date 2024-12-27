import re


def is_valid_vn_phone_number(phone_number):
    """
    Kiểm tra tính hợp lệ của số điện thoại Việt Nam.
    - Mã vùng hợp lệ: 03, 05, 07, 08, 09.
    - Tổng số ký tự: 10 chữ số.
    """
    pattern = r'^(03|05|07|08|09)\d{8}$'  # Biểu thức chính quy kiểm tra số điện thoại
    return re.match(pattern, phone_number) is not None #regex


def main():
    print("=== Kiểm tra số điện thoại Việt Nam ===")
    print("1. Kiểm tra số điện thoại đơn lẻ")
    print("2. Kiểm tra danh sách số điện thoại")
    print("3. Thoát chương trình")

    while True:
        try:
            choice = input("Chọn chức năng (1/2/3): ").strip()

            if choice == "1":

                phone_number = input("Nhập số điện thoại: ").strip()
                if is_valid_vn_phone_number(phone_number):
                    print(f"Số {phone_number} là số điện thoại hợp lệ tại Việt Nam.")
                else:
                    print(f"Số {phone_number} không hợp lệ.")

            elif choice == "2":

                phone_numbers = input("Nhập danh sách số điện thoại (cách nhau bởi dấu phẩy): ").strip()
                phone_list = phone_numbers.split(",")
                for phone in phone_list:
                    phone = phone.strip()  # Loại bỏ khoảng trắng
                    if is_valid_vn_phone_number(phone):
                        print(f"Số {phone} là số điện thoại hợp lệ.")
                    else:
                        print(f"Số {phone} không hợp lệ.")

            elif choice == "3":
                # Thoát chương trình
                print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
                break

            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")


if __name__ == "__main__":
    main()
