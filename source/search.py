import pandas as pd
import numpy as np
def interpolation_search(array, x):
  
    n = len(array)
    left = 0
    right = n -1

    while left <= right and x >= array[left] and x <= array[right]:
        if left == right:
            if array[left]==x:
                return left
            return -1

        position =  left + int((float( right - left)/(array[right] - array[left])) * (x - array[left]))
        
        if (array[position] == x):
            return position
        if (array[position] < x):
            left = position + 1
        else:
            right = position -1
    return -1

def search_by_name(file_path, name):
    """
    Tìm kiếm thông tin của một người trong file Excel dựa trên tên của họ.
    Hiển thị tất cả thông tin về người đó nếu tìm thấy, và thông báo nếu không tìm thấy.
    """
    # Đọc dữ liệu từ file Excel vào một DataFrame
    df = pd.read_excel(file_path)

    name = name.lower()
    print(name)
   
    # tìm kiếm theo cột tên trong file Excel
    name_col = 'Họ và tên'
    # Áp dụng hàm .str.lower() để chuyển đổi tất cả các giá trị trong cột thành chữ thường
    names = df[name_col].str.lower()
    print(names)
    # Lấy ra mảng numpy chứa các giá trị đã được chuyển đổi sang chữ thường
    names = np.array(names.values)
    
    # print(len(names))
     
    # if not matching_rows.empty:
    #     print(matching_rows)
    # else:
    #     print("Không tìm thấy bản ghi phù hợp.")
    index = interpolation_search(names, name)

    if index != -1:
        # nếu tìm thấy tên, hiển thị tất cả thông tin liên quan đến người đó
        print(f"Tìm thấy thông tin về {name}:")
        print(df.iloc[index])
    else:
        print(f"Không tìm thấy thông tin về {name}.")

file_path = "C:\\Users\\ky_II_nam3\\TKTT\\project\\data.xlsx"
name = 'Nguyễn Hoài Sơn'#input("Nhập tên cần tìm kiếm: ")

search_by_name(file_path, name)
