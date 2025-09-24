number = int(input("Enter a number to see its multiplication table: "))


for table in range(1, 11):
  print(f"{number} * {table} = {number * table}")