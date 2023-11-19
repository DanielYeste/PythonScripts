import sys

def read_and_write_file(file_name):
    try:
        with open(file_name, 'r') as file_input, open('combinations.txt', 'w') as file_output:
            lines = file_input.readlines()
            for line in lines:
                clean_line = line.strip()
                usernames_list = create_usernames(clean_line)
                for username in usernames_list:
                    file_output.write(username + '\n')
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

def  create_usernames(name_input):
    full_name = name_input.lower()
    name, surname = full_name.split(" ", 1)
    return name + "." + surname, name[0] + surname, name+surname, name + "_" + surname, name[0] + "." + surname, name[0:3] + surname, name[0:3] + surname [0:3]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py file_name.txt")
    else:
        file_name = sys.argv[1]
        read_and_write_file(file_name)
