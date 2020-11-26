"""Ping"""
def main(received=0, check=""):
    """main"""
    domain = ''
    maxx, minn, summ = 0, 0, 0
    for i in range(7):
        txt = input()
        if i == 0:
            domain = txt[txt.find('ping')+5:]
        if i == 2 and '[' and ']' in txt:
            domain = txt[txt.find('[')+1:txt.find(']')]
        if txt.count('time=') != 0:
            check = int(txt[txt.find('time')+5:txt.find('ms')])
            summ += check
            if maxx == 0:
                minn = check
            if check > maxx:
                maxx = check
            if minn > check:
                minn = check
        if txt.count('Reply from') != 0:
            received += 1
    print('Ping statistics for %s:' %(domain))
    print('    Packets: Sent = 4, Received = %d, Lost = %d (%s loss),' %\
        (received, (4-received), str((4-received)*25)+'%'))
    if received != 0:
        print('Approximate round trip times in milli-seconds:')
        print('    Minimum = %dms, Maximum = %dms, Average = %dms' %(minn, maxx, summ/received))
main()
