# Automação de Processos para Estamparia

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
