class SuffixArrays(object):

    def __init__(self, string):
        self.array = self.str_split(string)
        self.array_s = sorted(self.str_split(string))

    def __repr__(self):
        return f"{self.array[0]}"

    def str_split(self, string):
        split_array = []
        for index in range(0, len(string)):
            split_array.append((string[index:], index))
        return split_array

    def _binary_search(self, array, string, rule='all'):
        length = len(array)
        mid_index = length // 2
        mid_item = array[mid_index]
        mid_string = mid_item[0]
        
        if length == 1:
            if array[0][0].startswith(string):
                return array[0]
            else:
                return None

        if not(mid_string.startswith(string)) and string < mid_string:
            return self._binary_search(array[:mid_index], string, rule)
        elif string > mid_string:

            if mid_index + 1 >= length:
                return None
            else:
                return self._binary_search(array[mid_index+1:], string, rule)
        
        if rule == 'short':

            if string == mid_string:
                return mid_item
            else:
                shorter = self._binary_search(array[:mid_index], string, rule)
                if shorter and (len(shorter[0]) < len(mid_item[0])):
                    return shorter
                else:
                    return mid_item

        elif rule == 'long':
            longer = self._binary_search(array[mid_index:], string, rule)

            if longer and (len(longer[0]) > len(mid_item[0])):
                return longer
            else:
                return mid_item

        else:
            assert False, 'Should not happen.'

    def find_shortest(self, string):
        return self._binary_search(self.array_s, string, 'short')[0]

    def find_longest(self, string):
        return self._binary_search(self.array_s, string, 'long')[0]

    def find_all(self, string):
        start = self._binary_search(self.array_s, string, 'short')
        end = self._binary_search(self.array_s, string, 'long')

        if not start:
            return None
        elif start == end:
            return start
        else:
            s_num = e_num = None
            for i, text in enumerate(self.array_s):
                if start[0] == text[0]:
                    s_num = i
                if s_num and end[0] == text[0]:
                    e_num = i
                    break
            return self.array_s[s_num : e_num + 1]