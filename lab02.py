from PIL import Image, ImageTk
import tkinter as tk
from tkinter.ttk import Frame, Style, Label

# Định nghĩa lớp Example kế thừa từ lớp Frame
class Example(Frame):
    # Phương thức khởi tạo của lớp Example
    def __init__(self, parent):
        # Gọi phương thức khởi tạo của lớp cha (Frame)
        Frame.__init__(self, parent)
        
        # Gán tham chiếu đến cửa sổ gốc (Tkinter) cho biến self.parent
        self.parent = parent
        
        # Gọi phương thức initUI() để tạo giao diện người dùng
        self.initUI()

    # Phương thức tạo giao diện người dùng
    def initUI(self):
        # Đặt tiêu đề cho cửa sổ
        self.parent.title("Absolute positioning")
        
        # Bố trí (layout) Frame để điền vào toàn bộ cửa sổ và mở rộng
        self.pack(fill=tk.BOTH, expand=1)

        # Thiết lập một Style cho Frame để đặt màu nền
        Style().configure("TFrame", background="#333")

        # Mở và thay đổi kích thước ảnh "download.jfif", sau đó chuyển thành đối tượng PhotoImage
        bard = Image.open("c:\\2115200_LuongTuanDuy\\download.jfif")
        width, height = 100, 200
        bard = bard.resize((width, height), Image.DEFAULT_STRATEGY)  
        bardejov = ImageTk.PhotoImage(bard)
        
        # Tạo một Label để hiển thị ảnh "download.jfif"
        label1 = Label(self, image=bardejov)
        label1.image = bardejov  # Đảm bảo tham chiếu ảnh được giữ lại
        label1.place(x=20, y=20)  # Đặt vị trí của label trên Frame

        # Tương tự cho ảnh thứ hai (đổi đường dẫn và vị trí)
        img2 = Image.open("c:\\2115200_LuongTuanDuy\\download1.jfif")
        width, height = 100, 200
        img2 = img2.resize((width, height), Image.DEFAULT_STRATEGY)  
        img2_tk = ImageTk.PhotoImage(img2)
        label2 = Label(self, image=img2_tk)
        label2.image = img2_tk
        label2.place(x=150, y=20)

        # Và cho ảnh thứ ba (đổi đường dẫn và vị trí)
        img3 = Image.open("c:\\2115200_LuongTuanDuy\\download2.jfif")
        width, height = 100, 200
        img3 = img3.resize((width, height), Image.DEFAULT_STRATEGY)  
        img3_tk = ImageTk.PhotoImage(img3)
        label3 = Label(self, image=img3_tk)
        label3.image = img3_tk
        label3.place(x=280, y=20)

# Tạo một cửa sổ gốc (root window) sử dụng lớp Tk
root = tk.Tk()

# Đặt kích thước và vị trí ban đầu của cửa sổ
root.geometry("500x280+300+300")

# Tạo một đối tượng Example với cửa sổ gốc làm đối số
app = Example(root)

# Bắt đầu vòng lặp chính của ứng dụng để hiển thị cửa sổ
root.mainloop()

