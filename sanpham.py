class Sanpham: 
    
    def __init__(self, ten_san_pham, gia, giam_gia):
        self.__ten_san_pham = ten_san_pham
        self.__gia = gia
        self.__giam_gia = giam_gia
    def doc_giam_gia(self):
       self.__giam_gia
    def __phi_giam_gia(self, giam_gia_moi):
       self.__giam_gia = giam_gia_moi
    def get_ten_sp (self):
        return self.__ten_san_pham
    def set_ten_sp (self, ten_san_pham_moi):
        self.__ten_san_pham = ten_san_pham_moi
    def get_gia_sp (self):
        return self.__gia
    def set_gia_sp (self, gia_moi):
        self.__gia = gia_moi
    def get_giam_gia (self):
        return self.__giam_gia
    def set_giam_gia (self, giam_gia_moi):
         self.__giam_gia = giam_gia_moi
    def thue_nhap_khau(self):
        return self.__gia * 0.1
    def nhap_thong_tin_sp(self):
        self.__ten_san_pham = input("Nhập tên sản phẩm: ")
        self.__gia = float(input("Nhập giá sản phẩm: "))
        self.__giam_gia = float(input("giam gia: "))
    def xuat_thong_tin_sp(self):
        print(f"Tên sản phẩm: {self.ten_san_pham} có giá {self.gia} và được giảm giá {self.__giam_gia}") 
    def __str__(self):
        return f"Sản phẩm {self.ten_san_pham} có giá {self.gia} và được giảm giá {self.__giam_gia} và thuế nhập khẩu là {self.thue_nhap_khau()}"
    
