# # car="audi"
# # print(car.title()=="Audi
# # div=[x for x in range (0,100) if x%5==0]
# # print(div)

# # print((5>3) and (4<5))

# # toppings=["sauce","onions","milk"]
# # print("milkw" not in toppings)

# a=50
# if (a<18):
#   print("hello")
# elif(a<10):
#   print("boom")
# else:('kaboom')

# available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']

# requested_toppings = ['mushrooms', 'olives', 'green peppeers']

# for requested_topping in requested_toppings:
#   if requested_topping in available_toppings:
#     print(f"adding {requested_topping} to your pizza")
#   else:
#     print(f"sorry we ran out of {requested_topping}")

# print("hello")

#DICTIONARIES

# if alien["speed"]=="medium":
#     alien["x_pos"] +=2

# del alien["points"]
# print(alien)


# for key in alien:
#     print(f"{key} \n")

# a=[1,2,3,44,55,6,6,6,7,7,8]
# print(set(a))
# river={"nile":"egypt","ganga":"india","yamuna":'bihar'}
# for x,y in river.items():
#     print(f"The {x} runs through {y}")

# alien=[]
# for i in range(30):
#     new_alien={"color":"green","points":5,"speed":"medium"}
#     alien.append(new_alien)

# for k in alien[:5:2]:
#     print(k)

# aliens = []
#  # Make 30 green aliens.
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#  # Show the first 5 aliens.
# for alien in aliens[:5]:
#     print(alien)
# print("...")

# for i in range(0,100,2):
#     print(i)

pizza={
    "crust":"thick",
    "toppings":["cheese","pepperoni"]
}
for i in pizza["toppings"]:
    print(i)
print(f"you ordered crust {pizza["crust"]} with toppings {i}")