regex_integer_in_range = r"^[0-9]{6}$"
regex_alternating_repetitive_digit_pair = r"(.)(?=.\1)"


'''
 backreference \1 (backslash one) references the first capturing group. 
\1 matches the exact same text that was matched by the first capturing group
'''
