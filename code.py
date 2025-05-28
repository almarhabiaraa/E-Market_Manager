def option_1(file_name):
	print(" ")
	print("Store item information: name, type and qunatity:")
	print("---------------------------------------------")

	item_ = 1
	option_1_key= True
	file_dict = {}
	while option_1_key:
		print(f"Please enter the information about item {item_}")
		item_name = input(f"Please enter the item name:-> ").strip()
		item_type = input(f"Please enter the item type:-> ").strip()
		item_qunatity = input(f"Please enter the item qunatity:-> ").strip()
		file_dict[item_] = [item_name,item_type,item_qunatity]
		

		ask_more_item = input(f"Add a new item yes/no:-> ").strip()
		if ask_more_item == "no":
			file = open(file_name + ".txt", "a+")
			for item in file_dict.values():
				value = str(item[0]) + " " + str(item[1]) + " " + str(item[2])
				file.write(value)
				file.write("\n")
			break
		else:
			item_ = item_ + 1
			continue


#......................................................................................
#......................................................................................
#......................................................................................


def option_2(file_name):
	print(" ")
	print("Display all items from the same type:")
	print("---------------------------------------------")
	item_type = dict()
	file = open(file_name + ".txt", "r")
	for line in file:
		v1,v2,v3 = line.split()
		item_type[v1] = v2

	new_dict = {}
	for pair in item_type.items():
		if pair[1] not in new_dict.keys():
			new_dict[pair[1]] = []
		new_dict[pair[1]].append(pair[0])

	print(new_dict)

#......................................................................................
#......................................................................................
#......................................................................................


def option_3(file_name):
	print(" ")
	print("Edit one item qunatity:")
	print("---------------------------------------------")
	file = open(file_name + ".txt", "r")
	my_dic = dict()
	for line in file:
		print("Item: " + line.split()[0] + "  *************** Qunatity: " + line.split()[2])
		my_dic[line.split()[0]] = [line.split()[1],line.split()[2]]
	print(" ")
	select_item = input("Select the item for editing its qunatity:-> ").strip()
	new_quantity_value = input("The New qunatity:-> ").strip()

	for k,v in my_dic.items():
		if k == select_item:
			v[1] = new_quantity_value

	file = open(file_name + ".txt", "w")
	for k,v in my_dic.items():
		line = str(k) + " " + str(v[0]) + " " + str(v[1])
		file.write(line)
		file.write("\n")

	print("Item qunatity is edited and the file is updated....")
	
#......................................................................................
#......................................................................................
#......................................................................................


def option_4(file_name):
	print(" ")
	print("Delete an item:")
	print("---------------------------------------------")

	file = open(file_name + ".txt", "r")
	my_dic = dict()
	for line in file:
		print("Item: " + line.split()[0])
		my_dic[line.split()[0]] = [line.split()[1],line.split()[2]]
	print(" ")
	select_item = input("Select the item to be deleted:-> ").strip()

	try:
		del my_dic[select_item]
	except KeyError:
		print("The item not existed!!!")

	file = open(file_name + ".txt", "w")
	for k,v in my_dic.items():
		line = str(k) + " " + str(v[0]) + " " + str(v[1])
		file.write(line)
		file.write("\n")

	print("Item is deleted and the file is updated....")

#......................................................................................
#......................................................................................
#......................................................................................
	

def option_5(file_name):
	print(" ")
	print("Add an item:")
	print("---------------------------------------------")
	file = open(file_name + ".txt", "r")
	my_dic = dict()
	for line in file:
		my_dic[line.split()[0]] = [line.split()[1],line.split()[2]]

	item_name = input(f"Enter the item name:-> ").strip()
	item_type = input(f"Enter enter the item type:-> ").strip()
	item_qunatity = input(f"Enter the item qunatity:-> ").strip()
	my_dic[item_name] = [item_type,item_qunatity]

	file = open(file_name + ".txt", "w")
	for k,v in my_dic.items():
		line = str(k) + " " + str(v[0]) + " " + str(v[1])
		file.write(line)
		file.write("\n")

	print("Item is added and the file is updated....")

#......................................................................................
#......................................................................................
#......................................................................................


def option_6(file_name):
	print(" ")
	print("Store items ascending or descending:")
	print("---------------------------------------------")
	file = open(file_name + ".txt", "r")
	my_dic = dict()
	for line in file:
		my_dic[line.split()[0]] = [line.split()[1],line.split()[2]]

	item_order = input(f"Select items to be ascending or descending (a,d):-> ").strip()

	file = open(file_name + ".txt", "w")

	if item_order == "a":
		l=list(my_dic.items())
		l.sort()
		final_dict_a = dict(l)
		
		for k,v in final_dict_a.items():
			line = str(k) + " " + str(v[0]) + " " + str(v[1])
			file.write(line)
			file.write("\n")

		print("Items are ascended and the file is updated....")

	if item_order == "d":
		l=list(my_dic.items())
		l.sort(reverse=True)

		final_dict_b = dict(l)
		
		for k,v in final_dict_b.items():
			line = str(k) + " " + str(v[0]) + " " + str(v[1])
			file.write(line)
			file.write("\n")

		print("Items are descended and the file is updated....")

	
#......................................................................................
#......................................................................................
#......................................................................................


def creat_file(finename):
	file = open(finename + ".txt", "a+")


#......................................................................................
#......................................................................................
#......................................................................................


def main():

	loop = True
	while loop:
		password = int(input("Please enter the correct password: ").strip())

		if password == 123:
			print("password is correct")
			print(" ")
			file_name = input("Please enter the file name: ").strip()
			key = True
			break
		else:
			print("password is wrong")
			key = False

	if key == True:
		print(" ")
		creat_file(file_name)
		print("File with name " + file_name + " is created.")
		print(" ")
		
		option_key = True
		while option_key:
			print("=======================================================")
			print("# The program options are:")
			print("1.Store item information: name, type and qunatity:")
			print("2.Display all items from the same type:")
			print("3.Edit one item qunatity:")
			print("4.Delete an item:")
			print("5.Add an item:")
			print("6.Store items ascending or descending:")
			print(" ")
			print("Enter exit for ending the program.")
			print("=======================================================")
			print(" ")
			option_value = input("Please select the option:-> ").strip()
			if option_value == '1':
				print("option-1 is selected")
				print("=======================================================")
				option_1(file_name)
				print(" ")

			if option_value == '2':
				print("option-2 is selected")
				print("=======================================================")
				option_2(file_name)
				print(" ")

			if option_value == '3':
				print("option-3 is selected")
				print("=======================================================")
				option_3(file_name)
				print(" ")

			if option_value == '4':
				print("option-4 is selected")
				print("=======================================================")
				option_4(file_name)
				print(" ")

			if option_value == '5':
				print("option-5 is selected")
				print("=======================================================")
				option_5(file_name)
				print(" ")

			if option_value == '6':
				print("option-6 is selected")
				print("=======================================================")
				option_6(file_name)
				print(" ")
			if option_value == 'exit':
				option_key = False
		print("program is Ended......")

			


if __name__ == '__main__':
	main()
	