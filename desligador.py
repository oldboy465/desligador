import tkinter as tk
from tkinter import messagebox
import os
import threading
import random
import pyautogui

# Função para criar o efeito de glitter
def create_glitter(event):
    x, y = event.x, event.y
    size = random.randint(5, 15)
    color = random.choice(["#FFD700", "#FF69B4", "#00FFFF", "#FF4500", "#8A2BE2"])
    canvas.create_oval(x, y, x + size, y + size, fill=color, outline=color)
    root.after(100, lambda: canvas.delete("all"))  # Limpa o glitter após 100ms

# Função para programar o desligamento
def schedule_shutdown():
    try:
        hours = int(entry_hours.get())
        minutes = int(entry_minutes.get())
        total_seconds = (hours * 3600) + (minutes * 60)
        if total_seconds <= 0:
            raise ValueError("Tempo inválido!")
        
        # Executa o comando de desligamento
        shutdown_thread = threading.Thread(target=run_shutdown, args=(total_seconds,))
        shutdown_thread.start()
        messagebox.showinfo("Sucesso", f"O computador será desligado em {hours} horas e {minutes} minutos.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para horas e minutos.")

# Função para executar o comando de desligamento
def run_shutdown(seconds):
    os.system(f"shutdown -s -t {seconds}")

# Função para cancelar o desligamento
def cancel_shutdown():
    os.system("shutdown -a")
    messagebox.showinfo("Cancelado", "O desligamento programado foi cancelado.")

# Configuração da janela principal
root = tk.Tk()
root.title("Programador de Desligamento Fofo 🌟")
root.geometry("400x300")
root.configure(bg="#FFD1DC")  # Cor de fundo suave

# Canvas para o glitter
canvas = tk.Canvas(root, bg="#FFD1DC", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Rótulos e entradas
label_hours = tk.Label(root, text="Horas:", font=("Arial", 12), bg="#FFD1DC")
label_hours.place(x=50, y=50)
entry_hours = tk.Entry(root, font=("Arial", 12))
entry_hours.place(x=120, y=50)

label_minutes = tk.Label(root, text="Minutos:", font=("Arial", 12), bg="#FFD1DC")
label_minutes.place(x=50, y=90)
entry_minutes = tk.Entry(root, font=("Arial", 12))
entry_minutes.place(x=120, y=90)

# Botões
btn_schedule = tk.Button(root, text="Programar Desligamento", font=("Arial", 12), command=schedule_shutdown, bg="#FF69B4", fg="white")
btn_schedule.place(x=100, y=140)

btn_cancel = tk.Button(root, text="Cancelar Desligamento", font=("Arial", 12), command=cancel_shutdown, bg="#FF4500", fg="white")
btn_cancel.place(x=100, y=190)

# Efeito de glitter seguindo o mouse
canvas.bind("<Motion>", create_glitter)

# Inicia o loop principal
root.mainloop()