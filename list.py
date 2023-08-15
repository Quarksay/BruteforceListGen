def generate_list(prefix, start, end):
    number_list = []
    for num in range(start, end + 1):
        formatted_num = f"{num:05d}"
        entry = f"{prefix}{formatted_num}"
        number_list.append(entry)
    return number_list

prefix = input("Enter the desired text: ")
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

result = generate_list(prefix, start_num, end_num)

with open("number_list.txt", "w") as file:
    for entry in result:
        file.write(entry + '\n')

print("List generated and saved to 'number_list.txt'.")
