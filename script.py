import mysql.connector as mysql
myConnection  = mysql.connect(host='localhost', user=' dmkimberlingt', passwd='' R00tp@$$w0rd”, db ='accidents')
cur = myConnection.cursor()
cur.execute('SELECT vtype FROM vehicle_type WHERE  vtype LIKE "%motorcycle%";') cycleList = cur.fetchall()
selectSQL = ('''SELECT t.vtype, a.accident_severity FROM accidents_2016 AS a JOIN vehicles_2016 AS v ON a.accident_index = v.Accident_Index JOIN vehicle_type AS t ON v.Vehicle_Type = t.vcode WHERE t.vtype LIKE "%s" ORDER BY a.accident_severity;''')
insertSQL = ('''INSERT INTO accident_medians VALUES (%s, %s);''')
for cycle in cycleList: cur.execute(selectSQL,cycle[0])
    accidents = cur.fetchall()
    quotient, remainder = divmod(len(accidents),2)
    if  remainder:
        med_sev = accidents[quotient][1]
    else:med_sev = (accidents[quotient][1] + accidents[quotient+2][1])/2
print('Finding median for',cycle[0])
cur.execute(insertSQL,(cycle[0],med_sev))
myConnection.commit()
myConnection.close()
