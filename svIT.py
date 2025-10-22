class SinhVienIT:
    def __init__(self, ma_sv, ho_ten, diem_java, diem_html, diem_css):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.diem_java = diem_java
        self.diem_html = diem_html
        self.diem_css = diem_css

    def nhap_thong_tin_sv(self):
        self.ma_sv = input("Nhập mã số sinh viên: ")
        self.ho_ten = input("Nhập họ tên sinh viên: ")
        self.diem_java = float(input("Nhập điểm Java: "))
        self.diem_html = float(input("Nhập điểm HTML: "))
        self.diem_css = float(input("Nhập điểm CSS: "))

    def get_diem(self):
        return (self.diem_java * 2 + self.diem_html + self.diem_css) / 4
    
    def get_hoc_luc(self):
        if self.__diem < 5:
            return "Yếu"
        elif 5 <= self.__diem < 7:
            return "Trung bình"
        elif 7 <= self.__diem < 8:
            return "Khá"
        elif 8 <= self.__diem < 9:
            return "Giỏi"
        else:
            return "Xuất sắc"
    
    def xuat_thong_tin_sv(self):
        print(f"Mã SV: {self.ma_sv}")
        print(f"Họ tên: {self.ho_ten}")
        print(f"Điểm Java: {self.diem_java}")
        print(f"Điểm HTML: {self.diem_html}")
        print(f"Điểm CSS: {self.diem_css}")

class SinhVienBiz:
    def __init__(self, ma_sv, ho_ten, diem_maketing, diem_sales):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.diem_maketing = diem_maketing
        self.diem_sales = diem_sales

    def nhap_thong_tin_sv(self):
        self.ma_sv = input("Nhập mã số sinh viên: ")
        self.ho_ten = input("Nhập họ tên sinh viên: ")
        self.diem_maketing = float(input("Nhập điểm Maketing: "))
        self.diem_sales = float(input("Nhập điểm Sales: "))

    def get_diem(self):
        return (self.diem_maketing * 2 + self.diem_sales) / 3
    
    def get_hoc_luc(self):
        if self.__diem < 5:
            return "Yếu"
        elif 5 <= self.__diem < 7:
            return "Trung bình"
        elif 7 <= self.__diem < 8:
            return "Khá"
        elif 8 <= self.__diem < 9:
            return "Giỏi"
        else:
            return "Xuất sắc"
    def xuat_thong_tin_sv(self):
        print(f"Mã SV: {self.ma_sv}")
        print(f"Họ tên: {self.ho_ten}")
        print(f"Điểm Maketing: {self.diem_maketing}")
        print(f"Điểm Sales: {self.diem_sales}")
