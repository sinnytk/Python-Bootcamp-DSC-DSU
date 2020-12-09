# student1_roll_num=input("Enter Roll Number Of First Student")
# student1_name=input("Enter Name Of First Student")
# student2_roll_num=input("Enter Roll Number Of Second Student")
# student2_name=input("Enter Name Of Second Student")
# student3_roll_num=input("Enter Roll Number Of Third Student")
# student3_name=input("Enter Name Of Third Student")
# student4_roll_num=input("Enter Roll Number Of Fourth Student")
# student4_name=input("Enter Name Of Fourth Student")
# student5_roll_num=input("Enter Roll Number Of Fifth Student")
# student5_name=input("Enter Name Of Fifth Student")
Student_Record={
1:[input("Enter Roll Number Of First Student: "),input("Enter Name Of First Student: "),input("Enter Age Of First Student: "),input("Enter Marks Of First Student: ")],
2:[input("Enter Roll Number Of Second Student: "),input("Enter Name Of Second Student: "),input("Enter Age Of Second Student: "),input("Enter Marks Of Second Student: ")],
3:[input("Enter Roll Number Of Third Student: "),input("Enter Name Of Third Student: "),input("Enter Age Of Third Student: "),input("Enter Marks Of Third Student: ")],
4:[input("Enter Roll Number Of Fourth Student: "),input("Enter Name Of Fourth Student: "),input("Enter Age Of Fourth Student: "),input("Enter Marks Of Fourth Student: ")],
5:[input("Enter Roll Number Of Fifth Student: "),input("Enter Name Of Fifth Student: "),input("Enter Age Of Fifth Student: "),input("Enter Marks Of Fifth Student: ")]

}
if int(Student_Record[1][3])>100 or int(Student_Record[2][3])>100 or int(Student_Record[3][3])>100 or int(Student_Record[4][3])>100 or int(Student_Record[5][3])>100:
	print("Kindly print marks out of 100")
else:
	max_mark=max(Student_Record[1][3],Student_Record[2][3],Student_Record[3][3],Student_Record[4][3],Student_Record[5][3])
	min_mark=min(Student_Record[1][3],Student_Record[2][3],Student_Record[3][3],Student_Record[4][3],Student_Record[5][3])
	sum_mark=int(Student_Record[1][3])+int(Student_Record[2][3])+int(Student_Record[3][3])+int(Student_Record[4][3])+int(Student_Record[5][3])
	print ("{:<10} {:<10} {:<10} {:<10}".format('Roll_No', 'Name', 'Age','Marks'))
	for key, value in Student_Record.items(): 
		Roll_No, Name, Age, Marks = value 
		print ("{:<10} {:<10} {:<10} {:<10}".format(Roll_No, Name, Age, Marks)) 
	print("CLASS MAXIMUM MARKS:      "+max_mark)
	print("CLASS MINIMUM MARKS:      "+min_mark)
	print("CLASS AVERAGE MARKS:     ",sum_mark/len(Student_Record))