import tkinter as tk
from tkinter import messagebox
import re
import pandas as pd

def validate_student_id():
    student_id = student_id_entry.get()
    if not student_id.isdigit() or len(student_id) != 7:
        messagebox.showerror("Lỗi", "Mã số sinh viên không hợp lệ. Vui lòng nhập đúng 7 số.")
        return False
    return True
                             
def validate_email():
    email = email_entry.get()
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        messagebox.showerror("Lỗi", "Email không hợp lệ. Vui lòng kiểm tra lại.")
        return False
    return True

def validate_phone():
    phone = phone_entry.get()
    if not phone.isdigit() or len(phone) != 10:
        messagebox.showerror("Lỗi", "Số điện thoại không hợp lệ. Vui lòng nhập đúng 10 số.")
        return False
    return True

def validate_semester():
    semester = semester_entry.get()
    if semester not in ['1', '2', '3']:
        messagebox.showerror("Lỗi", "Học kỳ không hợp lệ. Vui lòng nhập 1, 2 hoặc 3.")
        return False
    return True

def validate_birthdate():
    birthdate = birthdate_entry.get()
    if not re.match(r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$', birthdate):
        messagebox.showerror("Lỗi", "Ngày sinh không hợp lệ. Vui lòng nhập đúng định dạng dd/mm/yyyy.")
        return False
    return True

def validate_year():
    year = year_var.get()
    if year not in ['2022-2023', '2023-2024', '2024-2025']:
        messagebox.showerror("Lỗi", "Năm học không hợp lệ. Vui lòng chọn từ danh sách.")
        return False
    return True

def register():
    if not (validate_student_id() and validate_email() and validate_phone() and 
            validate_semester() and validate_birthdate() and validate_year()):
        return
    
    # Lưu thông tin vào tệp tin Excel
    data = {
        'Mã số sinh viên': [student_id_entry.get()],
        'Email': [email_entry.get()],
        'Số điện thoại': [phone_entry.get()],
        'Học kỳ': [semester_entry.get()],
        'Ngày sinh': [birthdate_entry.get()],
        'Năm học': [year_var.get()],
        'Môn học': [subject_var.get()]
    }

    df = pd.DataFrame(data)
    df.to_excel('student_info.xlsx', index=False)

    messagebox.showinfo("Thông báo", "Đăng ký thành công!")

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Đăng ký môn học")

# tHÔNG BÁO ĐỎ ĐỎ 
TB_label= tk.Label(root,text= "THÔNG BÁO ĐĂNG KÝ HỌC PHẦN"  )
TB_label= tk.Entry(root)

# Label và Entry cho Mã số sinh viên
student_id_label = tk.Label(root, text="Mã số sinh viên:")
student_id_label.grid(row=0, column=0, padx=(10, 0), pady=(10, 0))
student_id_entry = tk.Entry(root)
student_id_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 0))

# Label và Entry cho Email
email_label = tk.Label(root, text="Email:")
email_label.grid(row=1, column=0, padx=(10, 0))
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=(0, 10))

# Label và Entry cho Số điện thoại
phone_label = tk.Label(root, text="Số điện thoại:")
phone_label.grid(row=2, column=0, padx=(10, 0))
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1, padx=(0,10))

# Label và Entry cho Học kỳ 
semester_label = tk.Label(root, text="Học kỳ:")
semester_label.grid(row=3, column=0, padx=(10, 0))
semester_entry = tk.Entry(root)
semester_entry.grid(row=3, column=1, padx=(0,10))
# cho Ngày Sinh
birthdate_label = tk.Label(root, text="Ngày sinh( dd/mm.yyyy):")
birthdate_label.grid(row=4, column=0, padx=(10, 0))
birthdate_entry = tk.Entry(root)
birthdate_entry.grid(row=4, column=1, padx=(0,10))
#cho Năm học

year_label = tk.Label(root, text="Năm học:")
year_label.grid(row=5, column=0, padx=(10, 0))
year_var = tk.StringVar(root)
year_var.set('2022-2023')
year_option_menu = tk.OptionMenu(root,year_var, '2022-2023','2023-2024' , '2024-2025')
year_option_menu.grid(row=5, column=1, padx=(0,10))

# menu cho mon hoc
subject_label = tk.Label(root, text="Môn học:")
subject_label.grid(row=6, column=0, padx=(10, 0))
subject_var = tk.StringVar(root)
subject_var.set('Môn học 1')
subject_option_menu = tk.OptionMenu(root,subject_var, 'Môn học 1','Môn học 2' , 'Môn học 3')
subject_option_menu.grid(row=6, column=1, padx=(0,10))

# nút Đăng kí
register_button = tk.Button(root, text = "Đăng ký", command=register)
register_button.grid(row =7 , column= 0, pady= (10,0))

# nút thoát

exit_button = tk.Button( root , text= "Thoát", command=root.quit)
exit_button.grid(row=7, column=1, pady= (10,0))

# khởi động
root.mainloop()
