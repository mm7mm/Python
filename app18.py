# print("""Welcome to place the rabbit
#     ['🥕', '🥕', '🥕']
#     ['🥕', '🥕', '🥕']
#     ['🥕', '🥕', '🥕']
#     """)


# line1=['🥕', '🥕', '🥕']
# line2=['🥕', '🥕', '🥕']
# line3=['🥕', '🥕', '🥕']

# print("Where should the rabbit go? 🐇")
# rapit="🐇"
# choose=int(input("Please choose a row and a column: "))
# if choose==11:
#     line1[0]=rapit
#     print(f"{line1}\n{line2}\n{line3}")
# elif choose==12:
#     line1[1]=rapit
#     print(f"{line1}\n{line2}\n{line3}")
# elif choose==13:
#     line1[2]=rapit
#     print(f"{line1}\n{line2}\n{line3}")
# elif choose==21:
#     line2[0]=rapit
#     print(f"{line1}\n{line2}\n{line3}")
# elif choose==22:
#     line2[1]=rapit
#     print(f"{line1}\n{line2}\n{line3}")
# elif choose==23:
#     line2[2]=rapit
#     print(f"{line1}\n{line2}\n{line3}")
# elif choose==31:
#     line3[0]=rapit
#     print(f"{line1}\n{line2}\n{line3}")
# elif choose==32:
#     line3[1]=rapit
#     print(f"{line1}\n{line2}\n{line3}")
# elif choose==33:
#     line3[2]=rapit
#     print(f"{line1}\n{line2}\n{line3}")
# else:
#     print("Sorey Tray agin")
#==========================================================================
#طريقة اخري
print("Welcome to place the rabbit")
field=[['🥕', '🥕', '🥕'],['🥕', '🥕', '🥕'],['🥕', '🥕', '🥕']]
print(f"{field[0]} \n {field[1]} \n {field[2]}")
print("Where should the rabbit go? 🐇")
position=(input("Please choose a row and a column: "))
row=int(position[0])
column=int(position[1])
field[row-1][column-1]="🐇"
print("\n Success....\n")
print(f"{field[0]} \n {field[1]} \n {field[2]}")
