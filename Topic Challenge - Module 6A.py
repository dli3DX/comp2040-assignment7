file_path = r'C:\Users\l5647\OneDrive\桌面\2040\colors.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

with open(file_path, 'w', encoding='utf-8') as file:
    for line in lines:
        if 'Aqua' in line:
            file.write('Azure #007fff\n')
        else:
            file.write(line)
