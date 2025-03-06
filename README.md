# Automação de Processos para Estamparia

Este projeto foi desenvolvido com o objetivo de **melhorar a produção da empresa**, **automatizando processos repetitivos** e acelerando o fluxo de trabalho. Ele contém um **Controlador** principal que gerencia quatro scripts específicos:

- **Colocar Quantidade**
- **Encaixar**
- **Repassar**
- **Uniforme**

Além disso, há recursos adicionais como **slider** (para controlar velocidade de execução em alguns scripts), **botão de interromper scripts** e **botão para minimizar para a bandeja**.

---

## 1. Colocar Quantidade

![ColocarQuantidade](https://github.com/user-attachments/assets/95dd790a-8f16-4fa8-8f2b-719dc0566c9d)

> **Função**: Facilitar a colocação de quantidades em um programa específico (que prepara arquivos para impressão).  
> **Observação**: Este script depende de **coordenadas fixas** (via PyAutoGUI), então **pode apresentar erros** em outros computadores com resoluções diferentes. No futuro, a ideia é ajustar para torná-lo mais universal.

### Possível GIF de Demonstração
*(Aqui você pode inserir um GIF mostrando o “Colocar Quantidade” em ação.)*

*(Exemplo de placeholders para GIFs.)*

---

## 2. Encaixar

> **Função**: Pegar o mockup (enviado ao cliente, em vetor e com nomes de objetos pré-definidos no CorelDRAW) e **repassar** para o molde padrão da empresa.  
> **Observação**: Ainda é necessária uma conferência final (ajuste fino) depois do encaixe automático.

### Possível GIF de Demonstração


---

## 3. Repassar

> **Função**: Repassar a arte já encaixada para **demais moldes**, tendo um deles como referência principal. É útil quando existem variações de molde (por exemplo, tamanhos ou modelos diferentes) que devem receber a mesma arte base.

### Possível GIF de Demonstração


---

## 4. Uniforme

> **Função**: Inserir **nomes** e **números** em uniformes esportivos, usando um molde de referência.  
> **Diferencial**: Ele pode **duplicar automaticamente** o objeto para vários uniformes, de acordo com os inputs fornecidos (quantidade de camisas, nomes e números). É semelhante ao “Repassar”, mas voltado especificamente para uniformes e campos de personalização.

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
