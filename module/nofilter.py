def lst_chan():
    lst = [10, 7, 6, 9, 12, 4, 5, 2, 15]
    new_lst= []
    for i in lst:
        if i%2 == 0:
            new_lst.append(i)
        print("List số chẵn là:",new_lst)
lst_chan()