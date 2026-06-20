class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score  = score

    def info(self):
        print(f"Cricket Player: {self.__player}, Cricket Score: {self.__score}")

    def play(self):
        print(f"{self.__player} hits a six!")

    def get_score(self):
        return self.__score
    
    def set_score(self, new_score):
        if new_score >= 0:
           self.__score = new_score
        else:
            print("Update a valid score")

class Football:
    def __init__(self, player, score):
        self.__player = player
        self.__score  = score

    def info(self):
        print(f"Football Player: {self.__player}, Football Score: {self.__score}")

    def play(self):
        print(f"{self.__player} scores a goal!")

    def get_score(self):
        return self.__score
    
    def set_score(self, new_score):
        if new_score >= 0:
           self.__score = new_score
        else:
            print("Update a valid score")

cricket = Cricket("Tendulkar", 85)
football = Football("Messi", 3)

for player in [cricket, football]:
    player.info()
    player.play()

cricket.__score = 999
print(cricket.get_score())
cricket.set_score(100)
print(cricket.get_score())

football.__score = 10
print(football.get_score())
football.set_score(5)
print(football.get_score())