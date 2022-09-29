from read_contact import read_contact
from save_contacts import save_to_csv
from export_to_xml import export_to_xml
from export_to_json import export_to_json


def start():
    print('Select the required operation:', '1 - enter data in the format "Last name, First name, phone number, description"',
          '2 - output data in the required format', '3 - export data to a file', '4 - Exit',
          sep='\n')

    operation_select = int(input())
    if operation_select == 1:
        soname = input('Enter last name: ')
        name = input('Enter first name: ')
        phone_number = input('Enter phone number: ')
        description = input('Enter description: ')
        new_list = [soname, name, phone_number, description]
        save_to_csv(new_list)
        start()
        return new_list
    elif operation_select == 2:
        print('Select the data display format:', '1 - line by line', '2 - in one line', sep='\n')
        num = int(input())
        if num == 1 or num == 2:
            read_contact(num)
        start()
    elif operation_select == 3:
        print('Select the data export format:', '1 - xml', '2 - json', sep='\n')
        num = int(input())
        if num == 1:
            export_to_xml()
            print('The data has been successfully exported in xml!\n' + '-' * 20)
        elif num == 2:
            export_to_json()
            print('The data has been successfully exported in json!\n' + '-' * 20)
        else:
            print('Incorrect input! Repeat!\n' + '-' * 20)
            start()
        start()
    elif operation_select == 4:
        print('See you soon!\n' + '-' * 20)
        exit(0)
    else:
        print('Incorrect input! Repeat!\n' + '-' * 20)
        start()

