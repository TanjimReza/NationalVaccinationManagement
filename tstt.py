# from pprint import pprint
# input = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]
# K = 6 
# emp = []

# for each_tuple in input:
#     if each_tuple[0] % K == 0 and \
#         each_tuple[1] % K == 0 and \
#             each_tuple[2] % K == 0:
#                 emp.append(each_tuple)
# pprint(emp)


# lst = ['a', 'b', 'c', 'd',
#        'e', 'f', 'g', 'h',
#        'i', 'j', 'k', 'l',
#        'm', 'n', 'o', 'p',
#        'q', 'r']
# new_lst = []
# for i in range(0, len(lst), 4):
#     new_lst.append(lst[i:i+4])
# pprint(new_lst)

# my_dict = {}

# for eachList in new_lst:
#   ascii_sum = 0
#   for char in eachList:
#     ascii_sum += ord(char)
#   my_dict[ascii_sum] = eachList
# pprint(my_dict)

# input1 = "I love programming. Python is love."
# # input1 = "The secret of getting ahead is getting started."
# sentence_list = input1.split(".")
# special_list = ['@', '$', '&', '#']
# # special_list = ['-', '=', '+', '*', '%']
# # lst = [i.split() for i in lst]
# # Create a list of words in the document
# # create empty list for words
# word_list = []

# # loop over sentences in sentence_list
# for sentence in sentence_list:
# 	# split sentence into words
# 	current_words = sentence.split()
# 	# loop over words in current_words
# 	for word in current_words:
# 		# add word to word_list
# 		word_list.append(word)
# # print word_list
# pprint(word_list)
# #* create an empty dictionary
# my_dict = {} 
# #* loop through each word in the list
# for word in word_list: 
#     #* create a variable to hold the ascii_sum
# 	ascii_sum = 0 
# 	for char in word: #* loop through each character in the word
#      #* add the ascii value of the character to the ascii_sum variable
# 		ascii_sum += ord(char) 
#     #* find the remainder of the ascii_sum divided by the length of the special_list
# 	index_n = ascii_sum % len(special_list) 
#     #* set the key to the value at the index of the special_list
# 	key = special_list[index_n] 
# 	#* set the value to the current word
# 	value = word 
	
#  #* if the key already exists in the dictionary
# 	if key in my_dict: 
#      	#* create a variable to hold the existing values
# 		existing_values = my_dict[key] 
#   		#* if the value is not already in the list of existing values
# 		if value not in existing_values: 
# 			existing_values.append(value) #* append the value to the existing values list
# 			my_dict[key] = existing_values #* set the value to the key in the dictionary
# 	else: #* if the key does not exist in the dictionary
# 		my_dict[key] = [value] # set the value to the key in the dictionary

# pprint(my_dict) # print the dictionary

# my_dict = {}
# list_1 = [("a", 1), ("b", 2), 
#           ("a", 3), ("b", 1), 
#           ("a", 2), ("c", 1)]
# for item in list_1:
# 	key, value = item
# 	if key in my_dict:
# 		my_dict[key].append(value)
# 	else:
# 		my_dict[key] = [value]
# pprint(my_dict)

