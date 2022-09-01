import validators


def main():
    print(validate(input('Email Address: ')))


def validate(e):
    if validators.email(e):
        return 'Valid'
    else:
        return 'Invalid'


if __name__ == "__main__":
    main()