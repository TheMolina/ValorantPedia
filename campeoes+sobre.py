class Campeao:
    def __init__(self, nome, classe, habilidades, descricao=None, poder=None):
        self.nome = nome
        self.classe = classe
        self.habilidades = habilidades
        self.descricao = descricao  # Descrição do personagem
        self.poder = poder  # Ról de poder (ex: baixo, médio, alto)

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Classe: {self.classe}")
        print(f"Habilidades: {', '.join(self.habilidades)}")
        if self.descricao:
            print(f"Descrição: {self.descricao}")
        if self.poder:
            print(f"Poder: {self.poder}")
        print("-" * 30)

# Criando a lista de campeões com informações adicionais
campeoes = [
    Campeao(
        "Brimstone", 
        "Controller", 
        ["Incendiary", "Sky Smoke", "Stim Beacon", "Orbital Strike"],
        "Brimstone é um veterano estrategista militar, com habilidades de controle de zona.",
        "Alto"
    ),
    Campeao(
        "Viper", 
        "Controller", 
        ["Snake Bite", "Toxic Screen", "Poison Cloud", "Viper's Pit"],
        "Viper é uma especialista em armamentos tóxicos, controlando o campo com veneno.",
        "Médio"
    ),
    Campeao(
        "Jett", 
        "Duelist", 
        ["Cloudburst", "Updraft", "Tailwind", "Bladestorm"],
        "Jett é uma lutadora ágil que usa o vento para se mover rapidamente e confundir os inimigos.",
        "Alto"
    ),
    Campeao(
        "Phoenix", 
        "Duelist", 
        ["Blaze", "Curveball", "Hot Hands", "Run It Back"],
        "Phoenix é um combatente imbatível que pode se curar e ressuscitar a si mesmo.",
        "Médio"
    ),
    Campeao(
        "Sage", 
        "Sentinel", 
        ["Barrier Orb", "Slow Orb", "Healing Orb", "Resurrection"],
        "Sage é uma curandeira poderosa com a habilidade de proteger e reviver seus aliados.",
        "Alto"
    ),
    Campeao(
        "Cypher", 
        "Sentinel", 
        ["Trapwire", "Cyber Cage", "Spycam", "Neural Theft"],
        "Cypher é um mestre do controle e da vigilância, mantendo os inimigos em alerta.",
        "Médio"
    ),
    # Continue para outros campeões...
]

# Exibindo as informações dos campeões
for campeao in campeoes:
    campeao.exibir_informacoes()
