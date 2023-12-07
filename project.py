# программа с граф пользовательским интерфейсом

# Генератор пароль
# импорт модулей
import hashlib
from tkinter import Tk, Label, Entry, Button, StringVar 

# main function
def pwdGenerator(pwd_str: str) -> str:
    # transform to byte stroke
    byte_str = pwd_str.encode()
    # hashing
    hash_str = hashlib.sha256(byte_str)
    # transform to regular stroke
    hex_str = hash_str.hexdigest()[:6]
    # return hash stroke
    return hex_str

# test func
# while True:
#     pwd = input('insert your password: ')
#     if pwd == 'stop':
#         break
#     res = pwdGenerator(pwd)
#     print(res)

# windows object
app = Tk()

# strokes objects
raw_pwd = StringVar()
result = StringVar()

#vidget
Label(text='password: ').grid(row=0, column=0)

# vidget for pwd
Entry(textvariable=raw_pwd).grid(row=0, column=1)

# vidget buttons
def btn_func():
    result.set(pwdGenerator(raw_pwd.get()))
Button(text='ТЫК', command=btn_func).grid(row=1, column=0)

# vidget for pwd show
Entry(textvariable=result).grid(row=1, column=1)

# point of entering program
app.mainloop()