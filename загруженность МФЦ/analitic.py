
    
    #ПРиложение 1
    #наполняет БД или файла
    
    # Приложение 2
    # -диаграмма загруженности для каждого дня
    # (Matplotlib)


def obrabotka(filename):
    with open(filename,'r', encoding = "utf8") as f:
        for line in f:
            nam = line[:10] + '.csv'
            #print(nam)
            with open(nam,'a', encoding = "utf8") as f2:
                f2.write(line[11:])
            #visitor = line
    return 'OK'

def obrabotka2(filename):
    with open(filename,'r', encoding = "utf8") as f:
        for line in f:
            nam = line[:10] + '.csv'
            #print(nam)
            with open(nam,'a', encoding = "utf8") as f2:
                f2.write(line[11:])
            #visitor = line
    return 'OK'    

# s = input('хотите обработать файл mfc.csv? да/нет   ')
# if s == 'да' or s == 'д' or s == 'y' or s == 'yes':
    # fnme = 'mfc.csv'
    # print(obrabotka(fnme))

s = input('хотите обработать файл mfc2.csv? да/нет   ')
if s == 'да' or s == 'д' or s == 'y' or s == 'yes':
    fnme = 'mfc2.csv'
    print(obrabotka2(fnme))

data_visita = '2021-04-17.csv' #чтобы потом можно было как-то автоматом обработать
new_dict = {"08:00":[],\
            "09:00":[],\
            "10:00":[],\
            "11:00":[],\
            "12:00":[],\
            "13:00":[],\
            "14:00":[],\
            "15:00":[],\
            "16:00":[],\
            "17:00":[],\
            "counter_mm": 0\
            }
#counter_mm - счетчик человеко-минут всего
with open(data_visita,'r', encoding = "utf8") as f:
    for line in f:
        time_in_out = line.replace('\n', '').split(';')         #список времени прихода-ухода
        hour_v = time_in_out[0].split(':')[0]                      #час прихода в мфц
        ##предположим, что 2 часа никто не ждет
        if (int(time_in_out[1].split(':')[0]) - int(time_in_out[0].split(':')[0])) == 0:        
            new_dict[hour_v + ':00'].append(int(time_in_out[1].split(':')[1]) - int(time_in_out[0].split(':')[1])) #добавляем время
            new_dict['counter_mm'] += int(time_in_out[1].split(':')[1]) - int(time_in_out[0].split(':')[1])
        else:
            new_dict[hour_v + ':00'].append(60 - (int(time_in_out[0].split(':')[1])))                   #добавляем время к часу прихода
            new_dict['counter_mm'] += (60 - (int(time_in_out[0].split(':')[1])))
            new_dict[time_in_out[1].split(':')[0] + ':00'].append(int(time_in_out[1].split(':')[1])) #добавляем время к часу ухода
            new_dict['counter_mm'] += int(time_in_out[1].split(':')[1])
        # if ((int(time_in_out[1].split(':')[0]) - int(time_in_out[0].split(':')[0]))) > 0:           #предположим, что 2 часа никто не ждет
            # dlit_v = 60 - (int(time_in_out[0].split(':')[1])) + int(time_in_out[1].split(':')[1])     #длительность ожидания
        # else:
            # dlit_v = int(time_in_out[1].split(':')[1]) - int(time_in_out[0].split(':')[1])
        #new_dict[].append
        
        #print(type(time_in_out))
        #print(type(hour_v))
        #print(dlit_v)


    for t in new_dict:        
        if t == 'counter_mm':
           continue
        str2console = t + ' ' + '#' * (int(sum(new_dict[t]) / new_dict['counter_mm'] * 100))
        print(str2console)    