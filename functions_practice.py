def hello():
   print("Greetings User")

hello()

def pack(first_name, last_name, birth_year):
    return[first_name, last_name, birth_year]

print(pack("Jo", "Carr", "1999"))



def my_food(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

my_food(["Tacos", "Burrito", "strawberries", "blueberries", "Quesadillas"])

my_food([])
