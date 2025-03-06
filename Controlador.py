import tkinter as tk
from threading import Thread
import subprocess
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import keyboard
import sys
import os
import pyautogui
from PIL import Image

# Função para obter o caminho do ícone
def get_icon_path():
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, "Programa Interart.ico")
    return "C:\\Users\\Breno Nobre\\Desktop\\AutomaçãoInterart\\Programa\\Programa Interart.ico"

icon_path = get_icon_path()

# Configuração do ícone no Tkinter e Pystray
def configurar_icone_tkinter(root):
    root.iconbitmap(icon_path)

def configurar_icone_pystray():
    image = Image.open(icon_path)
    return image

def criar_bandeja():
    tray_icon = pystray.Icon(
        "Controlador",
        configurar_icone_pystray(),
        menu=pystray.Menu(
            item("Abrir", lambda: restore_window()),
            item("Sair", lambda: quit_app())
        )
    )
    tray_icon.run()

# Variáveis globais para os processos dos scripts
processo_script1 = None  # Encaixar.py
processo_script2 = None  # Repassar.py
processo_script3 = None  # Uniforme.py
processo_script4 = None  # ColocarQuantidade.py

# Variável global para o tempo de espera
tempo_espera = 0.1

python_path = "C:\\Users\\Breno Nobre\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"

def carregar_tempo_espera():
    global tempo_espera
    return tempo_espera

def alterar_tempo_espera(novo_tempo):
    global tempo_espera
    tempo_espera = novo_tempo
    print(f"Tempo de espera alterado para {tempo_espera} segundos.")

def iniciar_script1():
    global processo_script1
    if processo_script1 is None or processo_script1.poll() is not None:
        script1_path = os.path.join(os.path.dirname(__file__), 'Encaixar.py')
        processo_script1 = subprocess.Popen([python_path, script1_path, str(carregar_tempo_espera())])
        print("Encaixar.py iniciado.")
    else:
        print("Encaixar.py já está rodando.")

def iniciar_script2():
    global processo_script2
    if processo_script2 is None or processo_script2.poll() is not None:
        script2_path = os.path.join(os.path.dirname(__file__), 'Repassar.py')
        processo_script2 = subprocess.Popen([python_path, script2_path, str(carregar_tempo_espera())])
        print("Repassar.py iniciado.")
    else:
        print("Repassar.py já está rodando.")

def iniciar_script3():
    global processo_script3
    if processo_script3 is None or processo_script3.poll() is not None:
        script3_path = os.path.join(os.path.dirname(__file__), 'EncaixarUniforme.py')
        processo_script3 = subprocess.Popen([python_path, script3_path])
        print("Uniforme.py iniciado.")
    else:
        print("Uniforme.py já está rodando.")

def iniciar_script4():
    global processo_script4
    if processo_script4 is None or processo_script4.poll() is not None:
        script4_path = os.path.join(os.path.dirname(__file__), 'ColocarQuantidade.py')
        processo_script4 = subprocess.Popen([python_path, script4_path])
        print("ColocarQuantidade.py iniciado.")
    else:
        print("ColocarQuantidade.py já está rodando.")

def parar_scripts():
    global processo_script1, processo_script2, processo_script3, processo_script4
    if processo_script1 and processo_script1.poll() is None:
        processo_script1.terminate()
        processo_script1 = None
        print("Encaixar.py interrompido.")
    if processo_script2 and processo_script2.poll() is None:
        processo_script2.terminate()
        processo_script2 = None
        print("Repassar.py interrompido.")
    if processo_script3 and processo_script3.poll() is None:
        processo_script3.terminate()
        processo_script3 = None
        print("Uniforme.py interrompido.")
    if processo_script4 and processo_script4.poll() is None:
        processo_script4.terminate()
        processo_script4 = None
        print("ColocarQuantidade.py interrompido.")
    exibir_messagebox_timer("Interrupção", "Os scripts foram interrompidos com sucesso!", 1000)

def exibir_messagebox_timer(titulo, mensagem, timeout):
    msg_window = tk.Tk()
    msg_window.title(titulo)
    label = tk.Label(msg_window, text=mensagem, padx=10, pady=10)
    label.pack()
    msg_window.after(timeout, msg_window.destroy)
    msg_window.attributes('-topmost', True)
    msg_window.update_idletasks()
    width = msg_window.winfo_width()
    height = msg_window.winfo_height()
    screen_width = msg_window.winfo_screenwidth()
    screen_height = msg_window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    msg_window.geometry(f"+{x}+{y}")
    msg_window.mainloop()

def verificar_processos():
    global processo_script1, processo_script2, processo_script3, processo_script4
    if processo_script1 and processo_script1.poll() is not None:
        print("Encaixar.py foi finalizado.")
        processo_script1 = None
        pyautogui.hotkey('ctrl', 'num0')
    if processo_script2 and processo_script2.poll() is not None:
        print("Repassar.py foi finalizado.")
        processo_script2 = None
        pyautogui.hotkey('ctrl', 'num0')
    if processo_script3 and processo_script3.poll() is not None:
        print("Uniforme.py foi finalizado.")
        processo_script3 = None
        pyautogui.hotkey('ctrl', 'num0')
    if processo_script4 and processo_script4.poll() is not None:
        print("ColocarQuantidade.py foi finalizado.")
        processo_script4 = None
        pyautogui.hotkey('ctrl', 'num0')
    root.after(1000, verificar_processos)

def iniciar_thread_script1():
    Thread(target=iniciar_script1).start()

def iniciar_thread_script2():
    Thread(target=iniciar_script2).start()

def iniciar_thread_script3():
    Thread(target=iniciar_script3).start()

def iniciar_thread_script4():
    Thread(target=iniciar_script4).start()

def minimizar_para_bandeja():
    root.withdraw()

def restore_window(icon=None, item=None):
    if icon:
        icon.stop()
    root.after(0, root.deiconify)

def quit_app(icon=None, item=None):
    if icon:
        icon.stop()
    root.quit()

def criar_botao(parent, text, command, bg_color="#4b6584"):
    return tk.Button(
        parent,
        text=text,
        command=command,
        bg=bg_color,
        fg="#ffffff",
        font=("Helvetica", 11, "bold"),
        relief="raised",
        bd=3,
        activebackground="#34495e",
        activeforeground="#ffffff"
    )

# Criação e centralização da janela principal
root = tk.Tk()
root.title("Controlador")
root.configure(bg="#1e272e")
root.attributes('-topmost', True)
root.withdraw()
root.update_idletasks()
window_width = 350
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
pos_x = (screen_width // 2) - (window_width // 2)
pos_y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")
root.deiconify()

# --- SLIDER PARA TEMPO DE ESPERA ---
slider_label = tk.Label(
    root,
    text="Defina o tempo de espera (0.1 a 1.5 segundos)",
    bg="#1e272e",
    fg="#ffffff",
    font=("Helvetica", 10)
)
slider_label.pack(pady=(20, 5))

# Margem padronizada entre label e slider
margin1 = tk.Frame(root, height=20, bg="#1e272e")
margin1.pack(fill="x")

slider_tempo_espera = tk.Scale(
    root,
    from_=0.1, to=1.5,
    resolution=0.1,
    orient=tk.HORIZONTAL,
    bg="#4b6584",
    fg="#ffffff",
    highlightbackground="#4b6584",
    highlightcolor="#4b6584",
    troughcolor="#2c3e50"
)
slider_tempo_espera.set(carregar_tempo_espera())
slider_tempo_espera.pack()

# Margem padronizada entre slider e "Colocar Quantidade"
margin2 = tk.Frame(root, height=20, bg="#1e272e")
margin2.pack(fill="x")

# --- FRAME e BOTÃO (SCRIPT 4) NO TOPO: "Colocar Quantidade" ---
frame_script4 = tk.LabelFrame(
    root,
    text="Colocar Quantidade",
    padx=5,
    pady=5,
    bg="#2c3e50",
    fg="#ffffff",
    font=("Helvetica", 10, "bold")
)
frame_script4.pack(padx=5, pady=5)
btn_play4 = criar_botao(frame_script4, "Iniciar Script", iniciar_thread_script4)
btn_play4.pack(expand=True)

# --- FRAME e BOTÃO (SCRIPT 1): "Encaixar" ---
frame_script1 = tk.LabelFrame(
    root,
    text="Encaixar",
    padx=5,
    pady=5,
    bg="#2c3e50",
    fg="#ffffff",
    font=("Helvetica", 10, "bold")
)
frame_script1.pack(padx=5, pady=5)
btn_play1 = criar_botao(frame_script1, "Iniciar Script", iniciar_thread_script1)
btn_play1.pack(expand=True)

# --- FRAME e BOTÃO (SCRIPT 2): "Repassar" ---
frame_script2 = tk.LabelFrame(
    root,
    text="Repassar",
    padx=5,
    pady=5,
    bg="#2c3e50",
    fg="#ffffff",
    font=("Helvetica", 10, "bold")
)
frame_script2.pack(padx=5, pady=5)
btn_play2 = criar_botao(frame_script2, "Iniciar Script", iniciar_thread_script2)
btn_play2.pack(expand=True)

# --- FRAME e BOTÃO (SCRIPT 3): "Uniforme" ---
frame_script3 = tk.LabelFrame(
    root,
    text="Uniforme",
    padx=5,
    pady=5,
    bg="#2c3e50",
    fg="#ffffff",
    font=("Helvetica", 10, "bold")
)
frame_script3.pack(padx=5, pady=5)
btn_play3 = criar_botao(frame_script3, "Iniciar Script", iniciar_thread_script3)
btn_play3.pack(expand=True)

# --- FRAME e BOTÃO de PARAR SCRIPTS (em VERMELHO) ---
frame_stop = tk.LabelFrame(
    root,
    text="Interromper",
    padx=5,
    pady=5,
    bg="#2c3e50",
    fg="#ffffff",
    font=("Helvetica", 10, "bold"),
    bd=1,
    relief="solid"
)
frame_stop.pack(padx=5, pady=5)
btn_stop = tk.Button(
    frame_stop,
    text="Parar Scripts",
    command=parar_scripts,
    bg="#ff0000",
    fg="#ffffff",
    font=("Helvetica", 11, "bold"),
    relief="raised",
    bd=3,
    activebackground="#b30000",
    activeforeground="#ffffff"
)
btn_stop.pack(expand=True)

# Margem padronizada entre "Parar Scripts" e "Minimizar para Bandeja"
margin3 = tk.Frame(root, height=20, bg="#1e272e")
margin3.pack(fill="x")

btn_minimizar = criar_botao(root, "Minimizar para Bandeja", minimizar_para_bandeja)
btn_minimizar.pack(pady=5)

verificar_processos()
root.mainloop()
