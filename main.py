import pygame
import random
import sys
from personagem.jogador import Jogador
from personagem.inimigo import Inimigo
from telas.tela_jogar import TelaJogar
from telas.tela_select import TelaSelect
from telas.tela_config import TelaConfig
from telas.tela_ranking import TelaRanking
from progresso.manager_ranking import ManagerRanking
from progresso.jogador_ranking import JogadorRanking
from telas.tela_inicial import TelaInicial
from telas.menu import Menu
from adicionais.elem_independente import ElemIndependente

def main():
    pygame.init()
    pygame.mixer.init()
    
    
    manager_ranking = ManagerRanking()
    manager_ranking.carrega_arquivo("ranking.json")
    
    largura = 800
    altura = 600
    tela = pygame.display.set_mode((largura, altura))
    fundo_jogar = pygame.image.load("assets/fundo/5.jpeg").convert_alpha()
    fundo_jogar = pygame.transform.scale(fundo_jogar, (800, 600))
    nuvem = pygame.image.load("assets/elem_independente/nuvem.png").convert_alpha()
    nuvem = pygame.transform.scale(nuvem, (200, 100))
    fonte = pygame.font.Font("assets/MKX Title.ttf", 38)
    fonte_titulo = pygame.font.Font("assets/MKX Title.ttf", 50)
    fundo = pygame.image.load("assets/fundo/1.png").convert_alpha()
    fundo = pygame.transform.scale(fundo, (800, 600))
    pygame.display.set_caption("Imortal Kombat")
    musica = "assets/MusicaMenu.mp3"
    caminho_fundo = "assets/fundo/1.png"
    inicio = TelaInicial(caminho_fundo)
    inicio.inicial(tela, fonte_titulo, fonte)
    nomejogador = inicio.nome_jogador
    soco = pygame.mixer.Sound("assets/soco.mp3")

    # Dados dos personagens
    sprites_tonaldo = [3, 3, 4, 3, 4, 1, 8, 5]
    sprites_africa = [3, 3, 4, 6, 2, 1, 10, 5]
    sprites_ferro = [3, 3, 5, 6, 2, 1, 9, 4]
    sprites_nessi = [3, 3, 4, 3, 3, 1, 8, 8]

    lista_n_sprites = [sprites_tonaldo, sprites_africa, sprites_nessi, sprites_ferro]
    lista_personagens = ["cris_tonaldo", "cap_africa", "lionel_nessi", "ryan_man"]
    lista_mini = []
    lista_default = []
    lista_sons_select = []

    try:
        for i in range(len(lista_personagens)):
            mini = pygame.image.load(f"assets/tela_select/imagens/{lista_personagens[i]}_mini.png").convert_alpha()
            mini = pygame.transform.scale(mini, (50, 50))
            lista_mini.append(mini)
            default = pygame.image.load(f"assets/tela_select/imagens/{lista_personagens[i]}_grande.png").convert_alpha()
            lista_default.append(default)
            lista_sons_select.append(pygame.mixer.Sound(f"assets/tela_select/sons/{lista_personagens[i]}.mp3"))
    except Exception as e:
        print(e)
    clock = pygame.time.Clock()
    run = True

    menu = Menu(245, 55)
    config = TelaConfig(0.5, 0.5, "assets/fundo/1.png", "assets/2.png", "assets/fundo/3.png")
    fundo_menu = menu.fundo_tela(800, 600, "assets/fundo/1.png")
    menu.titulo_menu(fonte_titulo, "Imortal Kombat", (0, 0, 0))
    menu.criar_botao(fonte)
    menu.tocar_musica(musica)
    
    
    elem_inds = ElemIndependente(largura, nuvem)

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            clique = menu.acoes_menu(event)

            if clique == 0:
                # === JOGAR ===
                pygame.mixer.music.stop()
                select = TelaSelect(
                    lista_personagens, lista_mini, lista_default, lista_sons_select,
                    config.volume_ef, config.volume_mus
                )
                res = select.exibir(tela, fonte, fundo)
                nome = lista_personagens[res]
                tam_sprites = lista_n_sprites[res]
                config.volume_ef = select.volume_ef
                config.volume_mus = select.volume_mus
                
                player = manager_ranking.verifica_player(nomejogador, nome, tam_sprites, 200, altura - 150)
                if player is None:
                    player = Jogador(nome, tam_sprites, 200, altura - 150)

                # Inimigo aleatório
                sorteio = random.randint(0, 3)
                nome_bot = lista_personagens[sorteio]
                sprites_bot = lista_n_sprites[sorteio]
                bot = Inimigo(nome_bot, sprites_bot, 400, altura - 150)
                
                jogar = TelaJogar(player, bot, fundo, config.volume_ef * 100, config.volume_mus * 100, elem_inds)
                sorteio = random.randint(1, 2)

                res = jogar.tela_fighting(tela, altura, largura, fonte, fundo_jogar, sorteio, soco)
                res_pausa = jogar.pausa(tela, fonte, fundo, res, soco)

                if res == 0 or res_pausa == 0:
                    config.volume_ef = jogar.volume_ef
                    config.volume_mus = jogar.volume_mus
                    pontos, sequencia = player.pontos, player.streak          
                    manager_ranking.adicionar(JogadorRanking(nomejogador, pontos, sequencia))
                    manager_ranking.salvar_ranking("ranking.json")
                    break

            elif clique == 1:
                ranking = TelaRanking("assets/fundo/4.jpg")
                ranking.ranking(tela, fonte, fonte_titulo)

            elif clique == 2:
                config = TelaConfig(0.5, 0.5, "assets/fundo/1.png", "assets/fundo/3.png", "assets/fundo/2.png")
                config.config(tela, fonte, fonte_titulo)

            elif clique == 3:
                run = False
                pygame.quit()
                sys.exit()
 
        tela.blit(fundo_menu, (0, 0))
        menu.desenha_titulo_menu(tela)
        for botao in menu.botoes:
            botao.render_botao(tela)

        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()