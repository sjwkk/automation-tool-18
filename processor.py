import random
import time

class GameProcessor:
    def __init__(self):
        self.score = 0
        self.level = 1

    def random_event(self):
        event = random.choice(['bonus', 'trap', 'none'])
        return event

    def update_score(self, event):
        if event == 'bonus':
            self.score += 10 * self.level
        elif event == 'trap':
            self.score -= 5 * self.level
        return self.score

    def level_up(self):
        self.level += 1
        return self.level

    def play_turn(self):
        event = self.random_event()
        self.update_score(event)
        if event == 'bonus':
            print(f'Bonus event! Score: {self.score}')
        elif event == 'trap':
            print(f'Trap event! Score: {self.score}')
        else:
            print(f'No event. Score remains: {self.score}')
        if self.score >= 50:
            self.level_up()
            print(f'Level up! New level: {self.level}')

if __name__ == '__main__':
    processor = GameProcessor()
    for _ in range(10):
        processor.play_turn()  
        time.sleep(1)  
