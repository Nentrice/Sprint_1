string = '1h 45m,360s,25m,30m 120s,2h 60s'
string = string.replace(' ', ',')
new_str = string.split(',')
result = 0

for value in new_str:
    if 'h' in value:
        result += (int(value.replace('h', '')) * 60)
    elif 'm' in value:
        result += int(value.replace('m', ''))
    elif 's' in value:
        result += (int(value.replace('s', '')) // 60)
    else: print('Неверный формат данных')
print(result)