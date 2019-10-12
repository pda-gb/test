# task_2

import re

C = 64   ## константа для сдвига индекса букв по юникод таблице
summ_name = 0
j_idx = 1
proizved = 0
summ_all_proizved = 0
spam_str = []
buff_list = []
names = open('names.txt')   
data = []
data = names.read()  ## заносим всё из файла в переменную одной строкой
names.close()
spam_str = re.findall('\w+', data)   ## ищем имена по образцу - рег. выражением и закидываем в список
spam_str.sort()   ## сортируем
for i in spam_str: перебираем список
    itm = 0
    summ_name = 0    ## для каждого элемента списка сумма и произведение высчитывается с начала
    proizved = 0
    for itm in i:   ## каждый элемент списка перебираем по буквам
        summ_name = summ_name + (ord(itm) - C)   ## опеределяем индекс по юникод-таблице и сдвигаем константой(было А-65, стало А-1), и суммируем
    proizved = summ_name * j_idx   ## вычисляем произведение
    summ_all_proizved = summ_all_proizved + proizved   ## вычисляем конечную сумму всех произведений(конечный ответ)
    #print(f'summ_name: {summ_name}, j_idx: {j_idx}, proizved: {proizved}, answ: {summ_all_proizved}')
    j_idx+=1
print('all:', summ_all_proizved)

## answ: 871853874
