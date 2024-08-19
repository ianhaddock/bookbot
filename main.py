# bookbot

def get_content(book_path):
    with open(book_path) as f:
        return f.read()

def word_count(content):
    return len(content.split())

def count_characters(content):
    char_count = {}
    case_content = content.lower()
    for c in case_content:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count


def sort_on(dict):
    return dict["count"]


def run_report(book_path, chars, words):
    clist = []

    for c in chars:
        if c.isalpha():
            clist.append({"name": c, "count": chars[c]})
    clist.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print("")

    for i in range(0, len(clist)):
        print(f"The {clist[i]['name']} was found {clist[i]['count']} times.")

    print("--- End Report ---")


if __name__ == '__main__':
    book_path = 'books/frankenstein.txt'

    content = get_content(book_path)
    words = word_count(content)
    chars = count_characters(content)
    run_report(book_path, chars, words)


