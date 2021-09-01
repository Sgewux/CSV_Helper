import os
import csv
import sys


def is_correct_type(item, expected_type):
    """Function for check if a given item has the excpected type.
       returns True if the expected type matches the item, False if not

    Parameters:
        -item: the piece of data we are going to check.
        -expected_type: the expected data type for item.
    """
    if item != None:
        if expected_type in {int, float, (int, float)}:
            try:
                if (float(item)*10%10) == 0: 
                    
                    if expected_type in {int, (int, float)}:
                        return True
                    elif expected_type == float:
                        return False
                
                elif expected_type in {float, (int, float)}:
                    return True

            except ValueError: #This means that the value was not an integer or float
                return False

        elif expected_type == bool and item.strip().upper() in {'TRUE', 'FALSE'}:
            return True

        elif expected_type == str and item.strip().upper() not in {'TRUE', 'FALSE'}:
            try:
                float(item)
                return False
            
            except ValueError: #This means that we could not convert the item to float, wich means is not a numeric value
                return True
    else:
        return False
                

def find_type_errors(col_vs_type, reader_obj, file_path):
    """Function for find value errors in a given csv file

    Parameters:
        -col_vs_type: tuple with the name-type pairs.
        -reader_obj: csv reader object converted into tuple.
        -file_path: path of the given file.
    """

    for row in reader_obj:
        for col, type_ in col_vs_type:
            #try:
            if not is_correct_type(row[col], type_):
            
                print('no')
            #except Exception as e:
                #print(e)


def main(file_paths):
    """Main program function
       given a list of fle paths ask the user the value type for each column in each .csv file to look for errors
       by calling find_type_errors function with its requiered parameters

    Parameters:
        -file_paths: List of .csv file paths
    """

    errors = []
    for p in file_paths:
        row_types = []
        with open(p, 'r') as f:
            dict_reader = tuple(csv.DictReader(f))
            column_names = dict_reader[0].keys()
        
            for column in column_names:
                column_value_type = input(f'Which is the value type for {column} in {os.path.basename(p)}? >> ').upper()

                if column_value_type == 'S':
                    row_types.append(str)

                elif column_value_type == 'I':
                    row_types.append(int)

                elif column_value_type == 'F':
                    row_types.append(float)

                elif column_value_type == 'N':
                    row_types.append((int, float))

                elif column_value_type == 'B':
                    row_types.append(bool)

            name_type_pairs = tuple(zip(column_names, row_types))
            find_type_errors(name_type_pairs, dict_reader, p)



if __name__ == '__main__':
    path = sys.argv[1]
    
    if not os.path.exists(path):
        raise Exception('Unexistent file or dir')
    
    elif os.path.isdir(path):
        list_of_file_paths = []
        for p in os.listdir(path):
            if os.path.basename(p).endswith('.csv'):
                list_of_file_paths.append(os.path.join(path, p))

        main(list_of_file_paths)
    
    else:
        main((path,))
