class SinhvienPoly:
    def __init__(self,ten,ma_sv,diem):
        self.__ten = ten
        self.__ma_sv = ma_sv
        self.__diem = diem
    def get_ten(self):
        return self.__ten
    def get_ma_sv(self):
        return self.__ma_sv
    def get_diem(self):
        return self.__diem
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
    def nhap_thong_tin_sv(self):
        self.__ten = input("Nhập tên sinh viên: ")
        self.__ma_sv = input("Nhập mã sinh viên: ")
        self.__diem = float(input("Nhập điểm sinh viên: "))
    def xuat(self):
        print(f"Sinh viên: {self.__ten} - Mã SV: {self.__ma_sv} - Điểm: {self.__diem} - Học lực: {self.get_hoc_luc()}")
        