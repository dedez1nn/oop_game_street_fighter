import pygame
from screen.button import Botao

class Menu:
    def __init__(self, x: int, y: int):
        self.__titulo = None
        self.__posicao_titulo = (x, y)
        self.__botoes = []
        self.__volume_mus = 0.5
        
    @property
    def volume_mus(self):
        return self.__volume_mus
    
    @volume_mus.setter
    def volume_mus(self, val: float):
        self.__volume_mus = val

    @property
    def botoes(self):
        return self.__botoes

    @botoes.setter
    def botoes(self, val: list):
        self.__botoes = val

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, val: str):
        self.__titulo = val

    @property
    def posicao_titulo(self):
        return self.__posicao_titulo

    @posicao_titulo.setter
    def posicao_titulo(self, val: tuple):
        self.__posicao_titulo = val

    def tela(self, largura: int, altura: int):
        return pygame.display.set_mode((largura, altura))

    def fundo_tela(self, largura: int, altura: int, img: str)-> pygame.Surface:
        fundo = pygame.image.load(img).convert_alpha()
        fundo = pygame.transform.scale(fundo, (largura, altura))
        return fundo

    def titulo_menu(self, fonte: pygame.font.Font, texto: str, cor: tuple):
        self.titulo_renderizado = fonte.render(texto, True, cor)

    def desenha_titulo_menu(self, tela: pygame.Surface):
        if self.titulo_renderizado:
            tela.blit(self.titulo_renderizado, self.posicao_titulo)

    def verifica_click(self, evento: pygame.event.Event)-> int:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for i, botao in enumerate(self.botoes):
                if botao.rect.collidepoint(evento.pos):
                    return i
        return None

    def criar_botao(self, fonte: pygame.font.Font):
        texto_botoes = ["Jogar", "Ranking", "Configuracoes", "Sair"]
        botoes_criados = []

        for i, texto in enumerate(texto_botoes):
            botao = Botao(300, 170 + i * 50)
            botao.titulo_botao(fonte, texto, (255, 255, 0))
            botoes_criados.append(botao)

        self.botoes = botoes_criados

    def tocar_musica(self, musica: str):
        pygame.mixer.music.load(musica)
        pygame.mixer.music.set_volume(self.volume_mus)
        pygame.mixer.music.play(-1)

    def acoes_menu(self, evento: pygame.event.Event):
        clique = self.verifica_click(evento)
        if clique is not None:
            if clique == 0:
                return 0

            elif clique == 1:
                return 1

            elif clique == 2:
                return 2

            elif clique == 3:
                return 3