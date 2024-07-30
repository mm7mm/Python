# Step1: Setup
book=[]
wishlist=[]

# Step 2:Adding Individual Books
name_book=input("Enter the name of a book you own :")
book.append(name_book)
name_book=input("Enter the name of another book you own (or press ' Enter' or skip):")
if name_book:
        book.append(name_book)
print(f"\nYour library:{book}")



# STep 3 : Managing the wishlist
name_book=input("Enter the name of a book you wish to have in the future : ")
wishlist.append(name_book)

name_book=input("Eter the name of another book you wish to have (or press 'Enter') to skip): ")
if name_book:
    wishlist.append(name_book)

print(f"Your wishlist: {wishlist}")


# Step 4:Merging wishlist into Library
name_book=input("Enter the name of a book your wishlist that you've acquired (or press 'Wnter' to skip) :")
if name_book in wishlist:
    book.append(name_book)
    wishlist.remove(name_book)

print(f"Updated Library :{book}")
print(f"Updated Wishlist:{wishlist}")


# Step 6:Donating books
wish_book=input("Enter the name of a book from your library you wish to donate (or press 'Wnter' to skip) ")
book.remove(wish_book)
if wish_book in book:
    book.remove(wish_book)
print(f"final after Donations: {book}")
