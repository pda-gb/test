def search_pairs(array, k):
  i = 0
  itm = 0
  jtm = 0
  j = 0
  x = 0
  y = 0
  out_list = []
  sub_out = ()
  sub_out1 = ()
  sub_out2 = ()
  answer = []
  while i < len(array):   ## перебираем каждый элемент в array
      itm = i + 1
      a = array[i]   ## запоминаем первый элемент
      while itm < len(array):   ## перебираем последующие...
          b = array[itm]
          if a + b == k:    ## что бы просуммировать с первым
              sub_out = (a, b)   ## если их сумма равна пяти, то создаём кортеж 
              out_list.append(sub_out)   ## и добавляем в свой список
              j = 0
              jtm = 0
              while j < len(out_list):   ## аналогично перебираем свой список..
                  sub_out1 = out_list[j]
                  jtm = j + 1
                  while jtm < len(out_list):
                      sub_out2 = out_list[jtm]
                      if sub_out1[0] == sub_out2[1]  or sub_out1[0] == sub_out2[0]:     ## ...что бы найти дубли..
                          out_list.remove(sub_out2)   ## и удалить их
                      jtm+=1
                  j+=1
          itm += 1

      i += 1
  return out_list





print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))
