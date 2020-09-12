def no_dups(s):
    cache = []
    split_words = s.split(" ")
    
    string_seperator = " "
   
    cache.append(split_words[0])
    
    
    for word in range(1,len(split_words)):
        if split_words[word] not in cache:
            cache.append(split_words[word])
        
    return string_seperator.join(cache)

    
    

                
                



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))