# Step 1: Read the input file
with open("/Users/fangliu/Documents/Joseph/project-1/in.txt", 'r') as myfile:
    mylines = myfile.readlines()

# Step 2: read name
names_raw = mylines[:5]
# step 2 read age
ages_raw = mylines[5:10]
# step 2 read Calculation 
calculations_raw = mylines[10:]

# Step 3: clear names
names = []
for name in names_raw:
    name = name.replace("\\t", "")
    name = name.replace("<main>", "")
    name = name.replace("inputnamehere:", "")
    name = name.strip()
    # add new name
    names.append(name)

# Step 4: Convert ages to integers

ages = []
for age in ages_raw:
    age = age.strip()        # 去除空白字符
    age = float(age)          # 转换为浮点数
    age = int(age)            # 转换为整数
    ages.append(age)

# Step 5: Convert to scientific notation 
calculations = []
for line in calculations_raw:
    formatted_line = []
    for value in line.split():
        formatted_value = "{:.2e}".format(float(value))
        formatted_line.append(formatted_value)    
    calculations.append(formatted_line)

# Step 6: write in output format
output_lines = []
for i in range(5):
    # Name line
    output_lines.append(f"{names[i]}\n")
    # Age line
    output_lines.append(f"{ages[i]} years old\n")
    # Calculations line
    output_lines.append(" ".join(calculations[i]) + "\n")

with open("out.txt", 'w') as out_file:
    out_file.writelines(output_lines)


