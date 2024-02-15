import random

possible_games = ["pedra", "paper", "tissora"]
wins, loses, draws = 0, 0, 0
human_game = ""

while human_game != "q":
    human_game = input("Tria una jugada (pedra, paper, tissora) q for quit:\n")
    machine_game = random.choice(possible_games)
    if human_game == machine_game:
        # Draw
        print(f'Empat. Tu vas jugar {human_game}, i la màquina va jugar {machine_game}')
        draws += 1
    elif human_game == "pedra":
        if machine_game == "paper":
            # Loses
            print(f'Perds. Tu vas jugar {human_game}, i la màquina va jugar {machine_game}')
            loses += 1
        else:
            # Wins
            print(f'Guanyes!. Tu vas jugar {human_game}, i la màquina va jugar {machine_game}')
            wins += 1
    elif human_game == "paper":
        if machine_game == "tissora":
            # Loses
            print(f'Perds. Tu vas jugar {human_game}, i la màquina va jugar {machine_game}')
            loses += 1
        else:
            # Wins
            print(f'Guanyes!. Tu vas jugar {human_game}, i la màquina va jugar {machine_game}')
            wins += 1
    elif human_game == "tissora":
        if machine_game == "pedra":
            # Loses
            print(f'Perds. Tu vas jugar {human_game}, i la màquina va jugar {machine_game}')
            loses += 1
        else:
            # Wins
            print(f'Guanyes!. Tu vas jugar {human_game}, i la màquina va jugar {machine_game}')
            wins += 1
    elif human_game == "q":
        print("Gràcies per jugar!! Salut")
    else:
        print("Jugada incorrecta. Si us plau, introduiu un valor correcte")
    print(f'\n\tPartides guanyades: {wins}\n\tPartides empatades: {draws}\n\tPartides perdudes: {loses}\n')