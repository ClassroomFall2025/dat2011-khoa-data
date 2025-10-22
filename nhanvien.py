class NhanVien:
    luongcoban = 9000000  # Lương cơ bản
    def __init__(self, ma_nv, ho_ten, tuoi, he_so_luong):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.he_so_luong = he_so_luong

    def get_thu_nhap(self):
        return self.he_so_luong * 9000000
    def to_dict(self):
        return {
            "loai": "NhanVien",
            "ma_nv": self.ma_nv,
            "ho_ten": self.ho_ten,
            "tuoi": self.tuoi,
            "he_so_luong": self.he_so_luong
        }

    def __str__(self):
        return f"{self.ma_nv} - {self.ho_ten} - Thu nhập: {self.get_thu_nhap():,.0f} VND"


class TiepThi(NhanVien):
    def __init__(self, ma_nv, ho_ten, tuoi, he_so_luong, doanh_so, hoa_hong):
        super().__init__(ma_nv, ho_ten, tuoi, he_so_luong)
        self.doanh_so = doanh_so
        self.hoa_hong = hoa_hong

    def get_thu_nhap(self):
        # Tổng thu nhập = Lương cơ bản * HSL + doanh số * hoa hồng
        return self.luong_co_ban * self.he_so_luong + self.doanh_so * self.hoa_hong
    def to_dict(self):
        d = super().to_dict()
        d.update({
            "loai": "TiepThi",
            "doanh_so": self.doanh_so,
            "hoa_hong": self.hoa_hong
        })
        return d

class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, tuoi, he_so_luong, phu_cap):
        super().__init__(ma_nv, ho_ten, tuoi, he_so_luong)
        self.phu_cap = phu_cap

    def get_thu_nhap(self):
        # Tổng thu nhập = Lương cơ bản * HSL + phụ cấp
        return self.luong_co_ban * self.he_so_luong + self.phu_cap

    def to_dict(self):
            d = super().to_dict()
            d.update({
                "loai": "TruongPhong",
                "phu_cap": self.phu_cap
            })
            return d