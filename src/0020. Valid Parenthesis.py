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

