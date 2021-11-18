
from TK_1 import input_data_from_console
from TK_2 import get_min_max_from_list
from TK_3 import get_divided_list
from TK_4 import get_multiplied_list
from TK_5 import get_squared_list

def main():
    count_elements = int(input('Get number of elements:'))
    list_data = input_data_from_console(count_elements)
    print(get_min_max_from_list(list_data))
    print(get_divided_list(list_data))
    print(get_multiplied_list(list_data))
    print(get_squared_list(list_data))
    return 0
