import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        matches = re.search(r"src=([a-z0-9A-Z/:.\"]+)", s)
        m1 = matches.group(1)
        end = re.search(r"http(?:s)?://(?:www\.)?youtube.com/embed/([a-zA-z0-9]+)", m1)
        return 'https://youtu.be/' + end.group(1)
    except AttributeError:
        return 'None'


if __name__ == "__main__":
    main()
