# # import re
# with open("input.txt", "r") as f:
#     input = f.read().splitlines()  #? Read the input, split it into lines and store it in a list
# #     no_of_regex = int(input[0])  #? The first line of input is the number of regular expressions
#     regex_list = input[1:no_of_regex+1]  #? The next no_of_regex lines are the regular expressions
#     not_of_strings = int(input[no_of_regex+1])  #? The next line is the number of strings
#     string_list = input[no_of_regex+2:]  #? The next no_of_strings lines are the strings

#     #! First we loop through each string in the string list
#     for each_string in string_list:
#         #! Next we loop through each regex in the regex list
#         for i, each_regex in enumerate(regex_list):
#             #! Enumerate is used to get the index of the regex
#             if re.match(each_regex, each_string):
#                 #! If the regex matches the string, print the regex number
#                 print(f"YES,{i+1}")
#                 #! Break out of the regex loop
#                 break
#         #! If the string doesn't match any regex, we'll get here
#         else:
#             #! Print NO,0
#             print(f"NO,0")
    # r_n = int(input[0]) 
    # # print(r_n)      
    # # print(input[1:r_n+1])
    # s_n = int(input[r_n+1])
    # print(input[s_n+1:])
# user = "The purpose of our lives is to be happy"
# n=''
# l = []
# l2 = []
# for i in user:
#     #print(i)
#     if i != ' ':
#         n+=i
#     if i == ' ':
#         l.append(i)
#         n=''
# l.append(i) 
# for x in l:
#     convert = ord(str(len(x)))
#     l2.append(convert)
# print(l2)

#TASK4
# def function_name(string):
#   upper = 0
#   lower = 0
#   for i in string:
#     if ord('a')<=ord(i)<=ord("z"):   #use islower function
#       lower+=1
#     elif ord('A')<=ord(i)<ord("Z"): #use isupper function
#       upper+=1
#   print(f"No. of Uppercase Characters: {upper}")
#   print(f"No. of Lowercase Characters: {lower}")   
# function_name('The quick Sand Man')