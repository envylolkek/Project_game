from func import *
print('тебе нужно хорошо сдать егэ по информатике, чтобы это сделать надо победить трёх противников')
sleep(3)
name=input('игрок, как тебя зовут?:      ')
player['name']=name 

c_enemy = 0

while True:
    action=input('''Выберите действие:
1 - в бой
2 - тренировка
3 - магазин 
4 - получить валюту
5 - показать инвентарь
6 - информация об игроке
7 - информация о текущем противнике
8 - использовать аптечку
9 - использовать зелье силы
''')
    
    if action == '1':
        c_enemy = fight(c_enemy)

    if action == '2':
        training()
    
    if action == '3':
        shop()

    if action =='4':
        get_money()

    if action == '5':
        display_inventory()

    if action == '6':
        display_player()

    if action == '7':
        display_enemy(c_enemy)

    if action == '8':
        use_med()
    
    if action == '9':
        use_silla()

    if c_enemy==3:
        print('вы получили благословление трёх небожителей, с таким багажом знаний вы сможете сдать егэ без проблем. Поздравляем и благодарим за прохождение игры!!!')
        break