CREATE DATABASE IF NOT EXISTS `TRUONGHOC2`;
USE `TRUONGHOC2`;
SET GLOBAL max_allowed_packet = 1024 * 1024 * 525;
CREATE TABLE `TRUONG`(
    `MATR` NVARCHAR(225) NOT NULL,
    `TENTR` NVARCHAR(225) NOT NULL,
    `DCHITR` NVARCHAR(225) NOT NULL,
    PRIMARY KEY (`MATR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE INDEX `idx_tentr` ON TRUONGHOC2.TRUONG (`TENTR`);

CREATE TABLE `HS`(
    `MAHS` NVARCHAR(225) NOT NULL, 
    `HO` NVARCHAR(225) NOT NULL,
    `TEN` NVARCHAR(225) NOT NULL,
    `CCCD` NVARCHAR(225) NOT NULL,
    `NTNS` DATE NOT NULL,
    `DCHI_HS` NVARCHAR(225) NOT NULL,
    PRIMARY KEY(`MAHS`),
    UNIQUE(`CCCD`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `HOC`(
    `MATR` NVARCHAR(225) NOT NULL,
    `MAHS` NVARCHAR(225) NOT NULL,
    `NAMHOC` NVARCHAR(225) NOT NULL,
    `DIEMTB` FLOAT,
    `XEPLOAI` NVARCHAR(225) NOT NULL,
    `KQUA` NVARCHAR(225) NOT NULL,
    PRIMARY KEY(`MATR`, `MAHS`, `NAMHOC`),
    FOREIGN KEY(`MAHS`) REFERENCES HS(`MAHS`),
    FOREIGN KEY(`MATR`) REFERENCES TRUONG(`MATR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE INDEX `idx_xeploai` ON TRUONGHOC2.HOC (`XEPLOAI`);
CREATE INDEX `idx_namhoc` ON TRUONGHOC2.HOC (`NAMHOC`);