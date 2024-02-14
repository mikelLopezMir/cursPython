# farem una segona versió del joc pedra, paper, tissores, però aquest cop amb diccionaris

import random

possible_games = ["pedra", "paper", "tissora"]
winning_games = { "pedra": "tissora", "paper": "pedra", "tissora": "paper" }
wins, loses, draws = 0, 0, 0
human_game = ""

while human_game != "q":
    human_game = input("Tria una jugada (pedra, paper, tissora) q for quit:\n")
    machine_game = random.choice(possible_games)
    if human_game == "q":
        print("Gràcies per jugar!! Salut")
    elif human_game not in possible_games:
        print("Jugada incorrecta. Si us plau, introduiu un valor correcte")
    elif human_game == machine_game:
        # Draw
        print(f'Empat. Tu vas jugar {human_game}, i la màquina va jugar {machine_game}')
        draws += 1
    elif winning_games[human_game] == machine_game:
        # Wins
        print(f'Guanyes!. Tu vas jugar {human_game}, i la màquina va jugar {machine_game}')
        wins += 1
    else:
        # Loses
        print(f'Perds. Tu vas jugar {human_game}, i la màquina va jugar {machine_game}')
        loses += 1

    print(f'\n\tPartides guanyades: {wins}\n\tPartides empatades: {draws}\n\tPartides perdudes: {loses}\n')