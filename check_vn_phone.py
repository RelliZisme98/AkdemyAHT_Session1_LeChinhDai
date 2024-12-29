import re

def is_valid_vn_phone_number(phone_number):
    """
    Kiểm tra tính hợp lệ của số điện thoại Việt Nam.
    - Mã vùng hợp lệ: 03, 05, 07, 08, 09.
    - Tổng số ký tự: 10 chữ số.
    """
    phone_number = phone_number.strip()  # Loại bỏ khoảng trắng ở đầu và cuối
    pattern = r'^(03|05|07|08|09)\d{8}$'
    return re.match(pattern, phone_number) is not None



def validate_and_process_phone_number(phone_number):
    # Xử lý lỗi nhập liệu: Loại bỏ khoảng trắng không cần thiết
    phone_number = phone_number.strip()
    if is_valid_vn_phone_number(phone_number):
        return f"Số {phone_number} là số điện thoại hợp lệ tại Việt Nam."
    else:
        return f"Số {phone_number} không hợp lệ."


def process_phone_numbers_list(phone_numbers):
    """
    Kiểm tra danh sách các số điện thoại.
    """
    phone_list = [phone.strip() for phone in phone_numbers.split(",")]
    results = []
    for phone in phone_list:
        results.append(validate_and_process_phone_number(phone))
    return results


def test_cases():
    """
    Hàm test các trường hợp cụ thể để đảm bảo tính chính xác.
    """
    test_data = {
        "0356789123": True,  # Số hợp lệ
        "0961234567": True,  # Số hợp lệ
        "085123456": False,  # Không đủ số
        "07891234567": False,  # Quá nhiều số
        "0412345678": False,  # Mã vùng không hợp lệ
        " 0356789123  ": True,  # Số hợp lệ, có khoảng trắng
        "+840356789123": False,  # Số với mã quốc gia, không hợp lệ
    }

    print("=== Kết quả kiểm tra Test Case ===")
    for phone, expected in test_data.items():
        result = is_valid_vn_phone_number(phone)
        status = "Đúng" if result == expected else "Sai"
        print(f"Test số '{phone}': Kết quả thực tế = {result}, Kỳ vọng = {expected} -> {status}")


def main():
    print("=== Kiểm tra số điện thoại Việt Nam ===")
    print("1. Kiểm tra số điện thoại đơn lẻ")
    print("2. Kiểm tra danh sách số điện thoại")
    print("3. Kiểm tra test case")
    print("4. Thoát chương trình")

    while True:
        try:
            choice = input("Chọn chức năng (1/2/3/4): ").strip()
            if choice == "1":
                # Kiểm tra số điện thoại đơn lẻ
                phone_number = input("Nhập số điện thoại: ").strip()
                print(validate_and_process_phone_number(phone_number))

            elif choice == "2":
                # Kiểm tra danh sách số điện thoại
                phone_numbers = input("Nhập danh sách số điện thoại (cách nhau bởi dấu phẩy): ").strip()
                results = process_phone_numbers_list(phone_numbers)
                for result in results:
                    print(result)

            elif choice == "3":
                # Chạy hàm kiểm tra test case
                test_cases()

            elif choice == "4":
                # Thoát chương trình
                print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
                break

            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")


if __name__ == "__main__":
    main()
