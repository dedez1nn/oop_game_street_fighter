import pygame
from .carregar_sprites import Sprites
import random


class ElemIndependente:
    def __init__(self, largura: int, nuvem: pygame.Surface):
        self.__retangulo_nuvem = nuvem.get_rect(topleft=(100,100))
        self.__largura = largura
        self.__nuvem = nuvem
        self.__fator_deslocamento = 1
        self.__spritess = Sprites("elem_independente", [4])
        self.__spritess.addsprites()
        self.__cooldown_tr = 0
        self.__sorteio = 100
    
    @property
    def sorteio(self):
        return self.__sorteio
    
    @sorteio.setter
    def sorteio(self, val: int):
        self.__sorteio = val
    
    @property
    def cooldown_tr(self):
        return self.__cooldown_tr
    
    @cooldown_tr.setter
    def cooldown_tr(self, val: int):
        self.__cooldown_tr = val
    
    @property
    def spritess(self):
        return self.__spritess
    
    @spritess.setter
    def spritess(self, val: Sprites):
        self.__spritess = val
        
    @property
    def fator_deslocamento(self):
        return self.__fator_deslocamento
    
    @fator_deslocamento.setter
    def fator_deslocamento(self, val: int):
        self.__fator_deslocamento = val
        
    @property
    def retangulo_nuvem(self):
        return self.__retangulo_nuvem
    
    @retangulo_nuvem.setter
    def retangulo_nuvem(self, val: pygame.Rect):
        self.__retangulo = val
        
    @property
    def largura(self):
        return self.__largura
    
    @largura.setter
    def largura(self, val: int):
        self.__largura = val
        
    @property
    def nuvem(self):
        return self.__nuvem
    
    @nuvem.setter
    def nuvem(self, val: pygame.image):
        self.__nuvem = val
        
    def loop_nuvem(self, largura: int):
        deslocamento = 2 * self.fator_deslocamento
        self.retangulo_nuvem.x += deslocamento
        if self.retangulo_nuvem.right >= self.largura:
            self.retangulo_nuvem.right = largura
            self.fator_deslocamento *= -1
        elif self.retangulo_nuvem.left == 0:
            self.retangulo_nuvem.left = 0
            self.fator_deslocamento *= -1
    
    
    def loop_trovao(self, superficie: pygame.Surface):
        if self.cooldown_tr == 0:  
            self.sorteio = random.randint(100, 500)  
            self.desenhar(superficie, 0, 0.5)
            self.cooldown_tr = 100
            
        if self.cooldown_tr > 0:
            self.cooldown_tr -= 10
            
    def desenhar(self, superficie, indice: int, vel: float):
        imagem = self.spritess.percorrer(indice, vel)
        imagem = pygame.transform.scale(imagem, (400, 600))
        superficie.blit(imagem, (self.sorteio, 0))
            
            
