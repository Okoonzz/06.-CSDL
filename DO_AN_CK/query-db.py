import pymysql
import pandas as pd
import time
import xml.etree.ElementTree as ET
import xml.dom.minidom
import os
from tabulate import tabulate

# Nhập vào mật khẩu
inputpass = input("Please enter MySQL password: ")


# Ghi đường dẫn mỗi file XML vào Path.txt
f = open("Path.txt", "w", encoding="utf-8")
while True:

    # Nhập vào tên database muốn truy vấn
    inputdatabase = input("Please enter the database you want to make queries on (TRUONGHOC1, TRUONGNHOC2): ").upper()
    
    # Cảnh báo lỗi nếu không nhập đúng định dạng
    assert inputdatabase in ("TRUONGHOC1", "TRUONGHOC2") , "Please enter correct format!" 

    # Nhập vào mã số của trường muốn truy vấn
    inputtentruong = input("Please enter the school id you want to make queries on(00-99): ")

    # Cảnh báo lỗi nếu không nhập đúng 2 chữ số từ 00 đến 99
    assert len(inputtentruong) == 2, "Please enter correct format(00-99)!"

    # Nhập vào năm học theo định dạng YYYY-YYYY
    namhoc = input("Please enter the year in YYYY - YYYY, the years are consecutive (from 2018 to 2023): ")

    # Cảnh báo lỗi nếu nhập không đúng định dạng
    assert len(namhoc) == 9 or len(namhoc) == 11, "Please enter correct format!"
    
    # Kiểm tra xem nhập vào có theo thứ tự năm sau cách năm trước 1 năm hay không.
    tmp = []
    if len(namhoc) == 9:
        in_1 = int(namhoc.split("-")[0])
        in_11 = int(namhoc.split("-")[1])
        if(in_11 - in_1 != 1):
            print("Please enter the year in YYYY - YYYY, the years are consecutive (2021-2022)!")
            exit(0)
        tmp.append(in_1)
    elif len(namhoc) == 11:
        in_2 = int(namhoc.split(" - ")[0])
        in_22 = int(namhoc.split(" - ")[1])
        if(in_22 - in_2 != 1):
            print("Please enter the year in YYYY - YYYY, the years are consecutive (2021-2022)!")
            exit(0)
        tmp.append(in_2)

    inputnamhoc = tmp[0]
    
    # Báo lỗi nếu như nhập năm học không trong phạm vi từ 2018 đến 2023
    assert inputnamhoc in (range(2018, 2024)), "Enter the range from 2018 - 2023!"

    # Nhập vào xếp loại muốn truy vấn
    inputxeploai = input("please enter the qualification (xuất sắc ,giỏi, khá, trung bình, yếu): ").upper()

    # Báo lỗi nếu như nhập sai
    assert inputxeploai in ("XUẤT SẮC", "GIỎI", "KHÁ", "TRUNG BÌNH", "YẾU"), "Please enter the correct types!"

    # Định dạng lại format chuẩn của mã trường gồm TR301XX
    form_truong = f"TR301{inputtentruong}"

    # Định dạng lại format chuẩn của năm học có dạng 20xx - (20xx+1)
    form_namhoc = f"{inputnamhoc} - {inputnamhoc + 1}"

    # Đọc dữ liệu từ file sinh trường 
    datatruong = pd.read_excel(r"DanhSachTenTruong.xlsx")

    # Ánh xạ với bảng excel vừa mới sinh ra để tìm tên trường vừa nhập tương ứng với mã nhập vào
    ok = datatruong[datatruong['MA_TRUONG'] == form_truong]
    res = ok['TENTRUONG'].values[0]
    print(f"You entered: {res}")

    # Kết nối với TRUONGHOC1 nếu người dùng muốn
    if inputdatabase == "TRUONGHOC1":
        cnx_1 = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = f'{inputpass}',
            database = 'TRUONGHOC1'
        )

        cursor_1 = cnx_1.cursor()

        # Thực hiện câu lệnh truy vấn tương ứng với các điều kiện mà người dùng đã nhập vào.
        query_1 = r"""
                    SELECT concat_ws(' ', HS.HO, HS.TEN) as HOTEN, HS.NTNS, HOC.DIEMTB, HOC.XEPLOAI, HOC.KQUA
                    FROM (HOC LEFT JOIN TRUONG ON TRUONG.MATR = HOC.MATR)
                    LEFT JOIN HS ON HOC.MAHS = HS.MAHS
                    WHERE TRUONG.TENTR = '{0}' AND HOC.NAMHOC = '{1}' AND HOC.XEPLOAI = '{2}';
                """.format(res.replace("'", r"\'"), form_namhoc, inputxeploai)
        
        try:

            # Tính thời gian truy vấn
            star_1 = time.time()

            #Thực hiện câu truy vấn
            cursor_1.execute(query_1)

            # Lấy hết tất cả các kết quả truy vấn trả về
            result_1 = cursor_1.fetchall()

            root = ET.Element("data")
            table_data = []

            # Tạo tiêu đề cho bảng in ra terminal
            headers = ["HỌ TÊN", "NTNS", "ĐTB", "XẾP LOẠI", "KẾT QUẢ"]

            # Lấy kết quả vừa truy vấn thành công in ra terminal và file XML tương ứng
            for row in result_1:
                HOTEN = row[0]
                NTNS = row[1].strftime("%Y-%m-%d")
                DIEMTB = row[2]
                XEPLOAI = row[3]
                KQUA = row[4]

                # Ghi vào xml
                student = ET.SubElement(root, "student")
                ET.SubElement(student, "HOTEN").text = HOTEN
                ET.SubElement(student, "NTNS").text = NTNS
                ET.SubElement(student, "DIEMTB").text = str(DIEMTB)
                ET.SubElement(student, "XEPLOAI").text = XEPLOAI
                ET.SubElement(student, "KQUA").text = KQUA

                # Ghi vào danh sách để in ra terminal
                table_data.append([HOTEN, NTNS, DIEMTB, XEPLOAI, KQUA])
            
            # Giới hạn mỗi lần ghi được 100 dòng
            rows_per_table = 100
            table_data_chunks = [table_data[i:i+rows_per_table] for i in range(0, len(table_data), rows_per_table)]

            # In ra tất cả các kết quả cho từng bảng, mỗi bảng tương ứng 100 dòng 
            for chunk in table_data_chunks:
                print(tabulate(chunk, headers=headers, tablefmt="grid"))
                print("\n----------------------\n")
            
            # Xử lý file XML
            tree = ET.ElementTree(root)
            xml_str = ET.tostring(root, encoding="utf-8")
            dom = xml.dom.minidom.parseString(xml_str)
            pretty_xml_str = dom.toprettyxml(indent="  ")

            # Lấy đường dẫn của file XML ở thư mục hiện tại lưu vào file Path.txt
            current_directory = os.path.dirname(os.path.abspath(__file__))

            # Định dạng tên file xml
            filename = f"{inputdatabase}-{res}-{form_namhoc}-{inputxeploai}.xml"

            # Tiến hành ghi đường dẫn của xml vào Path.txt
            f.write(current_directory +"\\"+ filename + "\n")

            # Mở file xml và ghi nội dung vừa truy vấn được vào file
            with open(filename, "w", encoding="utf-8") as file:
                file.write(pretty_xml_str)
            print("XML file has been created according to your provided information:", filename)
        
        # Hiển thị lỗi nếu như quá trình truy vấn xảy ra lỗi
        except pymysql.Error as e:
            print("Error executing query:", str(e))

        cursor_1.close()
        cnx_1.close()    
        end_1 = time.time()

        # Tính toán thời gian thực hiện truy vấn cũng như ghi vào xml
        total_1 = end_1 - star_1

        print(f"Execution time: {total_1}")

    # Thực hiện truy vấn với TRUONGHOC2
    elif inputdatabase == "TRUONGHOC2":
        cnx_2 = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = f'{inputpass}',
            database = 'TRUONGHOC2'
        )
        
        cursor_2 = cnx_2.cursor()

        # Câu lệnh truy vấn tương ứng với những điều kiện mà người dùng vừa nhập
        query_2 = r"""
                    SELECT concat_ws(' ', HS.HO, HS.TEN) as HOTEN, HS.NTNS, HOC.DIEMTB, HOC.XEPLOAI, HOC.KQUA
                    FROM (HOC LEFT JOIN TRUONG ON TRUONG.MATR = HOC.MATR)
                    LEFT JOIN HS ON HOC.MAHS = HS.MAHS
                    WHERE TRUONG.TENTR = '{0}' AND HOC.NAMHOC = '{1}' AND HOC.XEPLOAI = '{2}';
                """.format(res.replace("'", r"\'"), form_namhoc, inputxeploai)
        
        try:
            # Tính thời gian thực hiện truy vấn
            star_2 = time.time()

            # Thực hiện truy vấn
            cursor_2.execute(query_2)

            # Lấy các kết quả vừa truy vấn được
            result_2 = cursor_2.fetchall()

            root = ET.Element("data")

            table_data = []

            # Tạo tiêu đề cho những kết quả in ra terminal
            headers = ["HỌ TÊN", "NTNS", "ĐTB", "XẾP LOẠI", "KẾT QUẢ"]

            # Lấy kết quả vừa truy vấn thành công in ra terminal và file XML tương ứng
            for row in result_2:
                HOTEN = row[0]
                NTNS = row[1].strftime("%Y-%m-%d")
                DIEMTB = row[2]
                XEPLOAI = row[3]
                KQUA = row[4]

                # Ghi vào xml
                student = ET.SubElement(root, "student")
                ET.SubElement(student, "HOTEN").text = HOTEN
                ET.SubElement(student, "NTNS").text = NTNS
                ET.SubElement(student, "DIEMTB").text = str(DIEMTB)
                ET.SubElement(student, "XEPLOAI").text = XEPLOAI
                ET.SubElement(student, "KQUA").text = KQUA

                # Ghi vào danh sách để in ra terminal
                table_data.append([HOTEN, NTNS, DIEMTB, XEPLOAI, KQUA])

            # Giới hạn mỗi lần ghi được 100 dòng
            rows_per_table = 100
            table_data_chunks = [table_data[i:i+rows_per_table] for i in range(0, len(table_data), rows_per_table)]

            # In ra tất cả các kết quả cho từng bảng, mỗi bảng tương ứng 100 dòng 
            for chunk in table_data_chunks:
                print(tabulate(chunk, headers=headers, tablefmt="grid"))
                print("\n----------------------\n")

            # Xử lý file XML
            tree = ET.ElementTree(root)
            xml_str = ET.tostring(root, encoding="utf-8")
            dom = xml.dom.minidom.parseString(xml_str)
            pretty_xml_str = dom.toprettyxml(indent="  ")

            # Lấy đường dẫn của file XML ở thư mục hiện tại lưu vào file Path.txt
            current_directory = os.path.dirname(os.path.abspath(__file__))

            # Định dạng tên file xml
            filename = f"{inputdatabase}-{res}-{form_namhoc}-{inputxeploai}.xml"

            # Tiến hành ghi đường dẫn của xml vào Path.txt
            f.write(current_directory +"\\"+ filename + "\n")

            # Mở file xml và ghi nội dung vừa truy vấn được vào file
            with open(filename, "w", encoding="utf-8") as file:
                file.write(pretty_xml_str)
            print("XML file has been created according to your provided information:", filename)

        # Hiển thị lỗi nếu như quá trình truy vấn xảy ra lỗi
        except pymysql.Error as e:
            print("Error executing query:", str(e))

        cursor_2.close()
        cnx_2.close()   
        end_2 = time.time()

        # Tính toán thời gian thực hiện truy vấn cũng như ghi vào xml
        total_2 = end_2 - star_2

        print(f"Execution time: {total_2}")

    # Nếu người dùng nhập yes thì tiếp tục truy vấn, nếu no thì thoát chương trình và kết thúc
    choice = input("Press Y to continue or N to stop [y/n] ").upper()[:1]
    if choice == "Y":
        continue
    elif choice == "N":
        print("BYE!!!")
        
        # Kết thúc việc đọc và ghi các đường dẫn vào Path.txt
        f.close()
        break


