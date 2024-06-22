from data import *
from time import *
from random import *

def training():
    for i in range(4):
        print(f'тренировка выполнена на {20*(i+1)}%')
        sleep(2)
    player["attack"]+=2
    print(f'теперь ваша атака равна {player["attack"]}')
    print('')
    
def display_player():
    print(f'игрок - {player["name"]}')
    print(f'здоровье - {player["hp"]}')
    print(f'атака - {player["attack"]}')
    print(f'деньги - {player["money"]}')
    print(f'удача - {player["luck"]}')
    print(f'защита - {player["armor"]}')

def display_enemy(c_enemy):
    enemy = enemies[c_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Здоровье - {enemy["hp"]}')
    print(f'Атака - {enemy["attack"]}')

def fight(c_enemy):
    print('битва начинается')
    sleep(1)
    enemy = enemies[c_enemy]
    print(enemy["script"])
    sleep(1)
    while player["hp"]>0 and enemy["hp"]>0:
        player["hp"]-=enemy["attack"]
        enemy["hp"]-=player["attack"]
        print(f'ваше здоровье равно {player["hp"]}, здоровье противника равно {enemy["hp"]}')
        print()
        sleep(1)
    if enemy["hp"]<=0:
        print(enemy["win"])
        print(f'ваше здоровье равно {player["hp"]}')
        c_enemy+=1
    else:
        print(enemy["loss"])
        sleep(2)
        print('вы проиграли, попробуйте еще раз')
    return c_enemy
        
def get_money():
    print('вы нашли волшебный банкомат, вы можете получить деньги, а можете и нет. А также у него есть еще и одна особенность - он ОЧЕНЬ медленно работает')
    sleep(3)
    a= randint(1,20)
    b= randint(1,10)
    print(f'шанс того, что вы получите деньги равен {a}, шанс получить ничего равен {b}')
    sleep(3)
    for h in range(4):
        print('подождите, операция выполняется...')
        sleep(1)
    if a>b:
        c=randint(10, 45)
        print(f'вы получили {c} денег!!')
        player["money"]+=c
    else:
        print('вы ничего не получили((((')

def display_inventory():
    print()
    print(f'аптечки = {inventory["аптечка"]}')
    print(f'зелья силы = {inventory["зелье силы"]}')
    print(f'ваши деньги = {player["money"]}')
    print()

def shop():
    print('''вы попали в магазин
          здесь вы можете купить:
          аптечку = 80 монет
          зелье силы 50 монет''')
    sleep(3)
    print('''что покупаем?
          1 - аптечка
          2 - зелье силы
          3 - выход из магазина''')
    n=int(input())
    if n == 1:
        if player["money"]>=80:
            print('аптечка добавлена в инвентарь')
            player["money"]-=80
            inventory["аптечка"]+=1
        else:
            print('недостаточно средств')
    elif n == 2:
        if player["money"]>=50:
            print('зелье силы добавлено в инвентарь')
            player["money"]-=50
            inventory["зелье силы"]+=1
        else:
            print('недостаточно средств')
    elif n==3:
        print('досвидания!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

def use_med():
    if inventory["аптечка"]>0:
        inventory["аптечка"]-=1
        player["hp"]+=20
        print(f'ваше здоровье увеличено на 20 едениц и равно {player["hp"]}')
    else:
        print('у вас нет аптечек')

def use_silla():
    if inventory["зелье силы"]>0:
        inventory["зелье силы"]-=1
        player["attack"]+=6
        print(f'ваша сила атаки увеличена на 6 едениц и равно {player["attack"]}')
    else:
        print('у вас нет зельев силы')