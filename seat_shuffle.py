import random


def main():
    with open("members.txt", mode="r")as f:
        members = f.read().split("\n")
    random.shuffle(members)

    table1 = ' '.join(members[0:6])
    table2 = ' '.join(members[6:11])
    table3 = ' '.join(members[11:16])

    print(f"Table1: {table1}")
    print(f"Table2: {table2}")
    print(f"Table3: {table3}")


if __name__ == '__main__':
    main()
