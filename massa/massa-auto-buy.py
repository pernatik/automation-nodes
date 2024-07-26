#!/usr/bin/python3
#################
# Ver = 0.0.4 works on 2.2 main massa

# Modules
import os

# VAR
passwd = os.getenv("MASSA_PASSWD")
Address = 0
Fee = 0.01
text = []
balance = 0
RollCount = 0
#################
wal_i = os.popen('cd /root/massa/massa-client && ./massa-client -p $MASSA_PASSWD  wallet_info').read()

wal_i = str(wal_i)
text = wal_i.split()

balance = text[6]
index_ravno = text[6].find('=')
index_zpt = text[6].find('.')
balance = int(balance[index_ravno+1:index_zpt]) # Баланс с которым можно работать
Address = text[2]
if balance >= 100:
    #print('необходимо купить ролл')
    RollCount = balance // 100
    print(RollCount)
    os.popen('cd /root/massa/massa-client && ./massa-client -p $MASSA_PASSWD buy_rolls {Address} {RollCount} {Fee}')
    print(f'Куплено {RollCount} роллов')
else:
    print('поупать ролл не надо')
