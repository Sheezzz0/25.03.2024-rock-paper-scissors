import random
class Game():
    
    def __init__(self, all_types):
        self.all_types = all_types
    
    def player(self, player_type):
        self.player_type = player_type
        return player_type
    
    def computer(self, computer_type):
        self.computer_type = computer_type
        return print(f'Выбор компъютера: {computer_type}')
    
    def winner_check(self):
        if player_type == computer_type:
            return print('Ничья')
        elif player_type == 'Камень' and computer_type == 'Ножницы':
            return print('Игрок выиграл')
        elif player_type == 'Камень' and computer_type == 'Бумага':
            return print('Компьютер выиграл')
        elif player_type == 'Ножницы' and computer_type == 'Бумага':
            return print('Игрок выиграл')
        elif player_type == 'Ножницы' and computer_type == 'Камень':
            return print('Компьютер выиграл') 
        elif player_type == 'Бумага' and computer_type == 'Камень':
            return print('Игрок выиграл')
        elif player_type == 'Бумага' and computer_type == 'Ножницы':
            return print('Компьютер выиграл')
        return

all_types = ['Камень', 'Ножницы', 'Бумага']
computer_type = random.choice(all_types)
player_type = input('Выберите одну из фигур: ')

def main():
    game = Game(all_types)
    game.player(player_type)
    game.computer(computer_type)
    game.winner_check()
    return
main()
main()