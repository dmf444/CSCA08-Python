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

if(__name__ == "__main__"):
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
