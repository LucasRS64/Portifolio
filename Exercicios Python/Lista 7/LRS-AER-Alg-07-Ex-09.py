import random

def generate_bingo_calls():
    return [f"{letter}{number}" for letter in "BINGO" for number in range(1, 16)]

def shuffle_bingo_calls(calls):
    random.shuffle(calls)
    return calls

def generate_bingo_card():
    card = []
    for letter_index in range(5):
        column = random.sample(range(1 + 15 * letter_index, 16 + 15 * letter_index), 5)
        card.append(column)
    card[2][2] = 0  # Espaço central é um "free space"
    return [list(row) for row in zip(*card)]

def mark_bingo_card(card, call):
    letter, number = call[0], int(call[1:])
    col_index = "BINGO".index(letter)
    for row in card:
        if row[col_index] == number:
            row[col_index] = 0


def is_bingo_winner(cartela):
    for row in cartela:
        if sum(row) == 0:
            return True

    for col in range(5):
        if sum(cartela[row][col] for row in range(5)) == 0:
            return True

    if sum(cartela[i][i] for i in range(5)) == 0:
        return True

    if sum(cartela[i][4-i] for i in range(5)) == 0:
        return True

    return False

def simulate_bingo_game():
    calls = generate_bingo_calls()
    shuffle_bingo_calls(calls)
    card = generate_bingo_card()
    
    for call_count, call in enumerate(calls, start=1):
        mark_bingo_card(card, call)
        if is_bingo_winner(card):
            return call_count
    return len(calls)  

def main():
    num_simulations = 1000
    results = [simulate_bingo_game() for _ in range(num_simulations)]
    
    min_calls = min(results)
    max_calls = max(results)
    avg_calls = sum(results) / num_simulations
    
    print(f"Resultados após {num_simulations} simulações:")
    print(f"Mínimo de chamadas: {min_calls}")
    print(f"Máximo de chamadas: {max_calls}")
    print(f"Média de chamadas: {avg_calls:.2f}")

if __name__ == "__main__":
    main()