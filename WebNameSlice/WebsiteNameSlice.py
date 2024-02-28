import re


def main():
    website1 = "https://www.google.com"
    website2 = "https://www.w3schools.com/js/default.asp"
    website3 = "https://orteil.dashnet.org/cookieclicker/"
    website4 = "https://github.com/kirby-b"
    # Website names for slicing

    print("This program takes a sample website like this:")
    print(website1)
    print(website2)
    print(website3)
    print(website4)
    print("And turns them into this")
    print(extract_name(website1))
    print(extract_name(website2))
    print(extract_name(website3))
    print(extract_name(website4))


def extract_name(website):
    temp = re.search(".+://", website).span()
    start = temp[-1]
    # Gets the start of the website name
    temp = re.search("\..+(/{1})|\..+", website).span()
    end = temp[-1]
    # Gets the end of the website name
    s = slice(start, end)
    # Gets the name by slicing from start to end
    website = website[s]
    regex_is_dumb = re.split("/", website)
    # I had to do this because I couldn't figure out how to get the regex to stop at the first "/" and not the last
    website = regex_is_dumb[0]
    return website


if __name__ == "__main__":
    main()
