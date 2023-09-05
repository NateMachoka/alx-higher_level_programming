#!/usr/bin/python3
for ascii_value in range(97, 123):
    if(chr(ascii_value)) not in 'qe':
       print("{}".format(chr(ascii_value)), end ='')
