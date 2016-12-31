import pandas as pd
import re
from collections import OrderedDict

# convert to dataframe
faculty_df = pd.read_csv('faculty.csv')

# create ' first name' and ' last name' columns
# is it possible to do something like the following:
# faculty_df[' first name'], faculty[' last name'] = faculty_df['name'].apply(get_first_and_last)
# any way to do these in parallel?
faculty_df[' last name'] = faculty_df['name'].apply(lambda name: name.split()[-1])
faculty_df[' professor name'] = faculty_df['name'].apply(lambda name: (name.split()[0], name.split()[-1]) )
faculty_df[' dict_values'] = faculty_df.apply(lambda df: [df[' degree'] , df[' title'], df[' email']], axis = 1)

# sort by first name
faculty_df = faculty_df.sort(columns = 'name')

# print faculty_df

# Q6: print out key-value pairs
# faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
#                  'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
# convert faculty df to a dictionary


faculty_last_group = faculty_df.groupby(' last name')
# test to find groups
# for name, group in faculty_last_group:
#     print name
#     print group
#     print

# create a dictionary
faculty_last_dict = OrderedDict.fromkeys(faculty_df[' last name'], [])

# assign values to the dictionary
print 'Q6. key-value pairs based on last name'
for last_name, info in faculty_last_dict.iteritems():
    faculty_last_dict[last_name] = faculty_last_group.get_group(last_name)[' dict_values'].tolist()
    print '%s: %s' % (last_name, faculty_last_dict[last_name])
print





# Q7: print out key-value pairs
# professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], 
#                   ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], 
#                   ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], 
#                   ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], 
#                   ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }

# create groups by professor name
faculty_professor_group = faculty_df.groupby(' professor name')

# create a dictionary
faculty_professor_dict = OrderedDict.fromkeys(faculty_df[' professor name'], [])

# assign values to the dictionary
print 'Q7. key-value pairs based on professor tuple'
for prof_name, info in faculty_professor_dict.iteritems():
    faculty_professor_dict[prof_name] = faculty_professor_group.get_group(prof_name)[' dict_values'].tolist()
    print '%s: %s' % (prof_name, faculty_professor_dict[prof_name])
print





# Q8. print out dictionary key value pairs in order of last names
# sort by last name
faculty_l_df = faculty_df.sort(columns = ' last name')

# create groups by professor name
faculty_professor_l_group = faculty_l_df.groupby(' professor name')

# create a dictionary
faculty_professor_l_dict = OrderedDict.fromkeys(faculty_l_df[' professor name'], [])

# assign values to the dictionary
print 'Q8. key-value pairs based on professor tuple, last name'
for prof_name, info in faculty_professor_l_dict.iteritems():
    faculty_professor_l_dict[prof_name] = faculty_professor_l_group.get_group(prof_name)[' dict_values'].tolist()
    print '%s: %s' % (prof_name, faculty_professor_l_dict[prof_name])
print





