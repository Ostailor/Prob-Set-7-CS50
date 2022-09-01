import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    m = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)
    try:
        m1 = int(m.group(1))
        m2 = int(m.group(2))
        m3 = int(m.group(3))
        m4 = int(m.group(4))
    except (ValueError, AttributeError):
        return False
    else:
        if 0 <= m1 <= 255 and 0 <= m2 <= 255 and 0 <= m3 <= 255 and 0 <= m4 <= 255:
            return True
        else:
            return False


if __name__ == "__main__":
    main()
