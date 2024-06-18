def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    characters = character_count(text)
    print(f"---Begin Report of {book_path}---")
    print(f"{len(words)} words found in the document")
    print("")
    for s in characters:
        if s[0].isalpha():
            print(f"The '{s[0]}' character was found {s[1]} times")


        
def get_book_text(path):
    with open(path) as f:
        return f.read()
def character_count(text):
    all_lower = text.lower()
    count = {}
    for char in all_lower:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True), )
    report = list(sorted_count.items())
    return report
    
main()