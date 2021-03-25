import random
print('rock')
print('paper')
print('love')

player1 = input('Player 1 dame tu movimiento ')
player2 = input('Player 2 dame tu movimiento ')
print(random.randint(0, 2))

if player1 == player2:
    print("empate con " + player1)
elif player1 == "rock":

    if player2 == "love":
        print("Jugador 1 gana con " + player1)
    elif player2 == "paper":
        print("Jugador 2 gana con " + player2)
elif player1 == "paper":
    if player2 == "rock":
        print("Jugador 2 gana con " + player2)
    elif player2 == "love":
        print("Jugador 1 gana con " + player1)
elif player1 == "love":
    if player2 == "rock":
        print("Jugador 1 gana con " + player1)
    elif player2 == "paper":
        print("Jugador 2 gana con " + player2)

for item in range(1, 21):

    print(item)

for item in range(1, 10):
    print("\U0001f600"*item)

times = 11
while times >= 1:
    print("\U0001f600"*item)
    times -=1