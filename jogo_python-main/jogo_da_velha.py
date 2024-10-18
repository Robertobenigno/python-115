
import pygame #importa a biblioteca pygame para o script


# pygame configuração
pygame.init() #inicialização do pygame
pygame.font.init() #inicialização do pacote de fontes no pygame

screen = pygame.display.set_mode((600, 600)) #definição do tamanho da tela
pygame.display.set_caption('Jogo da Velha') #nome da janela do jogo
clock = pygame.time.Clock() #biblioteca de tempo

fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms', 100, True, True) #importar fonte
running = True #variável de controle do status do jogo

personagem_x = fonte_quadrinhos.render('X', True, 'red')
personagem_y = fonte_quadrinhos.render('O', True, 'red')
cor_fundo = 1

while running:
    # controle de enventos no jgo
    for event in pygame.event.get():
        # pygame.QUIT significa que quando usuário clicar em X a tela fechará
        if event.type == pygame.QUIT:
            running = False
        # pygame.MOUSEBUTTONDOWN significa evento de click do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Clicou')
            cor_fundo = cor_fundo + 1
            if(cor_fundo > 3):
                cor_fundo = 1
        
    #Desenha tabuleiro
    pygame.draw.line(screen, 'white',(200, 0), (200, 600), 10)
    pygame.draw.line(screen, 'white',(400, 0), (400, 600), 10)
    pygame.draw.line(screen, 'white',(0, 200), (600, 200), 10)
    pygame.draw.line(screen, 'white',(0, 400), (600, 400), 10)
                               
    screen.blit(personagem_x,(65,30)) #primeiro
    screen.blit(personagem_y,(265,30)) #segundo
    screen.blit(personagem_y,(460,30)) #terceiro

    # flip() o display para atualizar a página
    pygame.display.flip()

    clock.tick(60)  # limita o fps para 60

pygame.quit()