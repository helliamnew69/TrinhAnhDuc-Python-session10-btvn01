# Khoi tao gio hang mau
cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

# Vong lap menu chinh
while True:

    # Hien thi menu
    print("\n===== HE THONG QUAN LY GIO HANG SHOPEE =====")
    print("1. Xem chi tiet gio hang")
    print("2. Them san pham moi hoac tang so luong")
    print("3. Cap nhat so luong san pham")
    print("4. Xoa san pham khoi gio hang")
    print("5. Thoat chuong trinh")

    # Nhap lua chon
    choice = input("Nhap lua chon cua ban: ").strip()

    match choice:

        # Chuc nang 1: Xem gio hang
        case "1":

            # Kiem tra gio hang rong
            if len(cart_items) == 0:
                print("Gio hang hien dang trong!")

            else:

                total_quantity = 0
                total_price = 0

                print("\n===== GIO HANG =====")

                # Duyet danh sach san pham
                for i in range(len(cart_items)):

                    product = cart_items[i]

                    product_id = product[0]
                    product_name = product[1]
                    quantity = product[2]
                    price = product[3]

                    print(
                        i + 1,
                        ".",
                        product_id,
                        "-",
                        product_name,
                        "- SL:",
                        quantity,
                        "- Gia:",
                        price
                    )

                    # Cong don tong so luong
                    total_quantity += quantity

                    # Cong don tong tien
                    total_price += quantity * price

                print("\nTong so luong san pham:", total_quantity)
                print("Tong tien:", total_price)

        # Chuc nang 2: Them san pham
        case "2":

            product_id = input("Nhap ma san pham: ").strip().upper()

            product_name = input("Nhap ten san pham: ").strip()

            try:

                quantity = int(input("Nhap so luong: "))
                price = int(input("Nhap don gia: "))

                # Validate du lieu
                if quantity <= 0:
                    print("So luong phai lon hon 0")
                    continue

                if price < 0:
                    print("Don gia khong duoc am")
                    continue

                found = False

                # Tim san pham da ton tai
                for product in cart_items:

                    if product[0] == product_id:

                        # Cong don so luong
                        product[2] += quantity

                        found = True

                        print("Da cong don so luong san pham!")
                        break

                # Neu chua ton tai thi them moi
                if found == False:

                    new_product = [
                        product_id,
                        product_name,
                        quantity,
                        price
                    ]

                    cart_items.append(new_product)

                    print("Da them san pham moi vao gio hang!")

            except:
                print("So luong va don gia phai la so nguyen")

        # Chuc nang 3: Cap nhat so luong
        case "3":

            product_id = input("Nhap ma san pham: ").strip().upper()

            try:

                new_quantity = int(input("Nhap so luong moi: "))

                # Validate so luong
                if new_quantity <= 0:
                    print("So luong phai lon hon 0")
                    continue

                found = False

                # Tim san pham
                for product in cart_items:

                    if product[0] == product_id:

                        # Cap nhat so luong
                        product[2] = new_quantity

                        found = True

                        print("Cap nhat so luong thanh cong!")
                        break

                # Khong tim thay san pham
                if found == False:
                    print("Ma san pham khong ton tai trong gio hang.")

            except:
                print("So luong phai la so nguyen")

        # Chuc nang 4: Xoa san pham
        case "4":

            product_id = input("Nhap ma san pham can xoa: ").strip().upper()

            found = False

            # Duyet gio hang
            for product in cart_items:

                if product[0] == product_id:

                    # Xoa san pham
                    cart_items.remove(product)

                    found = True

                    print("Da xoa san pham khoi gio hang!")
                    break

            # Khong tim thay san pham
            if found == False:
                print("Ma san pham khong ton tai trong gio hang.")

        # Chuc nang 5: Thoat
        case "5":

            print("Cam on ban da su dung he thong!")
            break

        # Truong hop nhap sai menu
        case _:

            print("Lua chon khong hop le, vui long nhap lai!")