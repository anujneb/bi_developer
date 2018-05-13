import petl as etl
table1 = etl.fromtsv("D:\JOB\BI_Developer_Challenge\donedeal_data_sample.tsv")

table2 = etl.convert(table1,'mileage',float)
table3 = etl.convert(table2,'mileage',lambda v: v*1.60934, where = lambda r: r.mileageType == 'miles' )
table4 = etl.convert(table3,'mileageType',lambda v: 'km', where = lambda r: r.mileageType in ('miles','kilometres'))
table4 = etl.convert(table3,'mileageType',lambda v: 'NA', where = lambda r: r.mileageType not in ('km'))

etl.totsv(table4, "D:\JOB\BI_Developer_Challenge\donedeal_data_etl.tsv")