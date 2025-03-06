# Automação de Processos para Estamparia

Este projeto foi desenvolvido com o objetivo de **melhorar a produção da empresa**, **automatizando processos repetitivos** e acelerando o fluxo de trabalho. Ele contém um **Controlador** principal que gerencia quatro scripts específicos:

## Controlador
- **Colocar Quantidade**
- **Encaixar**
- **Repassar**
- **Uniforme**

![4](https://github.com/user-attachments/assets/0a00e3b1-73e1-4853-b95a-f4049944c219)

Além disso, há recursos adicionais como **slider** (para controlar velocidade de execução em alguns scripts), **botão de interromper scripts** e **botão para minimizar para a bandeja**.

---

## 1. Colocar Quantidade

![ColocarQuantidade](https://github.com/user-attachments/assets/95dd790a-8f16-4fa8-8f2b-719dc0566c9d)

> **Função**: Facilitar a colocação de quantidades em um programa específico (que prepara arquivos para impressão).  
> **Observação**: Este script depende de **coordenadas fixas** (via PyAutoGUI), então **pode apresentar erros** em outros computadores com resoluções diferentes. No futuro, a ideia é ajustar para torná-lo mais universal.

---

## 2. Encaixar

![Encaixar](https://github.com/user-attachments/assets/cf4730c3-c662-4d29-be86-4f2f893a10bd)

> **Função**: Pegar o mockup (enviado ao cliente, em vetor e com nomes de objetos pré-definidos no CorelDRAW) e **repassar** para o molde padrão da empresa.  
> **Observação**: Ainda é necessária uma conferência final (ajuste fino) depois do encaixe automático.

---

## 3. Repassar

![Repassar](https://github.com/user-attachments/assets/f6a4c64a-a7df-42ee-9878-3c7e86eb0111)

> **Função**: Repassar a arte já encaixada para **demais moldes**, tendo um deles como referência principal. É útil quando existem variações de molde (por exemplo, tamanhos ou modelos diferentes) que devem receber a mesma arte base.

### Possível GIF de Demonstração

---

## 4. Uniforme

![Uniforme](https://github.com/user-attachments/assets/69927870-de12-42ac-85b2-4c82bd80eb04)

> **Função**: Inserir **nomes** e **quantidades** em uniformes esportivos, usando um molde de referência.  
> **Diferencial**: Ele pode **duplicar automaticamente** o objeto para vários uniformes, de acordo com os inputs fornecidos (quantidade de camisas, nomes e quantidades). É semelhante ao “Repassar”, mas voltado especificamente para uniformes e campos de personalização.

*Possui um menu de input para inserir tanto nomes quanto quantidades de cada uniforme.*

![2](https://github.com/user-attachments/assets/94a55543-f631-44f8-9a38-1251fabb246b)
![1](https://github.com/user-attachments/assets/ef7ba821-7b5e-4e02-8951-93299c62b500)

### Possível GIF de Demonstração

---

## Recursos Adicionais

- **Slider de Velocidade**: Controla o tempo de espera (`time.sleep`) em alguns scripts, como *Encaixar* e *Repassar*. Você pode ajustar entre **0.1 e 1.5 segundos** conforme a estabilidade ou velocidade desejada.
- **Botão de Interromper Scripts**: Encerra qualquer script em execução. Útil se algo não saiu como esperado ou se você precisa cancelar a automação.
- **Minimizar para Bandeja**: Esconde a janela principal, deixando apenas um ícone na bandeja do sistema. Dessa forma, você pode continuar usando o computador sem a janela atrapalhar.

---

## Observações Finais

- Este projeto **foi criado especificamente** para **automatizar processos** de uma empresa de estamparia.  
- Alguns scripts usam **coordenadas fixas** (PyAutoGUI), o que pode não funcionar bem em outros computadores ou com outras resoluções.  
- No futuro, planeja-se melhorar a **portabilidade** e tornar as coordenadas dinâmicas, reduzindo erros.

**Sinta-se à vontade para explorar o código do `Controlador.py`**, que é a base da interface e da lógica de gerenciamento dos scripts.  
Para sugestões ou contribuições, abra uma **Issue** ou faça um **Pull Request**.

Obrigado por conferir o projeto!
