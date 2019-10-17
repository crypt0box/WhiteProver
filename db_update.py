# coding: utf-8
import subprocess
import sqlite3

conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()
mac_list = {}
researchers = {}

# データ（レコード）取得
sql = 'select first_name, mac, status  from register_user'
for row in c.execute(sql):
    mac_list[row[0]] = row[1]
    researchers[row[0]] = row[2]

for mac_researcher in mac_list:
    cmd = 'sudo l2ping -c 1 '+mac_list[mac_researcher]
    try:
        proc = subprocess.check_output(cmd.split()).decode()
        if '1 received' in proc:
            researchers[mac_researcher] = '在室'
        else:
            researchers[mac_researcher] = '不在'
    except:
        pass

try:
    for researcher in researchers:
            if researchers[researcher] == '在室':
                c.execute("update register_user set status = '在室'"
                          " where first_name = ('%s')" % researcher)
            else:
                c.execute("update register_user set status = '不在'"
                          " where first_name = ('%s')" % researcher)


except sqlite3.Error as e:
    print("error", e.args[0])

conn.commit()

conn.close()
