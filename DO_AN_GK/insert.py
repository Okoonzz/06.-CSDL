import pandas as pd
import os

# Duong dan data va dau ra sau khi insert
datafolder = 'D:\DOAN\data.xlsx'
output = open("Data.sql", "w", encoding="utf-8-sig")

# Cac ham insert


def insert_So():
    # print("--TABLE SO,", file=output)
    so = pd.read_excel(datafolder, sheet_name="SO")
    # print(so)
    for i in range(len(so)):
        print("INSERT INTO SO VALUES ({}, N'{}');".format(
            so["ID_SOGD"][i], so["TEN_SOGD"][i]), file=output)
    # print("--END DATA,", file=output)


def insert_Phong():
    # print("--TABLE PHONG_GD,", file=output)
    phong = pd.read_excel(datafolder, sheet_name="PHONG")
    for i in range(len(phong)):
        print("INSERT INTO PHONGGD VALUES ({}, N'{}', {});".format(
            phong["ID_PHONGGD"][i], phong["TEN_PHONGGD"][i], phong["ID_SOGD"][i]), file=output)
    # print("--END DATA,", file=output)


def insert_LOAIT():
    # print("--TABLE LOAI_TRUONG,", file=output)
    lt = pd.read_excel(datafolder, sheet_name="LOAITRUONG")
    for i in range(len(lt)):
        print("INSERT INTO LOAIT VALUES ({}, N'{}');".format(
            lt["ID_LOAITRUONG"][i], lt["TEN_LOAITRUONG"][i]), file=output)
    # print("--END DATA,", file=output)


def insert_LOAIH():
    # print("--TABLE LOAI_HINH,", file=output)
    lh = pd.read_excel(datafolder, sheet_name="LOAIHINH")
    for i in range(len(lh)):
        print("INSERT INTO LOAIH VALUES ({}, N'{}');".format(
            lh["ID_LOAIHINH"][i], lh["TEN_LOAHINH"][i]), file=output)
    # print("--END DATA,", file=output)


def insert_CAP():
    # print("--TABLE CAP,", file=output)
    cap = pd.read_excel(datafolder, sheet_name="CAP")
    for i in range(len(cap)):
        print("INSERT INTO CAP VALUES (N'{}', N'{}');".format(
            cap["ID_CAP"][i], cap["CAP"][i]), file=output)
    # print("--END DATA,", file=output)


def check(checkPHG):
    if (checkPHG == "THPT") | (checkPHG == "GDTX"):
        return False
    else:
        return True


def insert_TRUONG():
    # print("--TABLE TRUONG,", file=output)
    cap = pd.read_excel(datafolder, sheet_name="CAP")
    for i in range(len(cap)):
        cap_thu = cap["ID_CAP"][i]
        # print(type(cap_thu))
        data = pd.read_excel(datafolder, sheet_name=cap_thu)
        for j in range(len(data)):
            ma_truong = data["MATRUONG"][j]
            ten_truong = data["TENTRUONG"][j]
            id_sogd = data["ID_SOGD"][j] if pd.notnull(
                data["ID_SOGD"][j]) else "NULL"
            dia_chi = data["DIACHI"][j] if pd.notnull(
                data["DIACHI"][j]) else "NULL"
            lh = data["ID_LOAIHINH"][j] if pd.notnull(
                data["ID_LOAIHINH"][j]) else "NULL"
            lt = data["ID_LOAITRUONG"][j] if pd.notnull(
                data["ID_LOAITRUONG"][j]) else "NULL"
            id_phong = "NULL"
            if check(cap_thu):
                id_phong = data['ID_PHONGGD'][j] if pd.isnull(
                    data['ID_PHONGGD'][j]) == False else "NULL"
            print("INSERT INTO TRUONG VALUES (N'{}', N'{}', N'{}', N'{}', {}, {}, {}, {});".format(
                ma_truong, ten_truong,dia_chi,cap_thu,lt,lh,  id_sogd, id_phong), file=output)
    # print("--END DATA,", file=output)


insert_So()
insert_Phong()
insert_LOAIT()
insert_LOAIH()
insert_CAP()
insert_TRUONG()
