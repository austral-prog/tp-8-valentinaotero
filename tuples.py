def get_coordinate(tuple):
    coordinate = tuple [-1]
    return str (coordinate)

def convert_coordinate(coordinate):
    numero= coordinate [0]
    letra= coordinate [1]
    return (numero,letra)

def create_record(azara_record, rui_record):
    
    coordinate_rui= rui_record[1]
    coordinate_azara= azara_record [1]
    numero=coordinate_azara [0]
    letra=coordinate_azara[1]
    variable= (numero,letra)
    if coordinate_rui==variable:
        return azara_record + rui_record
    else:
        return "not a match"
