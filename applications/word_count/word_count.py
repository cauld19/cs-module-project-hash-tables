import re

def word_count(s):
    cache = {}
    
    remove_char = re.sub(r"[^\w']", ' ', s) ## remove all non alphanumeric chcaracters except '

    split_words = remove_char.split(" ") ## split at empty spaces
    for word in split_words: # iterate through words
        word = word.lower() #make lowercase
        if word == "":
            continue
        if word not in cache:
            cache[word] = 1
        else:  
            cache[word] += 1
    return cache
    



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))