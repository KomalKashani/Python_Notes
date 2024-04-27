# Retrieve Multiple Rows WHERE clause - Tuple
import mysql.connector
try:
	conn= mysql.connector.connect(
		user='root', 
		password='geek', 
		host='localhost', 
		database='pdb',
		port=3306
	)
	if (conn.is_connected()):
		print('Connected')
except:
	print('Unable to Connect')
	
sql = 'SELECT * FROM student WHERE roll=%s'
myc = conn.cursor(prepared=True)
disp_value = (777,)
try:
	myc.execute(sql, disp_value)
	row = myc.fetchone()
	while row is not None:
		print(row)
		row = myc.fetchone()
	print('Total Rows:',myc.rowcount)
except:
	print('Unable to Retrieve Data')
myc.close()		# Close Cursor
conn.close()	# Close Connection
