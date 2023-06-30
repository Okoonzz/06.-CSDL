import random
from datetime import datetime, timedelta
from openpyxl import Workbook
import pandas as pd
import pymysql
import time

# Nhập vào 1 để bắt đầu sinh dữ liệu 
press = int(input("Press '1' if you want to generate data: "))

if press == 1:
    # Nhập vào mật khẩu MySQL
    password = input("Please enter mysql password: ")
    print("Generating student...")
    ########################################################## MSSV START ###################################################################
    # Random MSSV

    # Random 1000000 MSSV
    MSSV = []
    for i in range(1000000):
        MSSV.append(250000000 + i)

    random.shuffle(MSSV)
    ########################################################## MSSV END ###################################################################


    ########################################################## STUDENT START ###################################################################
    # Random Student

    # Danh sách họ học sinh
    ho = ["Nguyễn", "Trần", "Lê", "Phạm", "Đinh", "Phan", "Hoàng", "Huỳnh", "Phan", "Đỗ", "Đào", "Dương", "Lý", "Hồ", "Ngô", "Vũ", "Võ", "Đặng", 
        "Kiều", "Thái", "Ưng", "Châu", "Tô", "Cao", "Lăng", "Quách", "Khổng", "Văn", "Tuyền", "Kha", "Viễn", "Bồ", "Trịnh", "Chí", "Biện", 
        "Lương", "Bùi", "Ngô", "Phùng", "Hà", "Hữu", "Lai", "Chu", "Xuyến", "Nhâm", "Hoàng", "Chung", "Quang", "Tống", "Phí"]

    # Danh sách tên đệm học sinh
    ten_dem = ["Văn", "Văn Trần", "Thái Thịnh", "Thịnh", "Ngọc", "Ngọc Vân", "Đình", "Thị", "Lê", "Lê Văn",  "Vân", "Vân Đoan", "Ngọc Hân", 
            "Quỳnh Thị", "Võ", "Tấn", "Hải", "Lưu", "Thành Tấn", "Lan", "Vĩnh", "Thanh", "Trung", "Nhật", "Vinh", "Minh", "Trần", "Viết", 
            "Tiến Thành", "Tiến", "Trọng Duy", "Duy", "Gia", "Hoàng", "Thái Hoàng", "Đăng", "Phú", "Huy", "Nhất", "Hà", "Diễm", "Đoan", 
            "Hồng", "Anh", "Hạ", "Chi", "Quế", "Tuyết", "Bích", "Tuệ", "Nhã", "Châu", "Hải", "Ái", "Thiện Nguyễn", "Thiên", "Hướng", "Vàng", 
            "Bạch", "Lệ", "Tường Trí", "Chí", "Hùng", "Nhật", "Quang", "Hán", "Tống Võ", "Mậu", "Trung", "Cao", "Khổng", "Tú", "Bích", "Thoa", "Kim", "Phát", "Lộc", 
            "Liễu", "Quyết", "Văn", "Minh Ngọc", "Quỳnh", "Ái Nguyễn", "Nghiêm Thanh", "Nghiêm", "Trương", "Võ Thành", "Phương Tuyển", "Tuyển", "Ngọc Bầu", "Đài", " Văn Sim", "Sang Hạ", "Ca", 
            "Tính", "Việt", "Khương", "Như", "Tịnh", "Hiệu", "Hinh", "Sáng", "Thìn"]

    # Danh sách tên học sinh
    ten = ["Xuân", "Vân", "Đạt", "Linh", "Kiên", "Phát", "Chánh", "Nam", "Vinh", "Phương", "Bình", "Bảo", "Nguyên", "Đức", "Thịnh", "Mỹ", "Nga", "Nguyệt", "Phi", 
        "Khải", "Thùy", "Đoàn", "Tuấn", "Phong", "Phúc", "Nhi", "Vỹ", "Vi", "Long", "Di", "Ngọc", "Hân", "San", "Thanh", "Thảo", "Thư", "Trang", "Hân", "Duyên", "Ly", 
        "Thương", "Nhường", "Bin", "Hiển", "Khải", "Quốc", "Nghi", "Vũ", "Sam", "Mai", "An", "Khánh", "Tài", "Giang", "Huyền", "Minh", "Vinh", "Tiến", "Khiêm", "Trâm", "Tuyền", "Tý", "Tịnh", "Khoa", "Luân", "Xìn", "Thành", "Đào", "Đô", "Tín", "Bim", 
        "Nghĩa", "Hiệp", "Chương", "Phong", "Thuận", "Sơn", "Phượng", "Tình", "Phấn", "Đại", "Ngân", "Thi", "Cường", "Hưng", "Nhựt", "Liêm", "Nữ", "Trinh", "Tuyến", "Tuyền", "Sang", "Độ", "Tùng", "Lượng", "Ca", "Trí", "Măng", "Muội", "Mùi", "Qúy", "Tin", 
        "Tĩnh", "Thân", "Nguyễn", "Giang", "Kỳ", "Trần", "Trân", "Triều", "Hổ", "Beo", "Liêm", "Thúy", "Mẫn", "Miu", "Vượng", "Xanh"]

    danhSachHo = []
    danhSachTen = []
    for _ in range(1000000):
        hoNgauNhien = random.choice(ho) + " " + random.choice(ten_dem)
        tenNgauNhien = random.choice(ten)
        danhSachHo.append(hoNgauNhien)
        danhSachTen.append(tenNgauNhien)

    # Random họ sinh viên
    random.shuffle(danhSachHo)

    # Random tên sinh viên
    random.shuffle(danhSachTen)
    ########################################################## STUDENT END ###################################################################


    ########################################################## CCCD START #####################################################################
    # Random CCCD

    def GenCCCD(soluong, sochuso):
        numbers = set()  # Dùng set để đảm bảo các số là duy nhất
        while len(numbers) < soluong:
            num = random.randint(10**(sochuso-1), (10**sochuso)-1)  # Sinh số ngẫu nhiên trong khoảng từ 10^(num_digits-1) đến 10^num_digits - 1
            numbers.add(num)
        return list(numbers)

    soluong = 1000000  # Số lượng số cần sinh
    sochuso = 12  # Số chữ số của mỗi số

    # Random cccd có 12 chữ số và khác nhau
    CCCD = GenCCCD(soluong, sochuso)
    ########################################################## CCCD END #####################################################################


    ########################################################## NTNS START ####################################################################
    # Random NTNS

    # Hàm sinh NTNS của học sinh
    def GenNTNS(start, end):
        result = []
        for i in range(1000000):
            delta = end - start
            ranNgay = random.randint(0, delta.days)
            NTN = start + timedelta(days=ranNgay)
            result.append(NTN.strftime("%Y/%m/%d"))
        return result

    start_date = datetime(2003, 1, 1)
    end_date = datetime(2006, 12, 31)

    # Random NTNS bắt đầu từ nagfy 1/1/2003 đến ngày 31/12/2023 và lưu dưới dạng năm/tháng/ngày
    NTNS = GenNTNS(start_date, end_date)
    ########################################################## NTNS END #####################################################################


    ########################################################## ADDRESS START #################################################################
    #Random Address

    # Danh sách tên đường của học sinh
    duongHS = ["685/36 Xô Viết Nghệ Tĩnh", "103 Nguyễn Tiểu La", "18 Tăng Bạt Hổ", "3/51 Thành Thái", "46 Âu Dương Lân", "44 Đường Số 2", "113 Vĩnh Viễn", "Hẻm 3/71 Thành Thái",
            "Hẻm 383/3/45 Quang Trung", "290/56 Nơ Trang Long", "294/22 Xô Viết Nghệ Tĩnh", "131 Đường 3/2", "203 Đường 3/2", "81 Nguyễn Bỉnh Khiêm", "125 Nguyễn Cửu Vân", "408 Nguyễn Xí", "463b/46 Cách Mạng Tháng 8",
            "55 Nguyễn Tư Nghiêm", "144 Lý Chính Thắng", "159 Trần Quốc Thảo", "16/41 Nguyễn Thiện Thuật", "179 Hai Bà Trưng", "Hẻm Số 2 Đường Số 19", "Hẻm 2 Cao Thắng", "202 Trần Quốc Thảo", " 205 Trần Văn Ðang", "548 Tân Kỳ Tân Quý", 
            "Hẻm C Lạc Long Quân", "373/1/44 Lý Thường Kiệt", "942 Trường Chinh", "565/18 Bình Thới", "Đường Nguyễn Thị Nhỏ", "88/10 Hẻm 88", "1041/85 Trần Xuân Soạn", "769/28/13 Phạm Thế Hiển", "316 Hồng Lạc", "35 Phú Thọ", "28 Đường Mai Xuân Thưởng",
            "467/101 Lê Đức Thọ", "175 Dương Tử Giang", "26/19 Nguyễn Văn Vịnh", "35 Đường Trần Bình", "124 Phan Huy Ích", "298/12 Tân Hòa Đông", "Hẻm 217 Bà Hom", "30/32 Đường 100 Bình Thới", "65d1 Hoài Thanh", "1170/52 Đường 3/2", "22 Tống Văn Hên",
            "Hẻm 7 Bà Lài", "1007/11 Lạc Long Quân", "38/25 Cầu Tân Kỳ Tân Quý", "25 Cống Lở", "44 Nguyễn Văn Của", "738 Quốc Lộ 1", "118 Duy Tân", "136 Liên Khu 10-11", "92a1 Phan Huy Ích", "96 Nguyễn Sỹ Sách", "13/19 Trần Văn Hoàng", "100/8 Lương Thế Vinh",
            "118 Bến Phú Định", "252/11 Phan Anh", "99 Đường 702 Hồng Bàng", "572/19/40 Âu Cơ", "161/35 Ni Sư Huỳnh Liên", "76/72 Lê Văn Phan", "17 Đường 277 Minh Phụng", "70/9 Nguyễn Sỹ Sách", "168/13-15 Lê Thị Bạch Cát", "43/25 Phạm Thế Hiển", "213 Hồng Lạc", 
            "69/2 Nguyễn Ngọc Cung", "72/63 Huỳnh Văn Nghệ", "204/131 An Dương Vương", "703/13 Lạc Long Quân", "353 Nguyễn Thái Bình", "180/13 Hồng Châu", "410 Đường Lê Văn Qưới", "47/5e Tân Hóa", "25 Trần Văn Thụ", "58/3 Tân Trang", "86/6 Âu Hồng", "149/20 Bành Văn Trân",
            "227/4 Bông Sao", "7 Trần Thái Tông", "45/2 Đình Nghi", "15 Nguyễn Kiệm", "101 Bùi Minh", "99 Đường Hố Văn", "16 Nghĩa Phát", "18 Phan Đăng", "231 Phạm Thế", "32 Nguyễn Trọng Tuyển", "64 Huỳnh Tịnh", "Đường Đào Trí", "45 Dương Bá Trạc", "22 Đoàn Văn Bơ", "7 Nguyễn Thần Hiến",
            "84 Nguyễn Biểu", "7/10 Cộng Hòa", "9 Thạnh Mỹ Lợi", "10 Thạnh Mỹ", "7 Hồ Biểu Chánh", "2 Cao Đạt", "30 Lê Văn Sỹ", "3 Lê Văn", "45 Tý Đô", "9 Nguyễn Văn Quý", "34 Nguyễn Qúy", "5 Thích Quảng Đức", "25 Tạ Quang", "99 Tạ Quang Bửu", "18 Phạm Hiển", "100/46 Lê Văn Duyệt", "02 Lê Văn Sỹ",
            "35 Đặng Minh Khiêm", "1b/17 Bến Bình Đông", "12 Phong Phú", "32 Phú Phong", "31 Phan Tây Hồ", "8/1 Chu Văn An", "59 Nguyễn Công Hoan", "48 Âu Dương Lân", "32 Đoàn Thị Điểm", "83 Điện Biên", "53 Ba Đình", "26 Trần Kế Xương", "17 Trần Hữu Trang", "37 Cao Xuân Dục"]

    # Danh sách tên quận của học sinh
    quanHS = ["Quận 1", "Quận 2", "Quận 3", "Quận 4", "Quận 5", "Quận 6", "Quận 7", 
            "Quận 8", "Quận 9", "Quận 10", "Quận 11", "Quận 12", "Gò Vấp", "Tân Bình", "Tân Phú", "Hóc Môn", "Bình Chánh", "Phú Nhuận", "Bình Thạnh", "Củ Chi", "Nhà Bè", "Cần Giờ", "Thủ Đức", "Bình Tân", "Diên Khánh", "Cam Ranh", "Khánh Sơn", "Khánh Vĩnh", "Vạn Ninh", "Ninh Hòa", 
            "Hải Châu", "Cẩm Lệ", "Liên Chiểu", "Ngũ Hành Sơn", "Sơn Trà", "Hòa Vang", "Hải Châu", "Phan Rang - Tháp Chàm", "Bác Ái", "Ninh Sơn", "Ninh Hải", "Ninh Phước", "Thuận Bắc", "Thuận Nam",
            "Bảo Lâm", "Cát Tiên", "Di Linh", "Đam Rông", "Đơn Dương", "Đức Trọng", "Lạc Dương", "Lâm Hà", "Sông Cầu", "Đông Hòa", "Phú Thứ", "Trường Sa", "Hoàng Sa", "Tân Đông", "Bình Thảo", "Tống Văn", "Lạc Hồng",
                "Quân Lài", "Lâm Lệ", "Tân Kỳ", "Độc Lập", "Vang Phú", "Môn Châu", "Cầu Trà", "Lương Của", "Kiệt La", "Tĩnh Lân", "Trung Kỳ", "Viễn Lai", "Thái Hào", "Cửu Vân", "Chinh Của", "Khiêm Thảo", "Qúy Hào", "Bạc Hồng", 
                "Lạc Trung", "Linh Nghiêm", "Đà Tiểu", "Bà Đen", "Trọng Quốc", "Phan Đức", "Đam Lý", "Trần Dương", "Long Chiểu", "Viết Ngũ", "Chính Lý", "Tây Nguyễn", "Thái Cao", "Xuân Phước", "Chăm Nhỏ", "Bình Hoài", "Hồng Trai", 
                "Cao Lãnh", "Phan Huỳnh Lý", "Tân Qúy", "Lâm Giang", "Chiến Lương", "Quốc Bảo", "Tam Cơ", "Mậu Thân", "Xa Kỳ", "Dương Bá", "Bông Xuân", "Phát Đăng", "Hồng Minh", "Hố Kiệm", "Trảng Hóa", "Bình Tịnh", "Thế Bạch", "Trần Trâm",
                "Hòa Khởi", "Văn Cư Trinh", "Mai Ngọc", "Văn Tài", "Nguyễn Kiệm", "Huy Tấn"]

    # Danh sách tên tỉnh của học sinh
    tinhHS = ["Khánh Hòa", "TP. Hồ Chí Minh", "Đà Nẵng", "Ninh Thuận", "Lâm Đồng", "Bạc Liêu", "Sóc Trăng", "Kiên Giang", "Cần Thơ", "Quảng Nam"]

    danhsachDC = []
    for _ in range(1000000):
        tenNgauNhiendc = random.choice(duongHS) + ", " + random.choice(quanHS) + ", " + random.choice(tinhHS) + "."
        danhsachDC.append(tenNgauNhiendc)

    # Random địa chỉ của các học sinh
    random.shuffle(danhsachDC)
    ########################################################## ADDRESS END #################################################################

    # Ghi dữ liệu vừa sinh ngẫu nhiên và excel
    wb = Workbook()
    sheet = wb.active

    # Tạo tiêu đề cho mỗi trường trong excel
    sheet[f"A1"] = "MSSV"
    sheet[f"B1"] = "HOSV"
    sheet[f"C1"] = "TENSV"
    sheet[f"D1"] = "CCCD"
    sheet[f"E1"] = "NTNS"
    sheet[f"F1"] = "DIACHI"

    # Tiến hành ghi vào excel
    for i, (mssv, hosv, tensv, socccd, ntns, dc) in enumerate( zip(MSSV, danhSachHo, danhSachTen, CCCD, NTNS, danhsachDC), start=2):
        # Mã học sinh bắt đầu bằng "HSXXXXXXXXX"
        sheet[f"A{i}"] = f"HS{mssv}"
        sheet[f"B{i}"] = hosv
        sheet[f"C{i}"] = tensv
        sheet[f"D{i}"] = socccd
        sheet[f"E{i}"] = ntns
        sheet[f"F{i}"] = dc


    wb.save(r"DanhSachTenHS.xlsx")

    print("Done!!!")

    ############################################################################ RANDOM SCHOOL ############################################################################

    # Random School
    print("Generating school...")

    # Danh sách các họ của trường
    hot = ["Nguyễn", "Trần", "Lê", "Phạm", "Đinh", "Phan", "Hoàng", "Huỳnh", "Phan", "Đỗ", "Đào", "Dương", "Lý", "Hồ", "Ngô", "Vũ", "Võ", "Đặng", "Lương", "Mẫn", "Hà", "Trương"]

    ten_dem_truong = ["Văn", "Thịnh", "Ngọc", "Lê", "Hồng", "Vân", "Thị", "Mười", "Quỳnh", "Vĩnh", "Tấn", "Văn", "Thế", "Long", "Nga", "Đức", "Linh", "Ngân", "Chính", "Tuyền", "Vương", "Chiến", "Mảnh", "Son", "Sính", "Đồng", "Bén"]

    # Danh sách tên trường
    ten_truong = ["Định", "An", "Hải", "Quân", "Vinh", "Cơ", "Bình", "Xuân", "Mỹ", "Lộc", "Tài", "Bưởi", "Tư", "Tuyền", "Ninh", "Vạn", "Trúc", "Phong", "Tuyến", "Hiệu", "Thịnh", "Thu", "Hạ", "Đông", "Thiện", "Thắm", "Thiên", "Luân", "Hùng"]

    # Danh sách quận
    quan = ["Quận 1", "Quận 2", "Quận 3", "Quận 4", "Quận 5", "Quận 6", "Quận 7", "Quận 8", "Quận 9", "Quận 10", "Quận 11", "Quận 12", "Gò Vấp", "Tân Bình", "Tân Phú", "Hóc Môn", "Bình Chánh", "Phú Nhuận", "Bình Thạnh", "Củ Chi", "Nhà Bè", "Cần Giờ", "Thủ Đức", "Bình Tân"]

    # Danh sách tên đường
    duong = ["22 Nguyễn Gia Trí,", "14 Lê Thành Phương,", "107 Nguyên Hồng,", "40 Phú Mỹ,", "Đường số 1,", "42 Bà Hạt,", "Đường số 64,", "250 Nguyễn Xí,", "232 Ngô Gia Tự,", "16 Hòa Hưng,", "114 Bùi Đình Túy,", "322 Vĩnh Viễn,", "461 Bạch Đằng,", "407 Sư Vạn Hạnh,", "413 Lê Hồng Phong,", "1404 Lê Đức Thọ,", "458 Nhật Tảo,", "118 Lê Lợi,", "19 Thiên Hộ Dương,", "11 Phạm Văn Chiêu,", "95 Nơ Trang Long,", "818 Xô Viết Nghệ Tĩnh,", "145 Phan Văn Trị,", "122 Trần Tuấn Khải,", "16 Vũ Ngọc Phan,", "458 Lý Thái Tổ,", "74 Phạm Ngũ Lão,", "163 Tân Phước,", "8 Đinh Bộ Lĩnh,", "41 Thích Bửu Đăng,", "113 Trương Đăng Quế,", "8/17 Võ Duy Ninh,", "249 Nguyễn Duy Dương,", "233 Nguyễn Duy Cung,", "71/9 Phú Mỹ,", "57 Lam Sơn,", "436/78 Trần Văn Đang,", "Hiệp Thành 42,", "84/28 Lý Thường Kiệt,", "24 Trần Quốc Tuấn,", "140 Nguyễn Tiểu La,", "72 Phú Mỹ Hưng", "53 Phú Mỹ", "78 Hưng Phú"]

    # Random tên trường, địa chỉ
    danh_sach = [f"{h} {tdt} {tt}" for h in hot for tdt in ten_dem_truong for tt in ten_truong]
    dia_chi = [f"{dg} {qn}" for dg in duong for qn in quan]

    random.shuffle(danh_sach)
    random.shuffle(dia_chi)

    # Lấy địa chỉ và tên của 100 trường
    ds = danh_sach[:100]
    dc = dia_chi[:100]

    # Random mã cho 100 trường 
    MaTruong = []
    for i in range(100, 200):
        MaTruong.append(30000 + i)
    random.shuffle(MaTruong)

    # Ghi dữ liệu vừa sinh được vào excel
    wb = Workbook()
    sheet = wb.active

    # Tạo tiêu đề cho excel
    sheet["A1"] = "MA_TRUONG"
    sheet["B1"] = "TENTRUONG"
    sheet["C1"] = "DIACHI"

    # Tiến hành ghi mã trường, tên trường và địa chỉ vào excel
    for j, (matruong, tent, diachi) in enumerate(zip(MaTruong, ds, dc), start=2):
        # Mã trường bắt đầu bằng "TRXX"
        sheet[f"A{j}"] = f"TR{matruong}"
        sheet[f"B{j}"] = f"THPT {tent}"
        sheet[f"C{j}"] = f"{diachi}, Hồ Chí Minh."

    wb.save(r"DanhSachTenTruong.xlsx")
    
    print("Done!!!")

    ############################################################################ END RANDOM ############################################################################
    print("Data generation is complete!")
    ############################################################################ START CONNECT ############################################################################
    print("Generating connect...")

    # Tạo bảng "HOC" làm bảng kết nối hai bảng trường và học sinh
    datafolderHS = r"DanhSachTenHS.xlsx"
    datafolderTR = r"DanhSachTenTruong.xlsx"

    # Lấy dữ liệu từ bảng trường và bảng học sinh
    TR = pd.read_excel(datafolderTR)
    HS = pd.read_excel(datafolderHS)

    data_list = []

    # Gắn cho mỗi học sinh đều có trường, điểm trung bình, xếp loại, kết quả, NTNS
    for i in range(len(HS)):
        matruong = random.choice(TR["MA_TRUONG"])
        # Nếu sinh năm 2006 thì chỉ có từ 1 đên 2 dòng. Còn không phải thì từ 1 đến 3 dòng. Tất cả đều được random theo tỷ lệ nhất định
        num_iterations = random.choices([1, 2], [20, 80])[0] if int(HS['NTNS'][i][:4]) == 2006 else random.choices([1, 2, 3], [5, 15, 80])[0]
        for stt in range(num_iterations):
            # Random điểm trung bình từ 2 đến 10 và làm tròn đến 1 chữ số phần thập phân
            dtb = round(random.uniform(2, 10), 1)
            data = {
                "MA_TRUONG": matruong,
                "MSSV": HS['MSSV'][i],
                "NTNS": HS['NTNS'][i],
                # Tính toán năm học của từng học sinh
                "NAMHOC": f"{int(HS['NTNS'][i][:4]) + 15 + stt} - {int(HS['NTNS'][i][:4]) + 15 + stt + 1}",
                "DTB": dtb,
                "XEPLOAI": "",
                "KETQUA": ""
            }
            # Phân loại xếp loại và kết quả tương ứng với điểm
            if 9 <= dtb <= 10:
                data["XEPLOAI"] = "Xuất sắc"
                data["KETQUA"] = "Hoàn thành"
            elif 8 <= dtb < 9:
                data["XEPLOAI"] = "Giỏi"
                data["KETQUA"] = "Hoàn thành"
            elif 6.5 <= dtb < 8:
                data["XEPLOAI"] = "Khá"
                data["KETQUA"] = "Hoàn thành"
            elif 4.5 <= dtb < 6.5:
                data["XEPLOAI"] = "Trung bình"
                data["KETQUA"] = "Hoàn thành"
            else:
                data["XEPLOAI"] = "Yếu"
                data["KETQUA"] = "Chưa hoàn thành"
            data_list.append(data)

    # Ghi dữ liệu vào file csv
    df = pd.DataFrame(data_list)
    df.to_csv("DanhSachHoc.csv", index=False)

    print("Done!!!")
    ############################################################################ END CONNECT ############################################################################
    print("Generating file Data.sql...")

    ############################################################################ START SQL ############################################################################
    datafolderTR = r"DanhSachTenTruong.xlsx"
    datafolderSV = r"DanhSachTenHS.xlsx"
    datafolderHoc = r"DanhSachHoc.csv"
    # Tạo file SQL gồm các câu lệnh để insert vào với dữ liệu vừa sinh được
    output = open("Data.sql", "w", encoding="utf-8-sig")

    # Tạo các câu lệnh để thêm vào bảng trường
    def insert_truong():
        truong = pd.read_excel(datafolderTR)
        for i in range(len(truong)):
            print(f"INSERT INTO TRUONG VALUES(N'{truong['MA_TRUONG'][i]}', N'{truong['TENTRUONG'][i]}', N'{truong['DIACHI'][i]}');", file=output)

    # Tạo các câu lệnh để thêm vào bảng học sinh
    def insert_sinhvien():
        sv = pd.read_excel(datafolderSV)
        for i in range(len(sv)):
            print(f"INSERT INTO HS VALUES (N'{sv['MSSV'][i]}', N'{sv['HOSV'][i]}', N'{sv['TENSV'][i]}', N'{sv['CCCD'][i]}', '{sv['NTNS'][i]}', N'{sv['DIACHI'][i]}');", file=output)

    # Tạo các câu lệnh để thêm vào bảng học
    def insert_hoc():
        hoc = pd.read_csv(datafolderHoc)
        for i in range(len(hoc)):
            print(f"INSERT INTO HOC VALUES (N'{hoc['MA_TRUONG'][i]}', N'{hoc['MSSV'][i]}', '{hoc['NAMHOC'][i]}', {hoc['DTB'][i]}, N'{hoc['XEPLOAI'][i]}', N'{hoc['KETQUA'][i]}');", file=output)

    # Thực thi các hàm để tiến hành tạo lệnh
    insert_truong()
    insert_sinhvien()
    insert_hoc()

    print("Finished all random data generation ^^")
    ############################################################################ END SQL ############################################################################
    print("Adding to the database...")
    ############################################################################ START CONNECT SQL ############################################################################
    # Kết nối với SQL và tiến hành insert từ file SQL vừa sinh ra với TRUONGHOC1
    def TRUONGHOC1():
        cnx = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = f'{password}',
            database = 'TRUONGHOC1'
        )

        cursor = cnx.cursor()

        # Mở file SQL vừa tạo 
        with open("Data.sql", "r", encoding="utf-8-sig") as file:
            for line in file.readlines():
                line = line.strip()
                if line and line.startswith("INSERT"):
                    # Thực thi từng câu lệnh trong file SQL
                    cursor.execute(line)

        cnx.commit()
        cursor.close()
        cnx.close()

     # Kết nối với SQL và tiến hành insert từ file SQL vừa sinh ra với TRUONGHOC2
    def TRUONGHOC2():
        cn2 = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = f'{password}',
            database = 'TRUONGHOC2'
        )

        cursor = cn2.cursor()

        # Mở file SQL vừa tạo
        with open("Data.sql", "r", encoding="utf-8-sig") as file:
            for line in file.readlines():
                line = line.strip()
                if line and line.startswith("INSERT"):
                    # Thực thi từng câu lệnh trong SQL
                    cursor.execute(line)

        cn2.commit()
        cursor.close()
        cn2.close()
    ############################################################################ END CONNECT SQL ############################################################################

    start_time1 = time.time()
    TRUONGHOC1()
    end_time1 = time.time()

    # Tính toán thời gian insert vào TRUONGHOC1
    execution_time1 = end_time1 - start_time1

    start_time2 = time.time()
    TRUONGHOC2()
    end_time2 = time.time()

    # Tính toán thời gian insert vào TRUONGHOC2
    execution_time2 = end_time2 - start_time2

    # Chuyển đổi thời gian vừa tính được sang giờ, phút, giây
    hours_1 = int(execution_time1 // 3600)
    minutes_1 = int((execution_time1 % 3600) // 60)
    seconds_1 = int(execution_time1 % 60)

    hours_2 = int(execution_time2 // 3600)
    minutes_2 = int((execution_time2 % 3600) // 60)
    seconds_2 = int(execution_time2 % 60)

    print("Done!!!")
    
    # Thời gian thực hiện insert vào TRUONGHOC1
    print(f"Execution time_1: {hours_1} hour {minutes_1} min {seconds_1} sec")

    # Thời gian thực hiện insert vào TRUONGHOC2
    print(f"Execution time_2: {hours_2} hour {minutes_2} min {seconds_2} sec")

else:
    # Nếu không nhấn 1 thì sẽ thoát chương trình
    print("Looks like you don't want to generate data automatically :(( ")