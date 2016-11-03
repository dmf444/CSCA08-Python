class Toy():
    '''A dog's toy'''

    def __init__(self, sound):
        self._sound = sound

    def squeeze(self):
        print(self._sound)


class Dog():
    '''A class to represent evil 4-legs that play with toys'''

    def __init__(self, breed, name):
        self._name = name
        self._breed = breed
        self.give_toy(None)

    def give_toy(self, new_toy):
        self._my_toy = new_toy

    def play(self):
        if(self._my_toy == None):
            print("Worf")
        else:
            self._my_toy.squeeze()


def dog_test():
    dog = Dog("DEATH", "I AM DEATH")
    dog.play()
    dog.give_toy(Toy("SICKLE"))
    dog.play()

dog_test()


class Building():
    '''Classto represent a building made of many rooms'''

    def __init__(self, address, num_rooms, room_size):
        self._my_address = address
        self._my_rooms = []
        for count in range(num_rooms):
            self._my_rooms.append(Room(room_size, 2, 1))

    def get_total_area(self):
        area = 0
        for next_room in self._my_rooms:
            area += next_room.get_area()
        return area


class Room():
    '''Class to define a room'''

    def __init__(self, area, num_doors, num_windows):
        self._my_area = area
        self._my_num_door = num_doors
        self._my_num_windows = num_windows

    def get_area(self):
        return self._my_area


def test_building():
    h_wing = Building("1295 Military Trail", 150, 100)
    print(h_wing._my_address)
    print(h_wing.get_total_area())

test_building()


class Person():
    '''More strings for reasons unknown'''
    ###############################
    #
    # ALL INTERNAL VARS SHOULD BE PRIVVY
    #
    ###############################
    def __init__(self, name, age, gender):
        # print("I'm in the init method")
        self.set_name(name)
        self.set_age(age)
        self.set_gender(gender)

    def __str__(self):
        return "My name is " + self.get_name() + "and I'm " + \
               str(self.get_age()) + "yrs old"

    def set_age(self, new_age):
        self._age = new_age

    def set_name(self, new_name):
        self._name = new_name

    def set_gender(self, new_gender):
        if(new_gender == "Male"):
            self._is_male = True
        else:
            self._is_male = False

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    def get_gender(self):
        if(self._is_male):
            r = "Male"
        else:
            r = "Female"
        return r

############################################


def test_person():
    person1 = Person("Alice Smith", 30, "Female")
    # person1.set_name("Alice")
    # person1.set_gender("Female")
    person2 = Person("Bob", 18, "Male")
    # person2.set_name("Bob")
    # person2.set_gender("Male")
    population = {person1, person2}
    for next_person in population:
        greeting = "Hello "
        if(next_person.get_gender() == "Female"):
            greeting += "Ms. "
        else:
            greeting += "Mr."
        print(greeting + next_person.get_name())

test_person()


class Student(Person):
    """a class that represents a student as a person - we're not"""

    def __init__(self, name, age, height, gender, gpa):
        super().__init__(name, age, gender)
        self.set_gpa(gpa)

    def set_gpa(self, new_gpa):
        self._gpa = new_gpa

    def get_gpa(self):
        return self._gpa

    def __str__(self):
        return "Yo! My GPA is: " + str(self.get_gpa())