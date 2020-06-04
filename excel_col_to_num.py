class util:
    def excel_col_to_num(col_str):
        BASE_NUMBER = 26
        mapper = {'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7,'i': 8,'j': 9,'k': 10,'l': 11,'m': 12,'n': 13,'o': 14,'p': 15,'q': 16,'r': 17,'s': 18,'t': 19,'u': 20,'v': 21,'w': 22,'x': 23,'y': 24,'z': 25}
        lower_col_str = col_str.lower()
        reverse_col_str = lower_col_str[::-1]
        col_count = 0
        number_of_digit = 0
        for n in reverse_col_str:
            col_count += mapper[n]
            if number_of_digit != 0 :
                col_count += ((BASE_NUMBER ** number_of_digit) * (mapper[n] + 1)) - mapper[n]
            number_of_digit += 1
        return col_count


