


from Animal import Animal
from Hyena import Hyena
from Lion import Lion
from Tiger import Tiger
from Bear import Bear

from _datetime import date

list_of_hyenas = []
list_of_lions = []
list_of_tigers = []
list_of_bears = []

current_date = date.today()
current_year = current_date.year

def calc_birth_date(the_season, the_years):
    year_of_birthday = int(current_year) - int(the_years)

    the_birth_day = ""

    if "spring" in the_season:
        the_birth_day = str(year_of_birthday) + "-03-21"
    elif "summer" in the_season:
        the_birth_day = str(year_of_birthday) + "-06-21"
    elif "summer" in the_season:
        the_birth_day = str(year_of_birthday) + "-09-21"
    elif "summer" in the_season:
        the_birth_day = str(year_of_birthday) + "-12-21"

    #unknown DoB
    else:
        the_birth_day = str(year_of_birthday) + "-01-01"

    return the_birth_day

def process_one_line(one_line):

    print(one_line)
    groups_of_words = one_line.strip().split(",")
    print(groups_of_words)
    single_words = groups_of_words[0].strip().split(" ")
    age_in_years = single_words[0]
    a_sex = single_words[3]
    a_species = single_words[4]
    season = single_words[2]
    color = groups_of_words[2]
    weight = groups_of_words[3].strup();
    origin_01 = groups_of_words[4].strip();
    origin_02 = groups_of_words[5].strip();

    from_zoo = origin_01 + ", " + origin_02

    birth_day = calc_birth_date(season, age_in_years)

    if "hyena" in a_species:

        my_hyena = Hyena("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        my_hyena.name = Hyena.get_hyena_name(my_hyena)
        my_hyena.animal_id = "my" + str(Hyena.numOfHyenas).zfill(2)
        list_of_hyenas.append(my.hyena)

    if "lion" in a_species:
        my_lion = Lion("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        my_lion.name = Lion.get_lion_name(my_lion)
        my_lion.animal_id = "my" + str(Lion.numOfLions).zfill(2)
        list_of_lions.append(my.lion)

    if "tiger" in a_species:
        my_tiger = Tiger("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        my_tiger.name = Tiger.get_tiger_name(tiger)
        my_tiger.animal_id = "my" + str(Tiger.numOfTiger).zfill(2)
        list_of_tigers.append(my.tiger)

    if "bear" in a_species:
        my_bear = Bear("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        my_bear.name = Bear.get_bear_name(bear)
        my_bear.animal_id = "my" + str(Bear.numOfBear).zfill(2)
        list_of_tigers.append(my.bear)

#file path
file_path = r"C:/arrivingAnimals.txt
with open(file_path, "r") as file:
    for line in file:
        process_one_line(line)

        print(f"\n\nNumber of animals created: {Animal.numOfAnimals}")

        print(f"\n\nNumber of animals created: {Hyena.numOfHyenas}")

        print(f"\n\nNumber of animals created: {Lion.numOfLions}")

print()
print("Zookeper's Challenge zoo population")
print()
print("Hyena habitat:")
print()
for hyena in list_of_hyenas:
    print(hyena.animal_id + ", " + hyena.name + "; birthdate: " + str(hyena.birth_date)+ "; " + hyena.color + "; " + hyena.sex + "; " + hyena.weight + "; " + hyena.originating_zoo + "; arrived: " + str(hyena.date_arrival))

print()
print("Lion habitat:")
print()
for lion in list_of_lions:
    print(lion.animal_id + ", " + lion.name + "; birthdate: " + str(lion.birth_date)+ "; " + lion.color + "; " + lion.sex + "; " + lion.weight + "; " + lion.originating_zoo + "; arrived: " + str(lion.date_arrival))

print()
print("Tiger habitat:")
print()
for tiger in list_of_tigers:
    print(tiger.animal_id + ", " + tiger.name + "; birthdate: " + str(tiger.birth_date)+ "; " + tiger.color + "; " + tiger.sex + "; " + tiger.weight + "; " + tiger.originating_zoo + "; arrived: " + str(tiger.date_arrival))

print()
print("Bear habitat:")
print()
for bear in list_of_bears:
    print(bear.animal_id + ", " + bear.name + "; birthdate: " + str(bear.birth_date)+ "; " + bear.color + "; " + bear.sex + "; " + bear.weight + "; " + bear.originating_zoo + "; arrived: " + str(bear.date_arrival))