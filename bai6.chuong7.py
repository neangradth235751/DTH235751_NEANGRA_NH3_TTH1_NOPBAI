import csv

# Mở file 'datacsv.csv' để đọc
# newline='' cần thiết cho việc xử lý CSV trên các hệ điều hành khác nhau
with open('datacsv.csv', newline='') as f:
    # Tạo đối tượng reader: 
    # delimiter=';' chỉ định dấu chấm phẩy là ký tự phân tách
    # quoting=csv.QUOTE_NONE đảm bảo các trường không được bọc trong dấu ngoặc kép
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    
    # Duyệt qua từng dòng (list) được trả về bởi reader
    for row in reader:
        # In ra phần tử đầu tiên của dòng, theo sau là một ký tự tab
        print(row[0], "\t")
