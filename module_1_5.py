immutable_var = 5,6,["seven", "eight"],"nine"
print(type(immutable_var))
print(immutable_var)
# immutable_var[0]=7  будет ошибка так как oбъект 5 относится к неизменяемому классу "int"
# immutable_var[3]="twenty"  так же будет ошибка так как объект "nine" относится к неизменяемому классу "str"
immutable_var[2][1]="seven" # можно присвоить новое значение так как объект "eight" относится к классу "list"
print(immutable_var)

mutable_list = [123,"four","five"]
print(type(mutable_list))
mutable_list.remove("five")
mutable_list[0]=456
mutable_list[1]=123
mutable_list = mutable_list[::-1]
mutable_list.extend([789,10])
print(mutable_list)