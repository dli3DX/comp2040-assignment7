file_path = r'C:\Users\l5647\OneDrive\桌面\2040\weather.csv'

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()[1:] 
    temperatures = [float(line.split(',')[0]) for line in lines]  

average_temp = sum(temperatures) / len(temperatures)

print("Original Data:")
for line in lines:
    print(line.strip())  

print(f"The average temperature is: {average_temp:.2f}")
