
# Nhập các thành phần cần thiết từ thư viện tkinter
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button, Style

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
        self.parent.title("Quit button")
        
        # Tạo một đối tượng Style để thiết lập giao diện người dùng
        self.style = Style()
        self.style.theme_use("default")

        # Bố trí (layout) Frame để điền vào toàn bộ cửa sổ và mở rộng
        self.pack(fill=BOTH, expand=1)
        
        # Tạo một nút "Quit" và thiết lập hàm gọi khi nút này được nhấn
        quitButton = Button(self, text="Quit", command=self.quit)
        
        # Đặt vị trí của nút "Quit" trên Frame
        quitButton.place(x=60, y=50)

# Tạo một cửa sổ gốc (root window) sử dụng lớp Tk
root = Tk()

# Đặt kích thước và vị trí ban đầu của cửa sổ
root.geometry("250x150+300+300")

# Tạo một đối tượng Example với cửa sổ gốc làm đối số
app = Example(root)

# Bắt đầu vòng lặp chính của ứng dụng để hiển thị cửa sổ
root.mainloop()

