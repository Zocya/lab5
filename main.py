import re


def main():
    with open('con228.bugs.799464655', 'r') as log:
        file = log.readlines()
    everything_found = []
    counter = 0
    first_pattern = r"\.edu.icons"
    for line in file:
        out = (re.findall(first_pattern, line))
        for i in out:
            if out != "":
                everything_found.append(out)
                counter += 1

    print(everything_found)
    print(counter)


if __name__ == '__main__':
    main()
