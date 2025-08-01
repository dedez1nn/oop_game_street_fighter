import json
import os
from .jogador_ranking import JogadorRanking
from character.player import Jogador

class ManagerRanking:
    def __init__(self):
        self.__jogadores = []
        self.__obj_jogadores = []
        
    @property
    def obj_jogadores(self):
        return self.__obj_jogadores
    
    @obj_jogadores.setter
    def obj_jogadores(self, val: list):
        self.__obj_jogadores = val
    
    @property
    def jogadores(self):
        return self.__jogadores
    
    @jogadores.setter
    def jogadores(self, val: list):
        self.__jogadores = val
    
    def adicionar(self, novo_jogador: JogadorRanking):
        for i, jogador in enumerate(self.jogadores):
            if jogador.nome == novo_jogador.nome:
                # Só atualiza se a nova pontuação for maior
                if novo_jogador.sequencia > jogador.sequencia:
                    self.jogadores[i] = novo_jogador
                return  # Já encontrou, não precisa continuar
        # Se não encontrou, adiciona
        self.jogadores.append(novo_jogador)

        
    def ordenar_e_limitar(self):
        self.jogadores.sort(key=lambda x: x.sequencia, reverse=True)
        self.jogadores = self.jogadores[:5]

    def salvar_ranking(self, nome_arquivo: str):
    # Verifica se a lista de jogadores não está vazia antes de salvar
        if not self.jogadores:
            print("Nenhum jogador no ranking para salvar!")
            return  # Se a lista estiver vazia, não salva o arquivo

        pasta_dados = os.path.join(os.path.dirname(__file__), 'dados')
        if not os.path.exists(pasta_dados):
            os.makedirs(pasta_dados)  # Cria a pasta 'dados' se não existir

        caminho = os.path.join(pasta_dados, nome_arquivo)
        print(f"Salvando no arquivo: {caminho}")

    # Salva os dados no arquivo JSON
        with open(caminho, "w") as f:
            json.dump([j.to_dict() for j in self.jogadores], f, indent=4)
            print(f"Ranking salvo no arquivo: {caminho}")


    def carrega_arquivo(self, nome_arquivo: str):
        pasta_dados = os.path.join(os.path.dirname(__file__), 'dados')
        caminho = os.path.join(pasta_dados, nome_arquivo)
        try:
            with open(caminho, "r") as f:
                dados = json.load(f)
                self.jogadores = [JogadorRanking.from_dict(d) for d in dados]
                self.ordenar_e_limitar()
    
        except FileNotFoundError:
            print(f"Arquivo {nome_arquivo} não encontrado. Criando novo ranking.")
            self.jogadores = []
        
        except json.JSONDecodeError:
            print(f"Erro ao ler o arquivo {nome_arquivo} Criando novo ranking.")
            self.jogadores = []
    
        
            
    def verifica_player(self, nome_jogador: str, nome_personagem: str, sprites: list, x: int, y: int):
        for jogador in self.jogadores:
            if jogador.nome == nome_jogador:
                player = Jogador(nome_personagem, sprites, x, y)
                player.pontos = jogador.pontuacao
                player.streak = jogador.sequencia
                return player
        return None

        

