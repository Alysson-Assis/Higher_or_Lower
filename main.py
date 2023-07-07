import random
from game_data import data


def clear():
    import os
    os.system('clear') or None


def descrição(conta):
    name = conta["name"]
    description = conta['description']
    pais = conta['country']
    return f"{name}, a {description}, from {pais}"


def compare(check_answer, Afollower, Bfollower):
    if Afollower > Bfollower:
        return check_answer == "a"
    else:
        return check_answer == "b"


game_is_on = True
conta_B = random.choice(data)
score = 0

while game_is_on:
    conta_A = conta_B
    conta_B = random.choice(data)
    if conta_A == conta_B:
        conta_B = random.choice(data)

    print(f"Compare A: {descrição(conta_A)}")
    print("VS")
    print(f"Compare B: {descrição(conta_B)}")

    answer = input("Quem tem mais seguidores? Digite 'A' ou 'B': ").lower()

    seguidores_contaA = conta_A["follower_count"]
    seguidores_contaB = conta_B["follower_count"]

    correto = compare(answer, seguidores_contaA, seguidores_contaB)

    if correto:
        score += 1
        print(f"Você acertou! Atual pontuação: {score}")
    else:
        game_is_on = False
        print(f"Descupa, isso está errado. Pontução final: {score}")
