# Phân tích lỗi

# product_code = product_info[1]
# Sai vì index 1 là "Áo polo nam", không phải mã sản phẩm.
# Mã sản phẩm "SP001" nằm ở index 0.

# product_name = product_info[2]
# Sai vì index 2 là "Size L", không phải tên sản phẩm.
# Tên sản phẩm "Áo polo nam" nằm ở index 1.

# product_length = product_info.length()
# Sai vì tuple không có phương thức length().
# Muốn đếm số phần tử phải dùng hàm len().

# product_info[3] = 279000
# Sai vì tuple là immutable (không thể thay đổi trực tiếp phần tử).
# Muốn cập nhật giá bán phải tạo tuple mới.


# Code đã sửa

product_info = ("SP001", "Áo polo nam", "Size L", 299000)
product_code = product_info[0]
product_name = product_info[1]
product_length = len(product_info)
product_info = (product_info[0],product_info[1],product_info[2],279000)
print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)