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

def print_cartela(cartela):
    for row in cartela:
        print(" ".join(str(num) for num in row))
    print()

def main():
    cartelas = [
        [[0, 0, 0, 0, 0],  
         [1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20]],

        [[0, 1, 2, 3, 4],  
         [0, 6, 7, 8, 9],
         [0, 11, 12, 13, 14],
         [0, 16, 17, 18, 19],
         [0, 21, 22, 23, 24]],

        [[0, 1, 2, 3, 4],  
         [5, 0, 7, 8, 9],
         [10, 11, 0, 13, 14],
         [15, 16, 17, 0, 19],
         [20, 21, 22, 23, 0]],

        [[1, 2, 3, 4, 0],  
         [5, 6, 7, 0, 9],
         [10, 11, 0, 13, 14],
         [15, 0, 17, 18, 19],
         [0, 21, 22, 23, 24]],

        [[0, 1, 2, 3, 4],  
         [5, 0, 7, 8, 9],
         [10, 11, 0, 13, 14],
         [15, 16, 17, 0, 19],
         [20, 21, 22, 23, 24]]
    ]

    for i, cartela in enumerate(cartelas):
        print(f"Cartela {i+1}:")
        print_cartela(cartela)
        if is_bingo_winner(cartela):
            print("Essa cartela é vencedora!\n")
        else:
            print("Essa cartela não é vencedora.\n")

if __name__ == "__main__":
    main()