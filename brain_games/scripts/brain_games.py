from ..cli import ask_name, greet_user


def main():
    print('Welcome to the Brain Games!')
    print()
    name = ask_name()
    greet_user(name)


if __name__ == "__main__":
    main()
