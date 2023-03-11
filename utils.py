import csv

def decompose_vin(vin):
    vin = vin.upper()
    if not is_valid_vin(vin):
        print('Invalid VIN number it must be exactly 17 charachters')
    else:
        list_vin = list(vin)
        wmi = c_list_to_str(list_vin[0:3])
        vds = {
            'model':vin[3],
            'type':vin[4],
            'details':c_list_to_str(list_vin[6:7])
        }
        safety = list_vin[7]
        check_digit = list_vin[8]
        model_year = list_vin[9]
        manufacturing_plant = list_vin[10]
        serial_number = c_list_to_str(list_vin[12:17]) 

        vin_data = {
            'wmi':wmi,
            'vds':vds,
            'restraint system' :safety,
            'check digit':check_digit,
            'model year':model_year,
            'manufacturing plant':manufacturing_plant,
            'serial number':serial_number
            }
        
        return vin_data
def r_sys(sys):
    restraint = ['C','D','E','F']
    for digit in restraint:
        if sys != digit:
            return 'F'
        else:
            return sys

def is_valid_vin(vin):
    vin = list(vin)
    if len(vin)!=17:
        return False
    elif contains_forbidden_char(vin):
        return False
    else:
        return True

def contains_forbidden_char(vin):
    for c in vin:
        if c == 'O' or c =='Q' or c == 'I':
            return True
        else:
            return False

def c_list_to_str(l):
    s=''
    for c in l:
        s=s+c
    return s

def read_csv(file_name):
    file_data =[]
    with open(file_name, 'r') as file:
        reader = csv.reader(file,delimiter=',')
        for item in reader:
            file_data.append(item)
        return file_data[1:]

