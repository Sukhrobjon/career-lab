def draw_grid():
    for i in range(8):
        for _ in range(i):
            print("* ", end="")
        print("")


# draw_grid()

def draw_pattern(row):
    for i in range(0, row):
        for j in range(0, i+1):
            print("* ", end="")

    print()

(draw_pattern(4))