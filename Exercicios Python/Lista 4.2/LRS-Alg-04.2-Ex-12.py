for x in range(1, 11):
    print(f"{x:2}|", end="")
    for y in range(1, 11):
        print(f"{x*y:4}", end="")
    print()