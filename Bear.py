#Bear

class Bear:
    numOfbear = 0

    bear_sound = "Groar"

    list_of_bear_names = []

    #File
    file_path = r'C:/zooPopulation.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()

        line_num = 1
        for line in lines:
            if line_num == 3:
                list_of_bear_names.extend(line.strip().split(', '))
                break
            else:
                line_num += 1

    #definitions
    def __init__(self, name="a_name", animal_id="an_id", birth_date="2099-01-01", color="a_color", sex="a_sex",
                 weight="a_weight", originating_zoo="a_zoo", date_arrival="2099-01-01"):

        Bear.numOfbear += 1

        #what will pop up
        super().__init__("hyena", name, animal_id, birth_date, color, sex, weight, originating_zoo, date_arrival)

    def make_sound(self):
        return self.bear_sound

    def get_hyena_name(self):
        return self.list_of_bear_names.pop(0)

