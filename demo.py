import pss


key = pss.dump('test.bin', 'Test message!')
print(pss.load('test.bin', key))