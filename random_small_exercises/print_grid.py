def draw_chessboard(row):
    for i in range(row):
        for _ in range(row):
            if i % 2 == 0:
                print("* ", end="")
            else:
                print(" *", end="")
        print()

row = 8
draw_chessboard(row)