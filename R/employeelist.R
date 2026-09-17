Id = c(1,2,3)
emp.name = c("Ramesh","Suresh","Kamlesh")
emp_num  = 4
emp_list = list(Id,emp.name,emp_num)
print(emp_list[1])
emp_dataframe = data.frame(Id,emp.name,emp_num)
print(emp_dataframe)
newDF = read.table(file="/home/neo_phantom_byte/Downloads/Recomendations.csv",sep = ",")
#print(newDF)


dataframe = data.frame()
dataframe = edit(dataframe)
print(dataframe)
