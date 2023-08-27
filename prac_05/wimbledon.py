"""
Wimbledon
Estimate: 1 hour minutes
Actual: 1hour 30mins
"""

FILENAME = "wimbledon.csv"
COUNT_COUNTRY = 1
COUNT_CHAMPION = 2

def main():
    """Read file and print the champions and countries."""
    data = get_datas(FILENAME)
    champion_to_win, countries = process_datas(data)
    display_results(champion_to_win, countries)


def get_datas(filename):
    """Get datas from file and put it in a list of lists."""
    datas = []

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            split_data = line.strip().split(",")
            datas.append(split_data)
    return datas


def process_datas(datas):
    champion_to_win = {}
    countries = set()

    for data in datas:
        countries.add(data[COUNT_COUNTRY])
        try:
            champion_to_win[data[COUNT_CHAMPION]] += 1
        except KeyError:
            champion_to_win[data[COUNT_CHAMPION]] = 1
    return champion_to_win, countries


def display_results(champion_to_win, countries):
    """Display champions, points and countries."""
    print("Wimbledon Champions:")

    for name, count in champion_to_win.items():
        print(name, count)
    print()

    print(f"These {len(countries)} countries have won Wimbledon:")
    print(" ,".join(country for country in sorted(countries)))


main()
