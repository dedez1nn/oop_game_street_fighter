import pygame
class Botao:
    def __init__(self, x: int, y: int):
        self.__posicao_botao = (x, y)
        self.__titulo_renderizado = None  
        self.__rect = None 

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, valor: pygame.Rect):
        self.__rect = valor

    @property
    def posicao_botao(self):
        return self.__posicao_botao
    
    @posicao_botao.setter
    def posicao_botao(self, posicao: tuple):
        self.__posicao_botao = posicao
    # Getter para titulo_renderizado
    @property
    def titulo_renderizado(self):        
        return self.__titulo_renderizado

    # Setter para titulo_renderizado
    @titulo_renderizado.setter
    def titulo_renderizado(self, valor: pygame.Surface):
        self.__titulo_renderizado = valor

    def titulo_botao(self, fonte: pygame.font.Font, texto: str, cor: tuple):

        self.titulo_renderizado = fonte.render(texto, True, cor)
        self.rect = self.titulo_renderizado.get_rect(topleft=self.posicao_botao)

    def render_botao(self, tela: pygame.Surface):
        if self.titulo_renderizado:
            tela.blit(self.titulo_renderizado, self.posicao_botao)
    