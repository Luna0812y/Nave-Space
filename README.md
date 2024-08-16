# Jogo da Nave Espacial

Este projeto é um jogo espacial de fase única desenvolvido em Python com a biblioteca Pygame. O jogo apresenta uma interface em 2D, onde a Pygame é responsável pelo controle dos personagens e pela movimentação dentro do ambiente do jogo.

## Estrutura do Projeto

- **Backend (Python com Pygame)**
  - **`src/main.py`**: Inicialização e controle do jogo.
  - **`src/constantes.py`**: Definição das constantes.
 
- **Assets**
  - **`assets/sprites/`**: Todas as imagens utilizadas.
  - **`assets/fonts/`**: Fonte das palavras.
  - **`styles.css`**: Estilos para a página.

## Instalação

1. **IInstalação da Pygame:**
    obs: Certifique-se de ter o Python instalado.

    ```bash
    pip install pygame
    ```

2. **Executar o jogo:**

    ```bash
    py src/main.py
    ```
    ou
    ```bash
    python src/main.py
    ```

### 3. Estrutura da Explicação do Código

#### 1. **Introdução**

Visão geral de como funciona o jogo.

O jogo permite ao jogador controlar uma nave espacial, disparar mísseis e tentar atingir inimigos enquanto evita colisões. O jogo possui um loop principal que gerencia a lógica do jogo, a interação do usuário e a atualização da tela.

#### 2. **Importações e Configurações Iniciais**

```python
import pygame
import random
import src.constantes as constantes
```

- `pygame`: Biblioteca usada para criar jogos 2D. Fornece funcionalidades para manipulação de gráficos, som e entrada do usuário.
- `random`: Biblioteca padrão usada para gerar números aleatórios, o que é útil para a posição dos inimigos.
- `src.constantes`: Módulo local que contém constantes usadas no jogo, como tamanhos de tela e caminhos para arquivos de recursos.

```python
pygame.init()
```
- Inicializa todos os módulos do Pygame necessários para a execução do jogo.

#### 3. **Carregamento de Recursos**

```python
bg = pygame.image.load(constantes.cenario).convert_alpha()
bg = pygame.transform.scale(bg, (constantes.largura, constantes.altura))
```
> Carregando o sprite ``cen-luta.png``
- Carrega a imagem de fundo e ajusta seu tamanho para cobrir toda a tela.

#### 4. **Configuração de Variáveis**

```python
pos_alien_x = 1200
pos_alien_y = 360

pos_player_x = 200
pos_player_y = 300

vel_missil_x = 0
pos_missil_x = 205
pos_missil_y = 315
```

- Define as posições iniciais e a velocidade do inimigo, do jogador e do míssil.

#### 5. **Loop Principal do Jogo**

```python
while inciando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inciando = False
```

- Verifica eventos, como o fechamento da janela, e encerra o jogo se o usuário clicar no botão de fechar.

```python
    tela.blit(bg, (0,0))
```

- Cria um efeito de movimento infinito para o fundo.

```python
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -= 2
        if not triggered:
            pos_missil_y -= 2
```

- Encerra o jogo quando a pontuação atinge zero.

```python
    if pos_alien_x == 50:
        pos_alien_x = random.randint(1350, 1500)
        pos_alien_y = random.randint(1, 640)
```
> Utilizando o ``import random`` 
- Reposiciona o inimigo quando ele sai da tela.

```python
    tela.blit(player, player_rect)
    if triggered: 
        tela.blit(missil, missil_rect)
    tela.blit(alien, alien_rect)
```

- Desenha a nave, o míssil (se disparado) e o inimigo na tela.


```python
    pygame.display.update()
```

- Atualiza a tela para refletir as mudanças feitas.

#### 6. **Encerramento**

Explique como o jogo é encerrado e os recursos são limpos.

```python
pygame.quit()
```

- Encerra o Pygame e limpa os recursos utilizados.

## Contato

Para qualquer dúvida ou sugestão, entre em contato pelo e-mail: [layspessoal338@gmail.com].