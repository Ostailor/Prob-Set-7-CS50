import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        matches = re.search(r"([0-9:]+) ([AMP]+) to ([0-9:]+) ([AMP]+)", s)
        m_one = matches.group(1)
        m2 = matches.group(2)
        if m_one.isnumeric():
            m1 = int(m_one)
            if 0 > m1 or m1 > 12:
                raise ValueError
            elif m1 == 12:
                if m2 == 'PM':
                    pass
                elif m2 == 'AM':
                    m1 = 0
            elif m2 == 'PM':
                m1 = m1 + 12
        else:
            hr1, min1 = m_one.split(':')
            if int(min1) < 0 or int(min1) > 59:
                raise ValueError
            if hr1.isnumeric():
                hr1 = int(hr1)
                if 0 > hr1 or hr1 > 12:
                    raise ValueError
                elif hr1 == 12:
                    if m2 == 'PM':
                        pass
                    elif m2 == 'AM':
                        hr1 = 0
                elif m2 == 'PM':
                    hr1 = hr1 + 12
        m_three = matches.group(3)
        m4 = matches.group(4)
        if m_three.isnumeric():
            m3 = int(m_three)
            if 0 > m3 or m3 > 12:
                raise ValueError
            elif m3 == 12:
                if m4 == 'PM':
                    pass
                elif m4 == 'AM':
                    m3 = 0
            elif m4 == 'PM':
                m3 = m3 + 12
        else:
            hr2, min2 = m_three.split(':')
            if int(min2) < 0 or int(min2) > 59:
                raise ValueError
            if hr2.isnumeric():
                hr2 = int(hr2)
                if 0 > hr2 or hr2 > 12:
                    raise ValueError
                elif hr2 == 12:
                    if m4 == 'PM':
                        pass
                    elif m4 == 'AM':
                        hr2 = 0
                elif m4 == 'PM':
                    hr2 = hr2 + 12
    except AttributeError:
        raise ValueError
    else:
        if m_one.isnumeric() and m_three.isnumeric():
            return f"{m1:02}:00 to {m3:02}:00"
        elif m_one.isnumeric() and m_three.isalpha():
            return f"{m1:02}:00 to {hr2:02}:{min2}"
        elif m_one.isalpha() and m_three.isnumeric():
            return f"{hr1:02}:{min1} to {m3:02}:00"
        else:
            return f"{hr1:02}:{min1} to {hr2:02}:{min2}"


if __name__ == "__main__":
    main()
