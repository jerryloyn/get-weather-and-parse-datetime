from datetime import datetime


def main(date_str):
    date_patterns = ["%b %d, %Y",
                     "%Y-%m-%d",
                     "%d %B %Y",
                     "%b %d, %Y, %I:%M%p",
                     "%Y-%m-%d %H:%M"
                     ]

    for pattern in date_patterns:
        try:
            return datetime.strftime(datetime.strptime(
                date_str, pattern).date(), "%Y-%m-%dT%H:%M:%SZ")
        except:
            pass

    print(f"Unable to parse {date_str}")


if __name__ == "__main__":

    date_strings = ["Sep 18, 2021",
                    "2021-09-18",
                    "18 September 2021",
                    "Sep 18, 2021, 12:00pm",
                    "2021-09-18 13:00"]

    [print(main(d)) for d in date_strings]
