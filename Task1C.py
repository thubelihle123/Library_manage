books = []
members = []

bookDetail = ({
 "book_id": int(input("enter a book id: ")),
 "title": input("enter a book title: "),
 "author": input("enter an author: "),
 "status": input("book status: ")
 })

books.append(bookDetail)
    
memberDetail = ({
        "member_id": int(input("enter a member id: ")),
        "name": input("enter a name: "),
        "borrowed_books": int(input("enter number of books borrowed: "))
    })

members.append(memberDetail)

print("Books ", books)
print("Members", members)