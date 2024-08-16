import pygame
import random
import constantes

pygame.init()

tela = pygame.display.set_mode((constantes.largura, constantes.altura))
pygame.display.set_caption('Nave Space')

#variaveis de entrada da animações
bg = pygame.image.load(constantes.cenario).convert_alpha()
bg = pygame.transform.scale(bg, (constantes.largura, constantes.altura))

alien = pygame.image.load(constantes.monstro).convert_alpha()
alien = pygame.transform.scale(alien, (70, 70))

player = pygame.image.load(constantes.nave).convert_alpha()
player = pygame.transform.scale(player, (100, 100)) 

missil = pygame.image.load(constantes.atack).convert_alpha()
missil = pygame.transform.scale(missil, (25, 25))

#posição e velocidade de cada personagem
pos_alien_x = 1200
pos_alien_y = 360

pos_player_x = 200
pos_player_y = 300

vel_missil_x = 0
pos_missil_x = 205
pos_missil_y = 315

#vida dos personagens
pontos = 2

#game over
font = pygame.font.SysFont(constantes.fonte, 50)

#variável para controlar se o míssil foi disparado
triggered = False

#incialização do jogo
inciando = True

while inciando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inciando = False
    
    tela.blit(bg, (0,0))

    rel_x = constantes.largura % bg.get_rect().width
    tela.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < 1280:
        tela.blit(bg, (rel_x, 0))

    # Movimentação do jogador 
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -= 2
        if not triggered:
            pos_missil_y -= 2

    if tecla[pygame.K_DOWN] and pos_player_y < 665:
        pos_player_y += 2
        if not triggered:
            pos_missil_y += 2

    if tecla[pygame.K_LEFT] and pos_player_x > 1:
        pos_player_x -= 2
        if not triggered:
            pos_missil_x -= 2

    if tecla[pygame.K_RIGHT] and pos_player_x < 1200:
        pos_player_x += 2
        if not triggered:
            pos_missil_x += 2

    # Disparo do míssil
    if tecla[pygame.K_SPACE] and not triggered:
        triggered = True
        vel_missil_x = 5
        pos_missil_x = pos_player_x + 40
        pos_missil_y = pos_player_y + 30  
    
    if pontos == 0:
        inciando = False
    
    if pos_alien_x == 50:
        pos_alien_x = random.randint(1350, 1500)
        pos_alien_y = random.randint(1, 640)
    
    if pos_missil_x >= 1300:
        triggered = False
    
    player_rect = player.get_rect(topleft=(pos_player_x, pos_player_y))
    missil_rect = missil.get_rect(topleft=(pos_missil_x, pos_missil_y))
    alien_rect = alien.get_rect(topleft=(pos_alien_x, pos_alien_y))

    # Checa colisões
    if player_rect.colliderect(alien_rect):
        pontos -= 1
        pos_alien_x = random.randint(1350, 1500)
        pos_alien_y = random.randint(1, 640)

    if missil_rect.colliderect(alien_rect):
        pontos += 1
        pos_alien_x = random.randint(1350, 1500)
        pos_alien_y = random.randint(1, 640)

    #movimento
    constantes.largura -= 5
    pos_alien_x -= 1
    pos_missil_x += vel_missil_x

    tela.blit(player, player_rect)
    if triggered: 
        tela.blit(missil, missil_rect)
    tela.blit(alien, alien_rect)

    score = font.render(f'Pontuação: {pontos}', True, (255, 255, 255))
    tela.blit(score, (50, 50))

    pygame.display.update()

# Encerra o Pygame
pygame.quit()