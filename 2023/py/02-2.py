class Game:
    id: int
    red: int = 0
    green: int = 0
    blue: int = 0
    def __init__(self, line: str):
        game_tag, balls = line.split(':')
        self.id = int(game_tag[4:])
        for show in balls.split(";"):
            red, green, blue = 0, 0, 0
            for ball in show.split(","):
                ball = ball.strip()
                if ball.endswith("red"):
                    red = int(ball[:-3])
                elif ball.endswith("green"):
                    green = int(ball[:-5])
                elif ball.endswith("blue"):
                    blue = int(ball[:-4])
                else:
                    assert False
            self.red = max(self.red, red)
            self.green = max(self.green, green)
            self.blue = max(self.blue, blue)
    def check(self, red, green, blue):
        return self.red <= red and self.green <= green and self.blue <= blue
    def power(self):
        return self.red * self.green * self.blue

with open("../input/02.txt") as f:
    print(sum(g.power() for g in map(lambda line: Game(line), f)))