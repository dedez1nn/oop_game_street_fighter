import pygame
from .personagem_base import PersonagemBase

class Jogador(PersonagemBase):
    def __init__(self, nome: str, listar: list, x: int, y: int):
        super().__init__(nome, listar, x, y)
        self.__pontos = 300
        self.__streak = 0
    
    @property
    def nome_player(self):
        return self.__nome_player
    
    @nome_player.setter
    def nome_player(self, val: str):
        self.__nome_player = val
    
    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self, val: int):
        self.__pontos = val

    @property
    def streak(self):
        return self.__streak
    
    @streak.setter
    def streak(self, val: int):
        self.__streak = val 
        
               
    def actions(self, superficie: pygame.Surface, altura: int, largura: int, alvo: PersonagemBase, soco: pygame.mixer.Sound):
        teclas = pygame.key.get_pressed()
        
        
        
        if self.retangulo.centerx > alvo.retangulo.centerx:
            self.flip = True
            deslocamento = 5
        else:
            self.flip = False
            deslocamento = -5
            
        if self.estados.atingido:
            self.retangulo.x += deslocamento
            
        if self.retangulo.x <= 0:
            self.retangulo.x = 0
        elif self.retangulo.right >= largura:
            self.retangulo.right = largura
        #movimentos player 1
        if not self.estados.atingido and not self.estados.soco and not self.estados.defesa:
                if teclas[pygame.K_a]:
                    nova_x = self.retangulo.x - 5
                    ret_temp = self.retangulo.copy()
                    ret_temp.x = nova_x
                    if nova_x >= 0 and not ret_temp.colliderect(alvo.retangulo):
                        self.retangulo.x = nova_x
                    self.estados.andando = True

                if teclas[pygame.K_d]:
                    nova_x = self.retangulo.x + 5
                    ret_temp = self.retangulo.copy()
                    ret_temp.x = nova_x
                    if nova_x + self.retangulo.width <= largura and not ret_temp.colliderect(alvo.retangulo):
                        self.retangulo.x = nova_x
                    self.estados.andando = True

                if teclas[pygame.K_w] and not self.fisica.no_ar and self.retangulo.y == altura - self.retangulo.height:
                    self.fisica.iniciar_pulo()
                    self.estados.pulando = True
                
                if not teclas[pygame.K_k]:
                    if teclas[pygame.K_f]:
                        self.estados.soco = True
                        
                    if teclas[pygame.K_t] and self.especial >= 100:
                        self.estados.special = True
                    
                    if teclas[pygame.K_r]:
                        self.estados.chute = True
                if teclas[pygame.K_k]:
                    self.estados.defesa = True
        #garantir um player sempre olhar para o outro
            
        #adicionar um cooldown
        if self.ataquecdr > 0:
            self.ataquecdr -= 1
 
        #metodo para pulo em fisica
        self.retangulo.y = self.fisica.aplicar_gravidade(self.retangulo.y, altura - self.retangulo.height)
        
        #resetar o estado de pulo
        if self.retangulo.y == altura - self.retangulo.height:
            self.estados.pulando = False
            
        
        #desenhar as animacoes na tela com base nos estados
        self.atualizar_animacao(superficie, alvo, 50, soco) #tela, inimigo e cdr ataque
        self.estados.resetar_estados()  