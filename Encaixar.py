import sys
import win32com.client as win32
import pygetwindow as gw
import pyautogui
import time
import ctypes
import os
import importlib.util

# Verifica se o valor de tempo_espera foi passado como argumento
try:
    tempo_espera = float(sys.argv[1])  # Captura o valor do argumento (primeiro argumento)
except (IndexError, ValueError):
    tempo_espera = 0.2  # Valor padrão, caso o argumento não tenha sido passado
    print("Aviso: Não foi passado um valor de tempo_espera. Usando valor padrão de 0.2 segundos.")


# Função para garantir que a caixa de mensagem seja exibida no topo
def show_message_box_topmost(message, title):
    MB_OK = 0x00000000
    hwnd = ctypes.windll.user32.GetForegroundWindow()  # Obtém a janela atual no primeiro plano
    ctypes.windll.user32.MessageBoxW(hwnd, message, title, MB_OK)

    # Após exibir a MessageBox, trazê-la para o topo com SetWindowPos
    HWND_TOPMOST = -1
    SWP_NOSIZE = 0x0001
    SWP_NOMOVE = 0x0002
    SWP_SHOWWINDOW = 0x0040
    message_hwnd = ctypes.windll.user32.FindWindowW(None, title)  # Encontra a janela pelo título
    if message_hwnd:
        ctypes.windll.user32.SetWindowPos(message_hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE | SWP_SHOWWINDOW)

# Conectar ao CorelDRAW
corel = win32.Dispatch("CorelDRAW.Application")
corel.Visible = True

# Maximizar a janela do CorelDRAW se estiver aberta
windows = gw.getWindowsWithTitle("CorelDRAW")
if windows:
    corel_window = windows[0]
    if corel_window.isMinimized:
        corel_window.restore()
    corel_window.maximize()
    corel_window.activate()
else:
    print("Janela do CorelDRAW não encontrada!")
    exit()

# Garantir que o documento ativo está aberto
doc = corel.ActiveDocument
if doc is None:
    print("Nenhum documento ativo no CorelDRAW!")
    exit()

# Usar o tempo de espera carregado
sleep_time = tempo_espera

# Função para procurar múltiplos objetos por nome, ignorando objetos bloqueados
def find_all_shapes_by_keyword(layer, keyword):
    shapes_found = []
    for shape in layer.Shapes:
        if not shape.Locked and shape.Name.endswith(keyword):  # Ignora objetos bloqueados
            shapes_found.append(shape)
        for subshape in shape.Shapes:
            if not subshape.Locked and subshape.Name.endswith(keyword):  # Ignora sub-objetos bloqueados
                shapes_found.append(subshape)
    return shapes_found

# Função para procurar um único objeto por palavra-chave, ignorando objetos bloqueados
def find_shape_by_keyword(layer, keyword):
    for shape in layer.Shapes:
        if not shape.Locked and shape.Name.endswith(keyword):  # Ignora objetos bloqueados
            return shape
        for subshape in shape.Shapes:
            if not subshape.Locked and subshape.Name.endswith(keyword):  # Ignora sub-objetos bloqueados
                return subshape
    return None

# Função para processar MOCKUP e o objeto alvo, garantindo que ambos não estão bloqueados
def processar_mockup(mockup_obj, target_obj):
    if mockup_obj is None or target_obj is None:
        print(f"Objeto '{mockup_obj.Name if mockup_obj else 'Mockup'}' ou '{target_obj.Name if target_obj else 'Target'}' não encontrado.")
        return
    
    if mockup_obj.Locked or target_obj.Locked:
        print(f"Um dos objetos está bloqueado: '{mockup_obj.Name}' ou '{target_obj.Name}'. Processo abortado.")
        return

    print(f"Objetos '{mockup_obj.Name}' e '{target_obj.Name}' encontrados!")

    # Selecionar MOCKUP e o alvo
    doc.ClearSelection()
    mockup_obj.Selected = True
    target_obj.Selected = True

    # PASSAR PREENCHIMENTO
    pyautogui.hotkey('num3')
    time.sleep(tempo_espera)  # Usa o tempo de espera configurado

    # Desselecionar
    doc.ClearSelection()
    print("Macro executada, preenchimento copiado.")

    # Fazer cópia do objeto MOCKUP
    mockup_copy = mockup_obj.Duplicate()
    print(f"Cópia do objeto '{mockup_obj.Name}' criada.")
    time.sleep(tempo_espera)  # Usa o tempo de espera configurado

    # Ajustar tamanho proporcionalmente à altura do alvo
    altura_target = target_obj.SizeHeight
    proporcao = altura_target / mockup_copy.SizeHeight
    mockup_copy.SetSize(mockup_copy.SizeWidth * proporcao, altura_target)
    time.sleep(tempo_espera)  # Usa o tempo de espera configurado
    print(f"Cópia de '{mockup_obj.Name}' ajustada para altura: {altura_target}")

    # Diminuir a largura em 1.5 cm proporcionalmente
    nova_largura = mockup_copy.SizeWidth - 1.5
    nova_altura = mockup_copy.SizeHeight * (nova_largura / mockup_copy.SizeWidth)
    mockup_copy.SetSize(nova_largura, nova_altura)
    time.sleep(tempo_espera)  # Usa o tempo de espera configurado
    print(f"Largura reduzida em 1.5 cm, nova largura: {nova_largura}, nova altura: {nova_altura}")

    # Centralizar a cópia com o alvo
    doc.ClearSelection()
    mockup_copy.Selected = True
    target_obj.Selected = True
    
    # CENTRALIZAR HORIZONTALMENTE
    pyautogui.press('c')
    time.sleep(tempo_espera)  # Usa o tempo de espera configurado
    # CENTRALIZAR VERTICALMENTE
    pyautogui.press('e')
    doc.ClearSelection()

    mockup_copy.Selected = True
    target_obj.Selected = True
    # ALINHGAR BASES
    pyautogui.press('b')
    doc.ClearSelection()

    mockup_copy.Selected = True
    # EXTRAIR CONTEÚDO DO OBJETO
    pyautogui.hotkey('num7')
    time.sleep(tempo_espera)  # Usa o tempo de espera configurado
    # AGRUPAR
    pyautogui.hotkey('ctrl', 'g')
    time.sleep(tempo_espera)  # Usa o tempo de espera configurado
    mockup_copy.Delete()

    target_obj.Selected = True
    # POWERCLIPAR
    pyautogui.hotkey('num2')
    time.sleep(tempo_espera)  # Usa o tempo de espera configurado
    doc.ClearSelection()

# Função para renomear o objeto após o procedimento (adicionar "2")
def renomear_para_2(shape, sufixo="2"):
    if shape:
        novo_nome = shape.Name + sufixo
        shape.Name = novo_nome
        print(f"Objeto renomeado para '{novo_nome}'.")

# Processar FRENTE MOCKUP e FRENTE
processar_mockup(find_shape_by_keyword(doc.ActiveLayer, "FRENTE MOCKUP"), find_shape_by_keyword(doc.ActiveLayer, "FRENTE"))

# Processar COSTAS MOCKUP e COSTAS
processar_mockup(find_shape_by_keyword(doc.ActiveLayer, "COSTAS MOCKUP"), find_shape_by_keyword(doc.ActiveLayer, "COSTAS"))

# Processar MANGA MOCKUP e MANGA 2 MOCKUP com MANGA
m_mangas = find_all_shapes_by_keyword(doc.ActiveLayer, "MANGA")

if len(m_mangas) == 1:
    processar_mockup(find_shape_by_keyword(doc.ActiveLayer, "MANGA MOCKUP"), m_mangas[0])
elif len(m_mangas) == 2:
    processar_mockup(find_shape_by_keyword(doc.ActiveLayer, "MANGA MOCKUP"), m_mangas[1])
    processar_mockup(find_shape_by_keyword(doc.ActiveLayer, "MANGA 2 MOCKUP"), m_mangas[0])
    renomear_para_2(m_mangas[0])

# Processar MANGA LONGA MOCKUP e MANGA LONGA 2 MOCKUP com MANGA LONGA
m_manga_longas = find_all_shapes_by_keyword(doc.ActiveLayer, "MANGA LONGA")

if len(m_manga_longas) == 1:
    processar_mockup(find_shape_by_keyword(doc.ActiveLayer, "MANGA LONGA MOCKUP"), m_manga_longas[0])
elif len(m_manga_longas) == 2:
    processar_mockup(find_shape_by_keyword(doc.ActiveLayer, "MANGA LONGA MOCKUP"), m_manga_longas[1])
    processar_mockup(find_shape_by_keyword(doc.ActiveLayer, "MANGA LONGA 2 MOCKUP"), m_manga_longas[0])
    renomear_para_2(m_manga_longas[0])

# Verificação final para preenchimentos ausentes
def verificar_objetos_sem_preenchimento():
    nomes_a_verificar = ["FRENTE", "COSTAS", "MANGA", "MANGA2", "MANGA LONGA", "MANGA LONGA2"]
    objetos_sem_preenchimento = []

    for nome in nomes_a_verificar:
        objeto = find_shape_by_keyword(doc.ActiveLayer, nome)
        if objeto and objeto.Fill.Type == 0:  # Verifica se o objeto está sem preenchimento (cdrNoFill é 0)
            objetos_sem_preenchimento.append(objeto.Name)
    
    if objetos_sem_preenchimento:
        mensagem = f"{len(objetos_sem_preenchimento)} objeto(s) sem preenchimento encontrado(s):\n\n"
        mensagem += "\n".join(objetos_sem_preenchimento)
        show_message_box_topmost(mensagem, "Verificação de Preenchimento")

# Chamar a verificação de objetos sem preenchimento
verificar_objetos_sem_preenchimento()
