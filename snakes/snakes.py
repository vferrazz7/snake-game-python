import pygame
import random

pygame.init()

pygame.display.set_caption('Snake Game')

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))

relogio = pygame.time.Clock()

# Definindo cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# Parâmetros da cobra
tamanho_quadrado = 20
velocidade_jogo = 15

def gerar_comida():
    comida_x = random.randrange(0, largura - tamanho_quadrado, tamanho_quadrado)
    comida_y = random.randrange(0, altura - tamanho_quadrado, tamanho_quadrado)
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branco, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f'Pontos: {pontuacao}', True, vermelho)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
    velocidade_x, velocidade_y = 0, 0

    if tecla == pygame.K_DOWN:
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado

    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False
    x = largura / 2
    y = altura / 2
    velocidade_x = 0
    velocidade_y = 0
    tamanho_cobra = 1
    pixels = []
    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(preto)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # Atualizar posição da cobra
        x += velocidade_x
        y += velocidade_y

        # Verificar colisão com a parede
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        # Desenhar comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # Desenhar a cabeça da cobra
        pixels.append([x, y])

        # Verificar colisão com a comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

        # Verificar colisão com a própria cobra
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        # Desenhar a cobra
        desenhar_cobra(tamanho_quadrado, pixels)

        # Desenhar pontuação
        desenhar_pontuacao(tamanho_cobra - 1)

        pygame.display.update()

        relogio.tick(velocidade_jogo)

    pygame.quit()

# Iniciar o jogo
rodar_jogo()
