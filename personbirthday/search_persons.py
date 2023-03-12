import datetime

from personbirthday.person import Person

def get_age_or_younger(list, ageInYears):
    sublist = [person for person in list if person.get_age() <= ageInYears]
    return sublist

if __name__ == "__main__":
    list = [
        Person(123, "Mary Kwan",            datetime.date(2002, 12, 11,)),
        Person(456, "Tomas White",          datetime.date(1968, 3, 12,)),
        Person(789, "Sonny Black",          datetime.date(2005, 4, 20,)),
        Person(135, "Riley Nicholson",      datetime.date(2000, 1, 15,)),
        Person(791, "Hudson Pearson",       datetime.date(1987, 5, 15,)),
        Person(246, "Samuel Miller",        datetime.date(2010, 9, 30,)),
        Person(802, "Arlo Rees",            datetime.date(2007, 2, 28,)),
        Person(150, "Sami Ball",            datetime.date(1972, 6, 1,)),
        Person(111, "Calvin Patel",         datetime.date(2021, 5, 10,)),
        Person(351, "Adam Murphy",          datetime.date(1998, 3, 12,)),
        Person(895, "Laurence Hunt",        datetime.date(1988, 5, 21,)),
        Person(125, "Tomas White",          datetime.date(1979, 9, 19,)),
        Person(478, "Sonny Black",          datetime.date(1999, 7, 11,)),
        Person(451, "Riley Nicholson",      datetime.date(1997, 9, 12,)),
        Person(124, "Hudson Pearson",       datetime.date(1994, 4, 14,)),
        Person(158, "Samuel Miller",        datetime.date(1992, 6, 16,)),
        Person(785, "Arlo Rees",            datetime.date(1997, 11, 18,)),
        Person(458, "Sami Ball",            datetime.date(2003, 12, 20,)),
        Person(852, "Calvin Patel",         datetime.date(2001, 11, 22,)),
        Person(127, "Adam Murphy",          datetime.date(2000, 10, 30,)),
        Person(851, "John Jonzz",           datetime.date(1971, 3, 8,)),
        Person(125, "Laurence Hunt",        datetime.date(1998, 3, 10,)),
    ]

    sublist = get_age_or_younger(list, 21)
    for person in sublist:
        print(person.__str__())
