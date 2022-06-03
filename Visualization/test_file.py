with open('FinalDataset.csv', 'r') as file:
    data = file.readlines()
    file.close()
c_data = [[x.strip() for x in line.replace('\n', '').split(',')] for line in data]
state, year, age, gender = [], [], [], []
print(c_data[0])
for line in c_data[1:]:
    state.append(line[0])
    year.append(line[1])
    age.append(line[2])
    gender.append(line[3])

print(f'\nstates : {list(set(state))}\nyear : {list(set(year))}\nage : {list(set(age))}\ngender : {list(set(gender))}\ncrime : {c_data[0][4:]}')

# <option value="volvo">Volvo</option>
# <option value="saab">Saab</option>
# <option value="mercedes">Mercedes</option>
# <option value="audi">Audi</option>

# dic = {'state' : list(set(state)),
#        'year' : list(set(year)),
#        'age' : list(set(age)),
#        'gender' : list(set(gender)),
#        'crime' : c_data[0][4:]}

# for i in dic.keys():
#     print(i)
#     for j in dic[i]:
#         print(f'<option value="{j}">{j}</option>')
#     print('\n\n')