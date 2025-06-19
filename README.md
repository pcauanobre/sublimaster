# Automation of Processes for Printing Shop (EN Version)

This project was developed with the goal of improving the company's production by automating repetitive processes and speeding up the workflow. It was built in Python, using libraries like pywin32 for communication with CorelDRAW and pyautogui for UI automation and shortcut execution. In addition, VBA scripts were used for internal automation within CorelDRAW. The project contains a main Controller that manages four specific scripts.

## Controller
- **Set Quantity**
- **Fit Layout**
- **Transfer**
- **Uniforms**

The **Controller** has an intuitive graphical interface with dedicated buttons that execute each script, allowing the user to start processes with a simple click.

![4](https://github.com/user-attachments/assets/0a00e3b1-73e1-4853-b95a-f4049944c219)

It also includes additional features such as a **slider** (to control the execution speed in some scripts), a **stop script button**, and a **minimize to tray button**.

---

## 1. Set Quantity

![ColocarQuantidade](https://github.com/user-attachments/assets/95dd790a-8f16-4fa8-8f2b-719dc0566c9d)

> **Function**: Facilitate file printing through a specific program.  
> **Process**: This script performs a preliminary mapping of the necessary clicks so that PyAutoGUI can then automatically input the correct quantities.  
> **Note**: It is necessary to define quantities for the different sizes, according to each order. Since the script depends on **fixed coordinates**, it may present errors on computers with different screen resolutions. In the future, the idea is to adjust it to make it more universal.

---

## 2. Fit Layout

![Encaixar](https://github.com/user-attachments/assets/cf4730c3-c662-4d29-be86-4f2f893a10bd)

> **Function**: Take the mockup (sent to the client, in vector format and with predefined object names in CorelDRAW) and **fit** it into the company's standard template.  
> **Process**: The **Fit Layout** script identifies elements by their predefined names in the templates and automatically aligns them correctly into the company’s template.  
> **Note**: A final check (fine adjustment) is still needed after automatic fitting.

---

## 3. Transfer

![Repassar](https://github.com/user-attachments/assets/f6a4c64a-a7df-42ee-9878-3c7e86eb0111)

> **Function**: Transfer the already aligned artwork to **other templates**, using one of them as the main reference.  
> **Process**: The **Transfer** script uses a base template as reference to apply the artwork to other templates, ensuring consistency across different models.

---

## 4. Uniforms

![Uniforme](https://github.com/user-attachments/assets/69927870-de12-42ac-85b2-4c82bd80eb04)

> **Function**: Insert **names** and **quantities** on sports uniforms, using a reference template.  
> **Differential**: It can **automatically duplicate** the object for multiple uniforms, based on the provided inputs (number of shirts, names, and quantities).  
> **Process**: In the **Uniforms** script, there is an input menu to insert specific data for each uniform, such as name, number, and other settings to start, pause, and finish the process.

![1](https://github.com/user-attachments/assets/ef7ba821-7b5e-4e02-8951-93299c62b500)  
![2](https://github.com/user-attachments/assets/94a55543-f631-44f8-9a38-1251fabb246b)

---

## Additional Features

- **Stop Script Button**: Stops any script in progress. Useful if something goes wrong or you need to cancel the automation.
- **Minimize to Tray**: Hides the main window, leaving only an icon in the system tray, allowing continued use of the computer without interference from the app window.

---

## Final Notes

- This project **was specifically created** to **automate processes** for a printing company.  
- Some scripts use **fixed coordinates** (PyAutoGUI), which may not work properly on other computers or with different screen resolutions.  

**Feel free to explore the `Controlador.py` and `Encaixar.py` code**, which are part of this automation demo. For suggestions or contributions, open an **Issue** or make a **Pull Request**.

Thanks for checking out the project!

---

# Automação de Processos para Estamparia (PT Version)

Este projeto foi desenvolvido com o objetivo de melhorar a produção da empresa, automatizando processos repetitivos e acelerando o fluxo de trabalho. Ele foi desenvolvido em Python, utilizando bibliotecas como pywin32 para comunicação com o CorelDRAW e pyautogui para automação de interface e execução de atalhos. Além disso, foram utilizados scripts em VBA para automação interna dentro do CorelDRAW. O projeto contém um Controlador principal que gerencia quatro scripts específicos.

## Controlador
- **Colocar Quantidade**
- **Encaixar**
- **Repassar**
- **Uniforme**

O **Controlador** possui uma interface gráfica intuitiva com botões dedicados que executam cada um dos scripts, permitindo ao usuário iniciar os processos com um simples clique.

![4](https://github.com/user-attachments/assets/0a00e3b1-73e1-4853-b95a-f4049944c219)

Além disso, há recursos adicionais como **slider** (para controlar a velocidade de execução em alguns scripts), **botão de interromper scripts** e **botão para minimizar para a bandeja**.

---

## 1. Colocar Quantidade

![ColocarQuantidade](https://github.com/user-attachments/assets/95dd790a-8f16-4fa8-8f2b-719dc0566c9d)

> **Função**: Facilitar a impressão dos arquivos através de um programa específico.  
> **Processo**: Este script realiza um mapeamento prévio dos cliques necessários para que, em seguida, o PyAutoGUI possa inserir as quantidades corretas automaticamente.  
> **Observação**: É necessário definir as quantidades para os diferentes tamanhos, de acordo com cada pedido. Como o script depende de **coordenadas fixas**, ele pode apresentar erros em computadores com resoluções diferentes. No futuro, a ideia é ajustá-lo para torná-lo mais universal.

---

## 2. Encaixar

![Encaixar](https://github.com/user-attachments/assets/cf4730c3-c662-4d29-be86-4f2f893a10bd)

> **Função**: Pegar o mockup (enviado ao cliente, em vetor e com nomes de objetos pré-definidos no CorelDRAW) e **repassar** para o molde padrão da empresa.  
> **Processo**: O script **Encaixar** identifica os elementos pelos nomes pré-definidos nos moldes e realiza um processo automático para encaixá-los corretamente no molde da empresa.  
> **Observação**: Ainda é necessária uma conferência final (ajuste fino) após o encaixe automático.

---

## 3. Repassar

![Repassar](https://github.com/user-attachments/assets/f6a4c64a-a7df-42ee-9878-3c7e86eb0111)

> **Função**: Repassar a arte já encaixada para **demais moldes**, tendo um deles como referência principal.  
> **Processo**: O script **Repassar** utiliza um molde base como referência para aplicar a arte aos demais moldes, garantindo uniformidade entre os diferentes modelos.

---

## 4. Uniforme

![Uniforme](https://github.com/user-attachments/assets/69927870-de12-42ac-85b2-4c82bd80eb04)

> **Função**: Inserir **nomes** e **quantidades** em uniformes esportivos, utilizando um molde de referência.  
> **Diferencial**: Ele pode **duplicar automaticamente** o objeto para vários uniformes, de acordo com os inputs fornecidos (quantidade de camisas, nomes e quantidades).  
> **Processo**: No script **Uniforme**, há um menu de input para inserir os dados específicos de cada uniforme, como nome, número e outras configurações para iniciar, pausar e finalizar o processo.

![1](https://github.com/user-attachments/assets/ef7ba821-7b5e-4e02-8951-93299c62b500)  
![2](https://github.com/user-attachments/assets/94a55543-f631-44f8-9a38-1251fabb246b)

---

## Recursos Adicionais

- **Botão de Interromper Scripts**: Encerra qualquer script em execução. Útil se algo não sair como esperado ou se você precisar cancelar a automação.
- **Minimizar para Bandeja**: Esconde a janela principal, deixando apenas um ícone na bandeja do sistema, permitindo o uso contínuo do computador sem a interferência da janela.

---

## Observações Finais

- Este projeto **foi criado especificamente** para **automatizar processos** de uma empresa de estamparia.  
- Alguns scripts utilizam **coordenadas fixas** (PyAutoGUI), o que pode não funcionar corretamente em outros computadores ou com diferentes resoluções.  

**Sinta-se à vontade para explorar os códigos do `Controlador.py` e do `Encaixar.py`**, que fazem parte desta demo de automação. Para sugestões ou contribuições, abra uma **Issue** ou faça um **Pull Request**.

Obrigado por conferir o projeto!
