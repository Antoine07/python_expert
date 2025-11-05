class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        
    def add_player(self, player):
        self.players.append(player)
        
    def total_score(self):
        s = 0
        for player in self.players:
            s += player.score
        return s
        
class Player:
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

players = [ 
           Player("Sylvain", 50), 
           Player("Zakaria", 49), 
           Player("Socrates", 49.5), 
           Player("Samia", 60),
           Player("Olivia", 60),
           Player("Rayan", 50),
           Player("Orlya", 50),
]

estima_players = Team("ESTIAM", players)
estima_players.add_player(Player("Chris", 60)) # création à la voler d'objet 

print( estima_players.total_score() )