import tkinter as tk
from tkinter import messagebox

messagebox.showinfo("Atenção !", "Atenção você acaba de ser rackeada, essa janela só irá fechar se você escolher a opção certa!")

def ask_lorena():
    
        
    answer = messagebox.askyesno("Pergunta", "Lorena, quer ficar comigo?")
    if answer:
        messagebox.showinfo("Resposta", "Te espero na sala de oração na hora do intervalo pode ser ?")
        root.quit()
    else:
        ask_lorena()
    

root = tk.Tk()
root.withdraw()
ask_lorena()
root.mainloop()