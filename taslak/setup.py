def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()

    print(new_string)


alternating("ecem aydogan")

def alternating_with_enumerate(string):
    new_string = ""
    for i ,letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating_with_enumerate("eren aydoğan")

students = ["ecem", "ayça", "begüm", "derin", "eren"]


def divine_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)

    print(groups)
    return groups

divine_students(students)


numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2


#{n: n**2 for n in numbers if n % 2 == 0}



import seaborn as sns
df = sns.load_dataset("car_crashes")
print(df.columns)


num_cols = [col for col in df.columns if df[col].dtype != "0"]

soz = {}
agg_list = ["mean","min","max","sum"]

for col in num_cols :
    soz[col] = agg_list

new_dict = {col : agg_list for col in num_cols}




