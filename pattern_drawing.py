x = int(input("Enter the size of the pattern "))
y = x
rows = 0

while rows < x:
    for col in range(y):
        print("*", end="")
    print()  # move to next line
    rows += 1