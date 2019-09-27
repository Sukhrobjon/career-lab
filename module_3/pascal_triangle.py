def pascal_triangle(num_rows):
    """
    Generate nth order Pascal triabgle with equal n number of rows 
    """
    # pascal_tri = [[0 for i in range(num_rows)] for j in range(num_rows)]
    pascal = []
    curr_row = []
    for row in range(0, num_rows):
        for col in range(0, row + 1):
            if col == 0 or col == row:
                print("1", end=" ")
                curr_row.append(1)
            else:
                coef = pascal[row-1][col-1] + pascal[row-1][col]
                print(coef, end=" ")

                curr_row.append(coef)
            # curr_row.append(row)
        pascal.append(curr_row)
        # print(f"current row: {curr_row}")
        curr_row = []
        print()
    print(pascal)
pascal_triangle(5)
