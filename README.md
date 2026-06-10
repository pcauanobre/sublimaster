# (EN-US)

# SubliMaster: CorelDRAW automation for sublimation print shops

> **📌 View-only repository.** SubliMaster is a commercial product and its full source code is private. This repo exists to **showcase the project**: the README below shows what it does, and the `.py` files here are early-generation sample scripts kept for reference. The product itself is distributed as a Windows installer at **[sublimaster-releases.vercel.app](https://sublimaster-releases.vercel.app)**.

![SubliMaster](media/capa.png)

**SubliMaster** is a Windows desktop app installed on the print shop's machine. It talks directly to CorelDRAW (COM automation + 30 VBA macros) and turns a manual workflow of **over an hour per order into a few minutes**: it lays out the templates by size, applies names and numbers to whole uniform orders, carries the front artwork to the back and sleeves, exports every piece named and organized by client, and connects everything to the plotter's print queue.

It is sold as a product: license keys bound to the machine, per-user permissions and automatic updates. The client clicks a popup and gets the new version.

---

## 1. Fit uniforms: names and numbers for the whole order

![Fit uniforms](media/uniforme.gif)

The operator opens an interface and fills in the name and number of each shirt, along with the sizes. There is also a standard input format, so the whole list can be pasted at once. That makes it easy to generate the list with AI and drop it straight in. SubliMaster then duplicates the templates in Corel and applies each name and number to its piece, with a progress bar and ETA. What used to be half an hour of Ctrl+D becomes seconds.

---

## 2. Propagate: the front artwork covers the whole garment

![Propagate](media/repassar.gif)

With the front design ready, one click carries the artwork to the back and sleeves in the right order, using PowerClip and automatic centering through VBA macros. No copying, pasting and eyeballing: every part comes out consistent.

---

## 3. Export: every piece becomes an organized file

![Export](media/exportar.gif)

The script reads the standardized object names, groups them by model and size, isolates each piece on screen and exports the files one by one, in **PNG or JPG** (the operator picks the format). Everything comes out already named ("MODEL 1 - M FRONT") and in the client's folder. Hundreds of files ready for production without touching the mouse.

---

## 4. Print queue: the plotter never sits idle

![Print queue](media/fila-impressao.gif)

A visual manager queries the shop's order API, builds the queue and drives the plotter's Production Manager through UI automation. When the printer is free, it sends the next job on its own, with per-order history and timings.

---

## Under the hood

- **Python 3.12 + Tkinter**, talking to CorelDRAW over **COM** and firing **30 VBA macros** compiled into a `.gms`
- Single `.exe` via **PyInstaller**, with an **Inno Setup** installer that detects the machine's CorelDRAW
- **Firebase** handles licenses (machine-bound keys, NTP date validation against clock tampering), per-user script permissions and update notices
- **GitHub Actions** builds and publishes every release. The app downloads the new installer, uninstalls the old version and relaunches itself, all silently
- PID-based lock system keeps multiple automations from fighting over the same CorelDRAW instance

| | |
|---|---|
| **50-70x** | faster than the manual workflow |
| **26k+** | lines of Python + VBA |
| **39** | releases shipped via auto-update |
| **15** | template sizes, from kids' to 3XL |

🔗 **Product page / download:** [sublimaster-releases.vercel.app](https://sublimaster-releases.vercel.app)

---

# (PT-BR)

# SubliMaster: automação de CorelDRAW pra gráficas de sublimação

> **📌 Repositório só de visualização.** O SubliMaster é um produto comercial e o código-fonte completo é privado. Este repo existe pra **apresentar o projeto**: o README abaixo mostra o que ele faz, e os arquivos `.py` daqui são scripts de amostra da primeira geração, mantidos como referência. O produto em si é distribuído como instalador Windows em **[sublimaster-releases.vercel.app](https://sublimaster-releases.vercel.app)**.

![SubliMaster](media/capa.png)

O **SubliMaster** é um aplicativo desktop Windows instalado na máquina da gráfica. Ele conversa direto com o CorelDRAW (automação COM + 30 macros VBA) e transforma um fluxo manual de **mais de uma hora por pedido em poucos minutos**: monta os moldes por tamanho, aplica nomes e números em pedidos inteiros de uniforme, leva a arte da frente pra costas e mangas, exporta cada peça nomeada e organizada por cliente, e conecta tudo à fila de impressão da plotter.

É vendido como produto: licença por chave amarrada à máquina, permissões por usuário e atualização automática. O cliente clica num popup e recebe a versão nova.

---

## 1. Encaixar uniforme: nomes e números do pedido inteiro

![Encaixar uniforme](media/uniforme.gif)

O operador abre uma interface e preenche o nome e o número de cada camisa, junto com os tamanhos. Também existe um formato de entrada padrão, então dá pra colar a lista inteira de uma vez. Isso facilita gerar a lista com IA e só soltar ali dentro. O SubliMaster sai duplicando os moldes no Corel e aplicando o nome e o número em cada peça, com barra de progresso e tempo estimado. O que era meia hora de Ctrl+D vira segundos.

---

## 2. Repassar: a arte da frente vai pra peça inteira

![Repassar](media/repassar.gif)

Com o design pronto na frente, um clique propaga a arte pra costas e mangas na ordem certa, usando PowerClip e centralização automática via macros VBA. Nada de copiar, colar e alinhar no olho: todas as partes saem consistentes entre si.

---

## 3. Exportar: cada peça vira arquivo organizado

![Exportar](media/exportar.gif)

O script lê os nomes padronizados dos objetos, agrupa por modelo e tamanho, isola cada peça na tela e exporta os arquivos um a um, em **PNG ou JPG** (o operador escolhe o formato). Tudo sai já nomeado ("MODELO 1 - M FRENTE") e na pasta do cliente. Centenas de arquivos prontos pro fluxo de produção sem tocar no mouse.

---

## 4. Fila de impressão: a plotter nunca fica parada

![Fila de impressão](media/fila-impressao.gif)

Um gestor visual consulta a API de pedidos da gráfica, monta a fila e comanda o Production Manager da plotter por automação de interface. Se a impressora está livre, ele envia o próximo trabalho sozinho, com histórico de O.S. e tempos de cada etapa.

---

## Por dentro

- **Python 3.12 + Tkinter**, falando com o CorelDRAW por **COM** e disparando **30 macros VBA** compiladas num `.gms`
- Um único `.exe` via **PyInstaller**, com instalador **Inno Setup** que detecta o CorelDRAW da máquina
- **Firebase** cuida das licenças (chave amarrada à máquina, validação de data por NTP contra relógio manipulado), das permissões de script por usuário e do aviso de atualização
- **GitHub Actions** builda e publica cada release. O app baixa o instalador novo, desinstala a versão antiga e se relança sozinho, tudo silencioso
- Sistema de locks por PID impede que automações rodem por cima umas das outras no mesmo CorelDRAW

| | |
|---|---|
| **50-70x** | mais rápido que o fluxo manual |
| **26 mil+** | linhas de Python + VBA |
| **39** | releases entregues por auto-update |
| **15** | tamanhos de molde, do infantil ao XG2 |

🔗 **Página do produto / download:** [sublimaster-releases.vercel.app](https://sublimaster-releases.vercel.app)
