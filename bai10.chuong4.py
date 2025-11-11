import time
import os

# Hàm xóa màn hình (hoạt động cho Windows)
def clear():
    os.system('cls')

# Hình 1
h1 = """
   *
  * *
 *   *
*******
*     *
*     *
"""

# Hình 2
h2 = """
*****
*    *
*****
*  *
*   *
*    *
"""

# Hình 3
h3 = """
  *
 * *
*   *
 * *
  *
"""

# Hình 4
h4 = """
*     *
 *   *
  * *
   *
  * *
 *   *
*     *
"""

# Danh sách các hình
shapes = [h1, h2, h3, h4]

# Hiển thị từng hình cách nhau 5 giây
for i, shape in enumerate(shapes, start=1):
    clear()
    print(f"Hình {i}:")
    print(shape)
    time.sleep(5)

clear()
print("Kết thúc hiển thị các hình.")
