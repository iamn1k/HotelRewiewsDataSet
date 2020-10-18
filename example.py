with open('data.txt','r') as f:
    input_data = f.read().split('*******')
    x_train,y_train = [],[]
    for el in range(len(input_data)-1):
        input_data[el] = (input_data[el]).split('$')
        x_train.append(input_data[el][0])
        y_train.append(input_data[el][-1])
    f.close()

print(len(x_train)) # 168256
print(len(y_train)) # 168256
print(x_train[404])
'''
Otnoshenie na retsepshins pri zaselenii esche bolee menee, a pri vyselenii voobsche ne zahoteli
 razgovarivat', prosto skazali :"ostav'te kljuch", ni do svidanija, ni chego bolee. Posle poses
chenija na uzhin restorana Sinema, voobsche chem-to otravilsja. Maksimal'no tjanet na 3 zvezdy)
'''
print(y_train[404]) # 0