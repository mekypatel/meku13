'''Module where GSTR9 bill parsing start'''
from advance import main as g9
from advance import generate_json as gj
# pylint: disable=W0703
# pylint: disable=C0301
def advance_main(download_location, request_id, input_file):
    '''Module where GSTR9 bill parsing start'''
    flag = False
    try:
        # file_list used for store text of file in list variable
        file_list = []

        print(f"{request_id} | {input_file} | START READING FILE AND STORE IN LIST FROM DOWNLOAD LOCATION : {download_location}")
        with open(download_location, "r", encoding="utf8") as file:
            for line in file:
                line = line.strip()
                if line:
                    file_list.append(line)
        print(f"{request_id} | {input_file} | END READING FILE AND STORE IN LIST FROM DOWNLOAD LOCATION : {download_location}")

        print(f"{request_id} | {input_file} | Start parsing Text in Json format for GSTR9 Bills")
        node_list, flag = g9.main(file_list)
        print(f"{request_id} | {input_file} | End parsing Text in Json format for GSTR9 Bills")

        if flag:
            print(f"{request_id} | {input_file} | Start generating Json for GSTR9")
            gj.generate_json(
                download_location,
                node_list
            )
            print(f"{request_id} | {input_file} | End generating Json for GSTR9")

    except Exception as error:
        print(f"{request_id} | {input_file} | ERROR AT GSTR9 PARSER : {str(error)}")
        flag = False
    return flag
