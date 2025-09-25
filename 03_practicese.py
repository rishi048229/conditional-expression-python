p1 = "make lots of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comment")

if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("this is a SPAM")

else:
    print("this comment is not a spam")
    