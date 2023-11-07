def interpret(string):
    string = string.replace('<S>\n', '')

    # Create an empty dictionary to store the variables
    data_dict = {}

    # Execute the input string as code in a controlled environment
    exec(string, {}, data_dict)

    # Extract the variables from the local namespace
    menu_items = data_dict.get('menu_items', [])
    quantities = data_dict.get('quantities', [])
    extra_info = data_dict.get('extra_info', [])

    # Create the final dictionary
    result = {
        "menu_items": menu_items,
        "quantities": quantities,
        "extra_info": extra_info
    }

    return result
