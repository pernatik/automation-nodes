#!/bin/bash

set -e

# VAR
fee=0,01
#
wal_info_array=()

if [[ ${#MASSA_PASSWD} -le 4 ]]; then
    echo "Следует проверить переменную MASSA_PASSWD"
    exit 1
fi

wal_info=`cd /root/massa/massa-client && ./massa-client -p ${MASSA_PASSWD}  wallet_info | sed 's/,//g'`
for i in $wal_info; do wal_info_array+=($i); done

address=${wal_info_array[2]} # Адрес кошелька
balance=${wal_info_array[6]} 
balance=`echo $balance | cut -c 7- | cut -d '.' -f 1` # Баланс

if [[ $balance -ge 100 ]]; then
    rollcount=$(( $balance / 100 ))
    `cd /root/massa/massa-client && ./massa-client -p ${MASSA_PASSWD} buy_rolls ${address} ${rollcount} ${fee}`
    echo "Куплено $rollcount шт"
else
    echo "Недостаточно средств для покупки"
fi
