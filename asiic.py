def string_to_ascii(input_string):
    ascii_values = [ord(char) for char in input_string]
    for x in ascii_values:
        x=int(x)+3 
        i=0
        add_value=[x]
        i=i+1
    return add_value

input_string = input("Enter the text :")
ascii_values = string_to_ascii(input_string)
print(f"ASCII values: {ascii_values}")
