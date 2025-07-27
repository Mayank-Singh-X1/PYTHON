# class dog:
#     def __init__(self,name,age):
#         self.Name=name
#         self.Age=age

#     def sit(self):
#         print(f"{self.Name} is sitting")

#     def rollover(self):
#         print(f"{self.Age} is jutst a nmber")

# mydog=dog('madharchod', 45)
# mydog=dog('piyush',3)
# print(f"{mydog.Name} is name and age is {mydog.Age}")
# mydog.sit()
# mydog.rollover()
# print(mydog.Name)

# class restaurants:
#     def __init__(self,restaurant_name, cuisine ):
#         self.name=restaurant_name
#         self.Cuisine=cuisine

#     def descibe_restaurant(self):
#         print("Best restaurant in world")

#     def open_restaurant(self):
#         print("Resaturant is open")

# a=restaurants("reyansh","Italinan")
# print(f"name is {a.name} and cuisine is {a.Cuisine}")

# a.descibe_restaurant()
# a.open_restaurant()

class CAR:
    def __init__(self, brand, year, color):
        self.Brand=brand
        self.Year=year
        self.Color=color

    def description(self):
        print(f"{self.Brand} is manufactured in {self.Year} and coloor is {self.Color}")
    def mileage(self,run):
        self.Run=run
        print(f"Total run is {self.Run}")

class electric(CAR):
    def __init__(self,brand,year,color):
        super().__init__( brand, year, color)

    def __str__(self):
        return  f"{self.Brand} is manufactured in {self.Year} and coloor is {self.Color}" 

c1=CAR("honda",2024,"biluuu")
# c1.Brand="hefhje"
c1.mileage(30)
c1.description()


    
a3=electric("bomm",343,"neon")
print(a3)
