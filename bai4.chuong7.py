import json

jsonString = '{ "ma":"nv1", "age":50, "ten":"Trần Duy Thanh"}'

# Chuyển chuỗi JSON (jsonString) thành đối tượng Python (Dictionary)
dataObject = json.loads(jsonString)

print(dataObject)
# Truy cập các giá trị trong dictionary bằng key tương ứng
print("Mã=", dataObject["ma"])
print("Tên=", dataObject["ten"])  # Đã sửa lỗi logic: in ra key 'ten'
print("Tuổi=", dataObject["age"]) # Đã sửa lỗi logic: in ra key 'age'
