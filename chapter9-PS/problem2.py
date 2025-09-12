# WAP in python write the tables from 2 to 20 in different text files
def generate_table(num):
    table = ""
    for i in range(1, 11):
        table += f"{num} x {i} = {num*i}\n"

    with open(f"tables/table_of_{num}.txt", "w") as tableFile:
        tableFile.write(f"Table of {num}:\n")
        tableFile.write(table)

for i in range(2, 21):
    generate_table(i)