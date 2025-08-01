import pygame
from .personagem_base import PersonagemBase
import random

class Inimigo(PersonagemBase):
     def __init__(self, nome: str, listar: list, x: int, y: int):
        super().__init__(nome, listar, x, y)
        self.__cooldownd = 0
        self.__cooldown_block = 0
        self.__terminar_defesa = 30
     
     @property
     def terminar_defesa(self):
        return self.__terminar_defesa
    
     @terminar_defesa.setter
     def terminar_defesa(self, val: int):
        self.__terminar_defesa = val
        
     @property
     def cooldownd(self):
        return self.__cooldownd
    
     @cooldownd.setter
     def cooldownd(self, val: int):
        self.__cooldownd = val 
        
     @property
     def cooldown_block(self):
        return self.__cooldown_block
    
     @cooldown_block.setter
     def cooldown_block(self, val: int):
        self.__cooldown_block = val
        
     def actions(self, superficie: pygame.Surface, largura: int, alvo: PersonagemBase, soco: pygame.mixer.Sound):
        deslocamento = 0
            
        if self.retangulo.x > alvo.retangulo.x:
            self.flip = True
            deslocamento = -2
        else:
            self.flip = False
            deslocamento = 2
        
        if self.estados.atingido:
            self.retangulo.x += -(deslocamento * 2.5)
            
        if self.retangulo.x <= 0:
            self.retangulo.x = 0
            self.estados.andando = False
        if self.retangulo.right >= largura:
            self.retangulo.right = largura
            self.estados.andando = False

        if not self.estados.atingido and not self.estados.soco and not self.estados.pulando:
            if self.retangulo.colliderect(alvo.retangulo) and self.cooldownd == 0:    
                if self.ataquecdr == 0:
                    self.estados.soco = True         
                    self.estados.andando = False 
                    self.cooldownd = 40             
            elif self.cooldownd > 0:
                if not self.estados.defesa:
                    self.retangulo.x += -deslocamento * (1/2)    
                    self.estados.andando = True      
                if self.cooldownd <= 10 and self.cooldown_block == 0:
                    self.estados.defesa = True                    
            else:
                if not self.estados.defesa and not self.retangulo.colliderect(alvo.retangulo):
                    self.estados.andando = True              
                    self.retangulo.x += deslocamento
            
        if self.ataquecdr > 0:
            self.ataquecdr -= 0.25
        if self.__cooldownd > 0:
            self.__cooldownd -= 0.25
        if self.__cooldown_block > 0:
            self.__cooldown_block -= 0.25
            

        self.atualizar_animacao(superficie, alvo, 60, soco) #superficie, player, cdratk
        self.estados.resetar_estados()
        
     def actions_2(self, superficie: pygame.Surface, largura: int, alvo: PersonagemBase, soco: pygame.mixer.Sound):
        deslocamento = 0
        
        
        if self.retangulo.x > alvo.retangulo.x:
            self.flip = True
            deslocamento = -2
        else:
            self.flip = False
            deslocamento = 2
            
        if self.estados.atingido:
            self.retangulo.x += -(deslocamento * 2.5)
        
        if self.retangulo.x <= 0:
            self.retangulo.x = 0
            self.estados.andando = False
        elif self.retangulo.right >= largura:
            self.retangulo.right = largura
            self.estados.andando = False 
            
            
        if self.terminar_defesa == 0:
            self.terminar_defesa = 30
            self.cooldown_block = 50       
            
        if not self.estados.atingido and not self.estados.soco and not self.estados.pulando:
            if self.retangulo.colliderect(alvo.retangulo) and self.cooldownd == 0:  
                if self.cooldown_block == 0:
                    self.estados.defesa = True
                    self.estados.andando = False
                    self.estados.defesa = True
                    self.terminar_defesa -= 1               
                elif self.cooldown_block > 0:
                    sorteio = random.randint(1,2)
                    if self.ataquecdr == 0:
                        if sorteio == 1:
                            self.estados.soco = True
                        if sorteio == 2:
                            print(self.especial)
                            if self.especial >= 100:
                                self.estados.special = True
                                self.cooldownd = 20
                            else:
                                self.estados.chute = True
                                self.cooldownd = 20
                else:
                    self.retangulo.x += deslocamento * -1
                    self.estados.andando = True
            else:
                if not self.retangulo.colliderect(alvo.retangulo):
                    self.retangulo.x += deslocamento
                    self.estados.andando = True
        
        if self.cooldown_block > 0:
            self.cooldown_block -= 0.50
        if self.cooldownd > 0:
            self.cooldownd -= 1
        if self.ataquecdr > 0:
            self.ataquecdr -= 0.25
            
        self.atualizar_animacao(superficie, alvo, 30, soco) #superficie, player, cdratk
        self.estados.resetar_estados()
        
        
     def actions_3(self, superficie: pygame.Surface, largura: int, alvo: PersonagemBase, soco: pygame.mixer.Sound):
        self.atualizar_animacao(superficie, alvo, 30, soco) #superficie, player, cdratk
        self.estados.resetar_estados()
        
    
                    
            
            
            
        
        
        