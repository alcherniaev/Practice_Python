import random
 
PRIZE = 1
EMPTY = 0
TRIES = 100_000
 
doors = [PRIZE, EMPTY, EMPTY]
 
 
score_keeps = 0
score_changes = 0
 
for i in range(TRIES):
    random.shuffle(doors)
    player_choice = random.randrange(len(doors))  # Какую дверь выбрал игрок
 
    host_options = []
    for j, door in enumerate(doors):
        if j != player_choice and doors[j] != PRIZE:
            host_options.append(j)
    host_choice = random.choice(host_options)  # Какую дверь откроет ведущий
 
    # Игрок сохраняет выбор
    score_keeps += doors[player_choice]
 
    # Игрок меняет выбор
    player_options = []
    for j, door in enumerate(doors):
        if j != player_choice and j != host_choice:
            player_options.append(j)
    player_choice = random.choice(player_options)
    score_changes += doors[player_choice]
 
print(f'Из {TRIES} попыток: если игрок оставляет выбор - {score_keeps}, если меняет - {score_changes}')

