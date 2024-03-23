"""Initialize two data structures to keep track of books and members both represented as lists. The system 
features two functions (You must create these functions): add_book and add_member. The add_book
function takes three parameters (book_id, title, author, status) and appends a new book dictionary to 
the books list. The add_member function, on the other hand, requires two parameters (member_id, 
name) and appends a new member dictionary to the members list. Each member dictionary includes an 
empty list for borrowed_books to track the IDs of books each member has borrowed.
Sequence hint: initialize two variables as lists, then create two functions as per the above requires. An 
example of the appending part of the question is as follows:
books.append({
 "book_id": book_id,
 "title": title,
 "author": author
 })
You must use the same procedure for all appends"""

books = []
members = []

def add_book (book_id, title, author, status):
    books.append({
 "book_id": book_id,
 "title": title,
 "author": author,
 "status": status
 })
    
def add_member (member_id, 
name, borrowed_books):
    members.append({
        "member_id": member_id,
        "name": name,
        "borrowed_books": borrowed_books
    })

add_book (23466786, "Masambiasane", "Thubelihle Dube", "available")
add_member (1, "Snenhlanhla", 1)

print("Books ", books)
print("Members", members)
    