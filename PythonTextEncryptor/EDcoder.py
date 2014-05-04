import string
#
#
#
#
#text encoder/decoder
print 'Welcome to 8bitEncryptor.'
print 'Would you like to...'
print '[E]ncrypt, [D]ecrypt, or E[x]it?'
ch1=raw_input('>>> ')

if ch1=='e':
    print '\nType what you want encrypted:'
    str = raw_input('>>> ')
    str = str.encode('base64','strict');
    print '\n=============================================================='
    print "Encoded String: " + str;
    print '==============================================================\n'
    
if ch1=='d':
    print '\nCopy and paste or type the string you want to decode:'
    str = raw_input('>>> ')
    print '\n=============================================================='
    print 'Decoded String: ' + str.decode('base64','strict');
    print '==============================================================\n'

if ch1=='x':
    exit()

while ch1!='x':
    print 'Would you like to...\n[E]ncrypt, [D]ecrypt, or E[x]it?'
    ch1=raw_input('>>> ')
    
    if ch1=='e':
        print '\nType what you want encrypted:'
        str = raw_input('>>> ')
        str = str.encode('base64','strict');
        print '\n=============================================================='
        print "Encoded String: " + str;
        print '==============================================================\n'
        
    if ch1=='d':
        print '\nCopy and paste or type the string you want to decode:'
        str = raw_input('>>> ')
        print '\n=============================================================='
        print 'Decoded String: ' + str.decode('base64','strict');
        print '==============================================================\n'
    
    if ch1=='x':
        exit()
