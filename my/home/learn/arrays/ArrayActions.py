def delete_element_from_array(array, element):
    array.remove(element)


class ArrayActions:
    @staticmethod
    def filter_array(array):
        for element in array:
            if not isinstance(element, list):
                if element > 10:
                    delete_element_from_array(array, element)
            else:
                ArrayActions.filter_array(element)
        return array
