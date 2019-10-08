def unique_meals(meals):
    """
    Counts number of unique meals in the list of objects
    """
    
    unique_ingre = []

    for meal in meals:
        ingre = sorted(meal["ingredients"])
        if ingre not in unique_ingre:
            print(meal["name"])
            unique_ingre.append(ingre)

    return len(unique_ingre)


meals = [
    {
        "name": "burger a",
        "ingredients": "[1, 2, 3, 4]"
    },

    {
        "name": "burger b",
        "ingredients": "[4, 2, 3, 1]"
    },

    {
        "name": "burger c",
        "ingredients": "[3, 1, 3, 4]"
    }
]

result = unique_meals(meals)
print(result)
