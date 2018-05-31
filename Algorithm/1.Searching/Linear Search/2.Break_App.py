import re
msg = int(input());
dt_count = 0
other = 0
while(msg > 0):
    msg -= 1
    chat = input();
    l = re.findall('\s*?([0-9]{1,2})\s*', chat);    
    #print ('asd: ',l);
    l = [int(d) for d in l]
    #print ('ints: ',l);
    #print ('All 2-digits: ', l);
    dte = [d for d in l if (d == 19) or (d == 20)]
    #print ('::', dte);    
    oth = [d for d in l if ( (d >= 1) or (d <= 30) ) and (d != 19) and (d != 20)]
    dt_count += len(dte) * 4
    other += len(oth) * 3
    dte = oth = []
 
if dt_count > other:
    print ('Date')
else:
    print ('No Date')