# must return 2
# cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
# cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
#


# Wrong result for recipe
# {'chocolate': 50, 'crumbles': 62, 'eggs': 29}
# and available ingredients
# {'apples': 536, 'cocoa': 6956, 'crumbles': 61, 'butter': 947, 'flour': 4397, 'eggs': 3049, 'oil': 8712, 'pears': 8973, 'chocolate': 6957, 'nuts': 2828}:
# 105 should equal 0


def cakes(recipe: dict, available: dict) -> int:
    result = 10000000000000
    for i in recipe:
        if available.get(i) is None:
            return 0
        else:
            if available.get(i) // recipe.get(i) < result:
                result = available.get(i) // recipe.get(i)
    return result



print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))

