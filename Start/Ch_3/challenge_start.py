# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for comprehensions

import string
import pprint


test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

length = len(test_str)
# print(length)
nums = len([x for x in test_str if x.isnumeric()])
# digits = len(nums)
# print(digits)
punctuation = len([x for x in test_str if x in string.punctuation])
# print(len(punctuation))
unique_letters = "".join({c for c in test_str if c.isalpha()})
# print(unique_letters)
# print the data
str_data = {
    'Length': length,
    'Digits': nums,
    'Punctuation': punctuation,
    'Unique Letters': unique_letters,
    'Unique Count': len(unique_letters)
}
pprint.pp(str_data)

values = ["1", 0, True, [1, 2, 3], "ABC", 4.0, {}, None]
result = [str(c) if bool(c) == True else c for c in values]
print(result)
