# TODO Create Variables
#   - Create the following variables
#   - my_first_name
#       -set this equal to your first name
my_first_name = 'Scott'
#   - my_last_name
#       -set this equal to your last name
my_last_name = 'Hadzik'
#   - my_year_of_birth
#       -set this equal to your birth year (doesn't have to be real should be less then 100 yrs ago)
my_year_of_birth = 1980
#   - current_year
#       -set this equal to 2020
current_year = 2023

# TODO String Indexing
#   - Print the following items (one per line) (print using variables)
#       - first name
print(my_first_name)  
#       - last name
print(my_last_name)
#       - first letter of your first name (use the +index)
print(my_first_name[0])
#       - second to last letter of your last name (use the -index)
print(my_last_name[-2])
#       - first two letter of your first name (use the +index)
print(my_last_name[:2])

#       - last two letter of your last name (use the -index)
print(my_last_name[-2:])

#TODO Combining Strings
#   - Print the following items (one per line) (print using variables)
#       -first name and last name combined
print(my_first_name + my_last_name) # concat
print(my_first_name + ' ' +  my_last_name) # concat
print(my_first_name, my_last_name) # concat
#       -first name six times
print(my_first_name*6)

# TODO Formatting Strings
#   - Print the following items (one per line) (print using variables)
#       - first name last name -was born in- year of birth
print(my_first_name, my_last_name, 'was born in', my_year_of_birth)
#       - first name last name -was born in- year of birth. first name -enjoyed celebrating- current year
print(my_first_name, my_last_name, 'was born in', my_year_of_birth, '.', my_first_name,'enjoyed celebrating', current_year )



# TODO Escape characters
#   - Print the following items (one per line) (print using variables)
#       - possesive first name -birth year is- year of birth 
#       - tab last name current year


# TODO String methods
#   - Print the following items (one per line) (print using variables)
#       - first name and last name in lower case
#       - length of last name
#       - first name and last name all in upper case