Все скрипты написаны с использованием SHELLPY, поэтому необходимо установить зависимости:
```
apt install python3-pip
pip install shellpy
```

Запуск скрипта <code php>/usr/local/bin/shellpy /root/xxx.spy</code>

Запуск скрипта из cron: 
```
*/5 * * * * /usr/local/bin/shellpy /root/xxx.spy
```

Решение проблемы <code>/usr/bin/env: ‘python’: No such file or directory</code>

```
apt install python-is-python3
```
