from xml.dom.minidom import parse
import xml.dom.minidom

# Mở file xml bằng minidom parser
DOMTree = xml.dom.minidom.parse("employees.xml")
collection = DOMTree.documentElement

# Lấy tất cả tag là employee
employees = collection.getElementsByTagName("employee")

# Duyệt vòng lặp để lấy toàn bộ dữ liệu ra
for employee in employees:
    # Lấy tag 'id' đầu tiên trong employee
    tag_id = employee.getElementsByTagName('id')[0]
    # Lấy dữ liệu (nội dung text) của tag 'id'
    id = tag_id.childNodes[0].data
    
    # Lấy tag 'name' đầu tiên trong employee
    tag_name = employee.getElementsByTagName('name')[0]
    # Lấy dữ liệu (nội dung text) của tag 'name'
    name = tag_name.childNodes[0].data
    
    # In ra ID và Name, cách nhau bằng tab
    print(id, '\t', name)
