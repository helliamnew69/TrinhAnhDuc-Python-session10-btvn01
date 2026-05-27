# Khoi tao bien luu thong tin don hang
sender_name = ""
sender_phone = ""
pickup_address = ""

receiver_name = ""
receiver_phone = ""

delivery_address = ""

note = ""

# Vong lap menu chinh
while True:

    # Hien thi menu
    print("\n===== HE THONG QUAN LY DON HANG GRAB =====")
    print("1. Nhap du lieu don hang")
    print("2. Chuan hoa ma don hang")
    print("3. An so dien thoai")
    print("4. Tim kiem va thay the ghi chu")
    print("5. Thoat")

    # Nguoi dung nhap lua chon
    choice = input("Nhap lua chon cua ban: ").strip()

    match choice:

        # Chuc nang 1: Nhap du lieu don hang
        case "1":

            sender_name = input("Ten nguoi gui: ").strip()
            sender_phone = input("SDT nguoi gui: ").strip()
            pickup_address = input("Dia chi lay hang: ").strip()

            receiver_name = input("Ten nguoi nhan: ").strip()
            receiver_phone = input("SDT nguoi nhan: ").strip()
            delivery_address = input("Dia chi giao hang: ").strip()

            note = input("Ghi chu giao hang: ").strip()

            # Validate ten nguoi gui
            if sender_name == "":
                print("Ten nguoi gui khong duoc bo trong")
                continue

            # Validate ten nguoi nhan
            if receiver_name == "":
                print("Ten nguoi nhan khong duoc bo trong")
                continue

            # Validate ghi chu
            if note == "":
                print("Ghi chu khong duoc bo trong")
                continue

            # Chuan hoa ten
            sender_name = sender_name.title()
            receiver_name = receiver_name.title()

            # Hien thi bao cao
            print("\n===== BAO CAO DON HANG =====")
            print("Nguoi gui:", sender_name)
            print("Nguoi nhan:", receiver_name)
            print("Dia chi lay:", pickup_address)
            print("Dia chi giao:", delivery_address)

            print("Ghi chu:", note)
            print("Do dai ghi chu:", len(note))
            print("So tu:", len(note.split()))
            print("Chu thuong:", note.lower())
            print("Chu hoa:", note.upper())

        # Chuc nang 2: Chuan hoa ma don hang
        case "2":

            order_code = input("Nhap ma don hang: ").strip()

            # Chuyen sang chu hoa
            order_code = order_code.upper()

            # Thay khoang trang bang dau gach ngang
            order_code = order_code.replace(" ", "-")

            # Them tien to GRAB- neu chua co
            if not order_code.startswith("GRAB-"):
                order_code = "GRAB-" + order_code

            print("Ma don hang chuan hoa:", order_code)

        # Chuc nang 3: An so dien thoai
        case "3":

            # Kiem tra da co du lieu hay chua
            if sender_phone == "" or receiver_phone == "":
                print("Chua co du lieu so dien thoai")
                continue

            # Validate sdt nguoi gui
            if not sender_phone.isdigit():
                print("So dien thoai nguoi gui khong hop le")
                continue

            # Validate sdt nguoi nhan
            if not receiver_phone.isdigit():
                print("So dien thoai nguoi nhan khong hop le")
                continue

            # Validate do dai sdt nguoi gui
            if len(sender_phone) != 10:
                print("So dien thoai nguoi gui phai co dung 10 ky tu")
                continue

            # Validate do dai sdt nguoi nhan
            if len(receiver_phone) != 10:
                print("So dien thoai nguoi nhan phai co dung 10 ky tu")
                continue

            # An thong tin sdt
            hidden_sender = sender_phone[:3] + "*****" + sender_phone[-2:]
            hidden_receiver = receiver_phone[:3] + "*****" + receiver_phone[-2:]

            print("SDT nguoi gui:", hidden_sender)
            print("SDT nguoi nhan:", hidden_receiver)

        # Chuc nang 4: Tim kiem va thay the tu khoa
        case "4":

            # Kiem tra da co ghi chu hay chua
            if note == "":
                print("Chua co ghi chu giao hang de tim kiem")
                continue

            old_word = input("Nhap tu khoa can tim: ").strip()
            new_word = input("Nhap tu khoa thay the: ").strip()

            # Dem so lan xuat hien
            count_word = note.count(old_word)

            if count_word > 0:

                # Thay the tu khoa
                note = note.replace(old_word, new_word)

                print("So lan xuat hien:", count_word)
                print("Ghi chu moi:", note)

            else:
                print("Khong tim thay tu khoa")

        # Chuc nang 5: Thoat chuong trinh
        case "5":

            print("Thoat chuong trinh")
            break

        # Truong hop nhap sai menu
        case _:

            print("Lua chon khong hop le, vui long nhap lai!")