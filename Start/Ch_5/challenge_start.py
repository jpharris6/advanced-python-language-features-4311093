# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for Structural Pattern Matching

# Dry Clean: [garment, size, starch, same_day]
#   garments are shirt, pants, jacket, dress
#   each item is 12.95, plus 2.00 for starch
#   same day service adds 10.00 per same-day item
# Wash and Fold: [description, weight]
#   4.95 per pound, with 10% off if more than 15 pounds
# Blankets: [type, dryclean, size]
#   type is "comforter" or "cover"
#   Flat fee of 25.00
# ---
# Output:
# Order Total Price

test_orders = [
    [
        ["shirt", "L", True, False],
        ["shirt", "M", True, False],
        ["shirt", "L", False, True],
        ["pants", "M", False, True],
        ["pants", "S", False, False],
        ["pants", "S", False, False],
        ["jacket", "M", False, False],
        ["jacket", "L", False, True]
    ],
    [
        ["dress", "M", False, True],
        ["whites", 5.25],
        ["darks", 12.5]
    ],
    [
        ["shirts and jeans", 28.0],
        ["comforter", False, "L"],
        ["cover", True, "L"],
        ["shirt", "L", True, True]
    ]
]

# TODO: process each order
for orders in test_orders:
    total = 0
    print("--------------")
    for order in orders:
        match order:
            case [garment, size, starch, same_day]:
                val = 12.95
                str = ""
                if starch:
                    val += 2.00
                    str = "Starched"
                if same_day:
                    val += 10.00
                    str = "same-day"
                print(f"Dry Clean: ({size}) {garment}" + str)
            case [description, weight]:
                val = weight * 4.95
                if weight > 15:
                    discount = val - (val * 0.1)
                    val = discount
                print(f"Wash/Fold: {description}, weight: {weight}")
            case[type, dryclean, size]:
                val = 25.00
                str = ""
                if dryclean:
                    str = "Dry Clean"
                print(f"Blanket: ({size}) {type} " + str)
            case _:
                print("This is not valid")
        total += val
    print(f"Order total: {total:0.2f}")
    print("--------------")
    

                    
            

