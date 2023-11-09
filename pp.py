# Given string
input_string = '<S>\n"menu_items": ["Dim Island"]\n"quantities": [1]\n"extra_info": ["-"]'

# Remove '<S>' and newlines from the input string
cleaned_string = input_string.replace('{\n', '')
cleaned_string = input_string.replace('\n}', '')

cleaned_string = cleaned_string.replace('\n', ',')

# Evaluate the cleaned string using eval() to convert it into a dictionary
result_dict = eval('{'+cleaned_string+'}')

# Print the resulting dictionary
print(result_dict)
