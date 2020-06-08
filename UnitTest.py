import unittest
import ToJson
import Merge_sort
import Decorator
import Vector
import random
import json


class UnitTest(unittest.TestCase):

    def test_converter(self):
        dict = {'Mama': 'Genya', 1: [1, 2, 3, 4]}
        dict2 = {'GJ': 'GL'}
        dict3 = {1: [1.2, 2.2, 3.3, 4.4]}
        this_list = ["apple", "banana", "cherry"]
        dict4 = {'list': this_list}
        this_list2 = [False, True, None]
        dict5 = {'Dict': this_list2}
        in_dict = {'Name': 'Geeks'}
        dict6 = {'Dict': in_dict}
        self.assertEqual(ToJson.dict_transform(dict), json.dumps(dict))
        self.assertEqual(ToJson.dict_transform(dict2), json.dumps(dict2))
        self.assertEqual(ToJson.dict_transform(dict5), json.dumps(dict5))
        self.assertEqual(ToJson.dict_transform(dict6), json.dumps(dict6))
        self.assertEqual(ToJson.to_json(dict3), json.dumps(dict3))
        self.assertEqual(ToJson.to_json(dict4), json.dumps(dict4))

    def test_merge(self):
        with open('numbers.txt', 'w') as f:
            f.writelines('{}\n'.format(random.randint(-100000, 100000)) for _ in range(100005))
        Merge_sort.external_sort()
        check = True
        with open('sorted_numbers.txt', 'r') as file:
            for line in file:
                temp = int(line)
                if int(line) >= temp:
                    temp = int(line)
                else:
                    check = False
                    break
        self.assertEqual(check, True)

    def test_decorator(self):
        self.assertEqual(Decorator.decorator(3), 8)
        self.assertEqual(Decorator.decorator(8), 13)
        self.assertEqual(Decorator.decorator(3), 8)
        self.assertEqual(Decorator.decorator(0), 5)

    def test_vector(self):
        test_vector1 = Vector.Vector([7, 6, 5])
        test_vector2 = Vector.Vector([-6, -5, -4])
        test_vector3 = Vector.Vector([6, 5, 4])
        test_vector4 = Vector.Vector([1, 1, 1])
        test_vector5 = Vector.Vector([-12, -10, -8])
        test_vector6 = Vector.Vector([5, 4, 3])
        test_vector7 = Vector.Vector([-36, -30, -24])
        test_vector8 = Vector.Vector([0])
        self.assertTrue(test_vector1 + test_vector2 == test_vector4)
        self.assertTrue(test_vector2 - test_vector3 == test_vector5)
        self.assertTrue(test_vector3 - test_vector4 == test_vector6)
        self.assertIsNone(test_vector1 + test_vector8, None)
        self.assertTrue(str(test_vector3), "5,4,3")
        self.assertTrue(test_vector4 * test_vector6 == 12)
        self.assertTrue(test_vector5.__const_mul__(3) == test_vector7)
        self.assertTrue(len(test_vector3), 3)
        self.assertTrue(test_vector7[1], -30)
