# Exercise 4.3 - Treasure Map
# Takes user input for a row and column to place the "X"

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
print("Where would you like to bury the treasure?")

column_choice = (int(input("Pick a column choice: 1, 2, or 3? ")) - 1)
row_choice = (int(input("Pick a row choice: 1, 2, or 3? ")) - 1)
map[row_choice][column_choice] = "X"

print(f"{row1}\n{row2}\n{row3}")