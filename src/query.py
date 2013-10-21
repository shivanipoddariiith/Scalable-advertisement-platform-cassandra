#!/usr/bin/env python
import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
pool = ConnectionPool('Keyspace1',server_list=['localhost:9160'])
col_fam = ColumnFamily(pool, 'ColumnFamily1')
check1 = col_fam.insert('row_key', {'col_name': 'col_val'})
print check1
print " is the added row into a column\n"
check2 = col_fam.insert('row_key', {'col_name':'col_val', 'col_name2':'col_val2'})
print check2
print " Multiple columns are added \n"
get_data1 = col_fam.get('row_key')
print get_data1
get_data2 = col_fam.get('row_key', columns=['col_name', 'col_name2'])
print get_data2
print "\n"
print "Slicing\n"
for i in range(1, 10):
	col_fam.insert('row_key', {str(i): 'val'})
print col_fam.get('row_key', column_start='5', column_finish='7')
print "\n"
print "Counting rows: "
print col_fam.get_count('row_key')
