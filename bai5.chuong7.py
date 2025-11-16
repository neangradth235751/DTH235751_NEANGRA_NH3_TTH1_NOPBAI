import json

pythonObject = {
 "ten": "Trần Duy Thanh",
 "tuoi": 50,
 "ma": "nv1"
}

# Chuyển đổi đối tượng Python (Dictionary) thành chuỗi JSON
jsonString = json.dumps(pythonObject)

# Kết quả là một chuỗi JSON (JSON string):
print(jsonString)
