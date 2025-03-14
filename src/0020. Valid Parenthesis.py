class Solution:
    def isValid(self, s: str) -> bool:
        left_set = {'(', '{', '['}
        right_set = {')', '}', ']'}
        valid_set = {'()', '{}', '[]'}
        left_deque = deque()

        if s[0] in right_set:
            return False

        if len(s) % 2 == 1:
            return False

        for parenthesis in s:
            if parenthesis in left_set:
                left_deque.append(parenthesis)
            else:
                if len(left_deque) == 0:
                    return False
                corresponding_left = left_deque.pop()
                combined = ''.join([corresponding_left, parenthesis])
                if combined in valid_set:
                    continue
                else:
                    return False

        if len(left_deque) != 0:
            return False
        else:
            return True
        
from collections import deque

# Alternate Solution

# class Solution:
#     def isValid(self, s: str) -> bool:

#         if len(s) % 2 == 1:
#             return False

#         # Initialise a deques to iterate through the string and store the
#         # open  parenthses
#         open_parentheses = deque([])
#         deque_length = 0

#         valid_open = ['(', '{', '[']
#         valid_close = ['()', '{}', '[]']

#         for character in s:
#             if character in valid_open:
#                 open_parentheses.append(character)
#                 deque_length += 1
#             else:
#                 if deque_length == 0:
#                     return False
#                 else:
#                     if open_parentheses.pop() + character in valid_close:
#                         deque_length -= 1
#                         continue
#                     else:
#                         return False

#         return deque_length == 0

