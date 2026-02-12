
def ft_count_harvest_recursive(day=1, last=None):
    if (last is None):
        last = int(input(
            "Days until harvest: "
        ))
    if (day <= last):
        print(
            f"Day {day}"
        )
        ft_count_harvest_recursive(day + 1, last)
    else:
        print(
            "Harvest time!"
        )
