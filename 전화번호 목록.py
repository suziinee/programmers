def solution(phone_book) :

    phone_book.sort(key = lambda x : len(x))
    phone_book.sort()

    for i in range(len(phone_book) - 1) :
        if phone_book[i + 1].find(phone_book[i]) == 0 :
            return False
    
    return True
    
    

    

    


    

