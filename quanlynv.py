import json
import nhanvien  # file nhanvien.py bạn đã có ở trên

class QuanLiNV:
    File_Name = "danhsach_nhanvien.json"

    def __init__(self):
        self.dsnv = []

    def them_nhan_vien(self):
        ma_nv = input("Nhập mã nhân viên: ")
        ho_ten = input("Nhập họ tên: ")
        tuoi = int(input("Nhập tuổi: "))
        he_so_luong = float(input("Nhập hệ số lương: "))
        loai = input("Loại nhân viên (NhanVien/TiepThi/TruongPhong): ").strip()
    
        if loai == "TiepThi":
            ds = float(input("Nhập doanh số: "))
            hh = float(input("Nhập hoa hồng: "))
            nv = nhanvien.TiepThi(ma_nv, ho_ten, tuoi, he_so_luong, ds, hh)
        elif loai == "TruongPhong":
            pc = float(input("Nhập phụ cấp: "))
            nv = nhanvien.TruongPhong(ma_nv, ho_ten, tuoi, he_so_luong, pc)
        else:
            nv = nhanvien.NhanVien(ma_nv, ho_ten, tuoi, he_so_luong)

        self.dsnv.append(nv)
        self.ghi_file()
        print("Đã lưu danh sách vào file thành công!")

    def ghi_file(self):
        data = [nv.to_dict() for nv in self.dsnv]
        with open(self.File_Name, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def doc_file(self):
        try:
            with open(self.File_Name, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.dsnv = []
            for nv in data:
                loai = nv.get("loai", "NhanVien")
                if loai == "TiepThi":
                    nhan_vien = nhanvien.TiepThi(
                        nv["ma_nv"], nv["ho_ten"], nv["tuoi"],
                        nv["he_so_luong"], nv["doanh_so"], nv["hoa_hong"]
                    )
                elif loai == "TruongPhong":
                    nhan_vien = nhanvien.TruongPhong(
                        nv["ma_nv"], nv["ho_ten"], nv["tuoi"],
                        nv["he_so_luong"], nv["phu_cap"]
                    )
                else:
                    nhan_vien = nhanvien.NhanVien(
                        nv["ma_nv"], nv["ho_ten"], nv["tuoi"], nv["he_so_luong"]
                    )
                self.dsnv.append(nhan_vien)

            print("Đọc file thành công! Danh sách nhân viên: ")
            for nv in self.dsnv:
                print(nv)

        except FileNotFoundError:
            print("File chưa tồn tại!")

    def tim_nhan_vien_theo_ma(self):
        ma_tim = input("Nhập mã nhân viên cần tìm: ")
        for nv in self.dsnv:
            if nv.ma_nv == ma_tim:
                print(f"Đã tìm thấy: {nv}")
                return nv
        print(f"Không tìm thấy nhân viên mã {ma_tim}")
        return None
    
    def xoa_nhan_vien(self):
        nv = self.tim_nhan_vien_theo_ma()
        if nv:
            self.dsnv.remove(nv)
            self.ghi_file()
            print("Đã xóa nhân viên và cập nhật file!")

    def cap_nhat_nhan_vien(self):
        nv = self.tim_nhan_vien_theo_ma()
        if nv:
            print("Nhập thông tin mới (để trống nếu không thay đổi):")
            ho_ten_moi = input("Họ tên mới: ")
            tuoi_moi = input("Tuổi mới: ")
            he_so_luong_moi = input("Hệ số lương mới: ")

            if ho_ten_moi:
                nv.ho_ten = ho_ten_moi
            if tuoi_moi:
                nv.tuoi = int(tuoi_moi)
            if he_so_luong_moi:
                nv.he_so_luong = float(he_so_luong_moi)

            self.ghi_file()
            print("Đã cập nhật thông tin nhân viên.")

    def sap_xep_theo_ho_ten(self):
        self.dsnv.sort(key=lambda nv: nv.ho_ten)
        print("Danh sách sau khi sắp xếp theo họ tên:")
        for nv in self.dsnv:
            print(nv)

    def sap_xep_theo_thu_nhap(self):
        self.dsnv.sort(key=lambda x: x.get_thu_nhap(), reverse=True)
        print("Danh sách theo thu nhập giảm dần:")
        for nv in self.dsnv:
            print(nv)

    def top5_thu_nhap(self):
        ds_sap_xep = sorted(self.dsnv, key=lambda nv: nv.get_thu_nhap(), reverse=True)
        print("Top 5 nhân viên thu nhập cao nhất:")
        for nv in ds_sap_xep[:5]:
            print(nv)