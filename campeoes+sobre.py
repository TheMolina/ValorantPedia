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
    Campeao(
        "Omen", 
        "Controller", 
        ["Shrouded Step", "Paranoia", "Dark Cover", "From the Shadows"],
        "Omen é um ser misterioso, capaz de se mover pelas sombras e manipular a percepção dos inimigos.",
        "Alto"
    ),
    Campeao(
        "Raze", 
        "Duelist", 
        ["Boom Bot", "Blast Pack", "Paint Shells", "Showstopper"],
        "Raze é uma especialista em explosivos, utilizando bombas e granadas para causar destruição em massa.",
        "Alto"
    ),
    Campeao(
        "Reyna", 
        "Duelist", 
        ["Leer", "Dismissing", "Devour", "Empress"],
        "Reyna é uma guerreira feroz que se fortalece à medida que elimina seus inimigos.",
        "Alto"
    ),
    Campeao(
        "Breach", 
        "Initiator", 
        ["Flashpoint", "Aftershock", "Fault Line", "Rolling Thunder"],
        "Breach é um especialista em iniciar combates, utilizando suas habilidades para desestabilizar os inimigos.",
        "Médio"
    ),
    Campeao(
        "Sova", 
        "Initiator", 
        ["Owl Drone", "Shock Bolt", "Recon Bolt", "Hunter's Fury"],
        "Sova é um mestre da vigilância, rastreando e revelando os inimigos com suas habilidades de precisão.",
        "Alto"
    ),
    Campeao(
        "Killjoy", 
        "Sentinel", 
        ["Nanoswarm", "Lockdown", "Turret", "Lockdown"],
        "Killjoy é uma inventora inteligente, capaz de usar tecnologia para controlar o campo de batalha.",
        "Médio"
    ),
    Campeao(
        "Astra", 
        "Controller", 
        ["Gravity Well", "Nova Pulse", "Nebula", "Astral Form"],
        "Astra é uma controladora cósmica que manipula as estrelas para afetar o campo de batalha.",
        "Alto"
    ),
    Campeao(
        "KAY/O", 
        "Initiator", 
        ["FRAG/ment", "ZERO/point", "FLASH/drive", "NULL/cmd"],
        "KAY/O é um ex-soldado robótico com habilidades voltadas para neutralizar as habilidades inimigas.",
        "Médio"
    ),
    Campeao(
        "Yoru", 
        "Duelist", 
        ["Blindside", "Gatecrash", "Fakeout", "Dimensional Drift"],
        "Yoru é um duelista enigmático, capaz de manipular portais e enganar os inimigos.",
        "Alto"
    )

]

# Exibindo as informações dos campeões
for campeao in campeoes:
    campeao.exibir_informacoes()
