import unittest

def unique_count(numbers: list):
    return len(list(set(numbers)))


class Person:
    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

   
def people_sort(persons: list, attribute: str):
    sorted_persons = sorted(persons, key=lambda x: getattr(x, attribute))
        # print([getattr(person, attribute) for person in sorted_persons])
    return sorted_persons
        
class tests(unittest.TestCase):

    def test_unique_count(self):
        self.assertEqual(unique_count([2, 3, 3, 2]), 2)
        self.assertEqual(unique_count([1, 1, 1, 2]), 2)
        self.assertEqual(unique_count([1, 2, 3]), 3)
    
    def test_people_sort(self):
        self.assertEqual(people_sort([p1, p2, p3], "firstname"), [p3, p2, p1])
        self.assertEqual(people_sort([p1, p2, p3], "lastname"), [p1, p2, p3])
        self.assertEqual(people_sort([p1, p2, p3], "age"), [p2, p3, p1])


        #self.assertEqual(people_sort([["Michael", "Farrel", 42], ["John", "Jacksson", 25], ["Anna", "Watson", 33]], "firstname"), ["Anna", "John", "Michael"])
        #self.assertEqual(people_sort([["Michael", "Farrel", 42], ["John", "Jacksson", 25], ["Anna", "Watson", 33]], "lastname"), ["Farrel", "Jacksson", "Watson"])
        #self.assertEqual(people_sort([["Michael", "Farrel", 42], ["John", "Jacksson", 25], ["Anna", "Watson", 33]], "age"), [25, 33, 42])


p1 = Person("Michael", "Farrel", 42)
p2 = Person("John", "Jacksson", 25)
p3 = Person("Anna", "Watson", 33)


if __name__ == '__main__':
    unittest.main()