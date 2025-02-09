def main():
    with open("/home/thelann/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    
    report(count_characters(file_contents), count_words(file_contents))

def count_characters(file_contents):
    characters = {}

    for letter in file_contents:
        if letter.lower() in characters:
            characters[letter.lower()] = characters[letter.lower()] + 1
        else:
            characters[letter.lower()] = 1
   
    return(characters)

def count_words(file_contents):
    return len(file_contents.split())

def report(characters, words):
    print("--- Begin report of books/frankenstein.txt --")
    print(f"{words} words found in the document")
    print("")
    for character in characters:
        if character.isalpha():
            print(f"The '{character}' character was found {characters[character]} times")
    print("--- End report ---")

main()