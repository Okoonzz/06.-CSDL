import lxml.etree as ET
from tabulate import tabulate

# Mở file chứa các đường dẫn tuyệt đối đã lưu ở câu 4
with open("Path.txt", "r", encoding="utf-8") as file:
    res = file.read()

# Lọc dữ liệu đường dẫn file
num = res.split("\n")

# Hàm tìm kiếm theo xpath
def find(path, low, high):

    # Đọc file XML
    tree = ET.parse(path)
    root = tree.getroot()

    # Tạo một danh sách để lưu trữ các học sinh thỏa mãn ngưỡng điểm
    students = []

    # Dùng mẫu XPath để tìm các học sinh thỏa mãn điều kiện
    xpath_expression = f".//student[number(DIEMTB) >= {low} and number(DIEMTB) <= {high}]"
    matching_students = root.xpath(xpath_expression)

    # Duyệt qua từng học sinh thỏa mãn và lấy thông tin
    for student in matching_students:
        name = student.findtext('HOTEN')
        score = float(student.findtext('DIEMTB'))
        students.append((name, score))

    return students


while True:
    
    # In ra terminal những file xml vừa truy vấn ở câu 4, để người dùng có thể dễ dàng kiểm soát dữ liệu 
    in4 = []
    for line in num:
        lines = line.split("\\")
        if len(lines) >= 2:
            in4.append(lines[-1])
    
    print("Created xml files: ")

    for idxx, val in enumerate(in4, start=1):
        print(f"{idxx}: {val}")
    
    # Nhập vào lần thứ truy vấn. Tức là truy vấn lần thứ bao nhiêu ở câu 4
    prs = int(input("Please enter the file number: "))

    # Nhập ngưỡng điểm thấp
    prs_l = float(input("Please enter the lower score range: "))

    #Nhập ngưỡng điểm cao
    prs_h = float(input("Please enter the higher score range: "))

    # Kiêm tra điều kiện nhập điểm
    if not (0.0 <= prs_l <= 10.0) or not (0.0 <= prs_h <= 10.0):
        print("Please enter valid score (from 0.0 to 10.0)")
        exit(0)

    print(f"The students included in the score threshold [{prs_l} - {prs_h}] of the {prs} query are:")

    # Tìm kiếm các học sinh có trong ngưỡng điểm vừa nhập
    res = find(f"{num[prs-1]}", prs_l, prs_h)
    table_data = []

    # Tạo header cho dữ liệu được in ra
    headers = ["HỌ TÊN", "ĐIỂM"]

    # Duyệt qua danh sách vừa tìm được để in ra kết quả
    for idx in res:
        name, score = idx
        table_data.append((name, score))

    # Nếu không tìm được thì chắc chắn nằm ngoài ngưỡng điểm
    if len(table_data) == 0:
        print("It looks like you have entered out of range of values corresponding to the rating")

    # Tiến hành in ra terminal những kết quả vừa tìm được
    else:
        # Mỗi lần in ra được 100 dòng đến khi hết dữ liệu vừa tìm
        rows_per_table = 100
        table_data_chunks = [table_data[i:i+rows_per_table] for i in range(0, len(table_data), rows_per_table)]
        for chunk in table_data_chunks:
            print(tabulate(chunk, headers=headers, tablefmt="grid"))
            print("\n***************************************\n")
    
    # Nếu muốn tiếp tục tìm kiếm nhấn Y hoặc N nếu không muốn 
    choice = input("Press Y to continue or N to stop [y/n] ").upper()[:1]
    if choice == "Y":
        continue
    else:
        print("BYE!!!")
        file.close()
        break
