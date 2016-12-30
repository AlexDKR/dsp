import pandas as pd
import re

# dataframe apply functiont to 'sanitize' degree column
def convert_string(item):
    # strip out dots from the degree, also account for a no-degree scenario
    item = re.sub('\.', '', item)

    check_alpha = re.search('[a-zA-Z]+', item)
    if bool(check_alpha) is False:
        item = 'No_degree'
    
    return item

# count degrees
def count_degrees(entry, degree, degree_dict):
    check_degree = re.search(degree, entry)
    if check_degree:
        degree_dict[degree] += 1
    return degree_dict

# occupation
def find_title(title):
    title = re.sub('(?<=Professor)(.*)', '', title)
    return title

# occupation headcount
def count_occupations(title, occupation, occupation_dict):
    check_title = re.search(occupation, title)
    if check_title:
        occupation_dict[occupation] += 1
    return occupation_dict

# find email domains
def find_email_domain(email):
    domain = re.sub('.+@', '', email)
    return domain


# convert to dataframe
faculty_df = pd.read_csv('faculty.csv')

# convert degrees into standard degrees
faculty_df[' degree'] = faculty_df[' degree'].apply(convert_string)

# make a list of different entries of degrees
unique_degrees = faculty_df[' degree'].unique()

# concatenate all entries into a single string, and then take out repeated degrees
unique_degrees_string = ''
for degree in unique_degrees:
    unique_degrees_string += (degree + ' ')

# create a list of each degree entered, and split them into a list
unique_degree_list = unique_degrees_string.split()
# print unique_degree_list

# sort the degree list
unique_degree_list.sort()

# remove extra entries of the same degree
final_degree_list = []
last_degree = ''

for degree in unique_degree_list:
    if degree != last_degree:
        final_degree_list.append(degree)
        last_degree = degree

# Q1.1 how many different degrees
print 'Q1: The following is a list of the %s unique degrees and how many there are within the faculty:' % (len(final_degree_list))
# for degree in final_degree_list:
#     print degree

# Q1.2 frequencies of each degree
degree_dict = {}

for degree in final_degree_list:
    degree_dict[degree] = 0
    faculty_df[' degree'].apply(count_degrees, args=(degree, degree_dict))

# print degree_dict
for degree, count in degree_dict.iteritems():
    print '%20s: %s' % (degree, count)
print





# Q2.1 how many different titles are there
faculty_df[' title'] = faculty_df[' title'].apply(find_title)
unique_occupation_list = faculty_df[' title'].unique()
print 'Q2: There are %s different titles. A summary of faculty titles is below including how many of each there are in the faculty:' % len(unique_occupation_list)



# Q2.2 frequencies of each title
occupation_dict = {}
for occupation in unique_occupation_list:
    occupation_dict[occupation] = 0
    faculty_df[' title'].apply(count_occupations, args=(occupation, occupation_dict))
for occupation, count in occupation_dict.iteritems():
    print '%20s: %s' % (occupation, count)
print





# Q3 take e-mail addresses and put them in a list
email_list = faculty_df[' email'].tolist()

print 'Q3: The elements of email_list are printed below for ease of readability:'
for email in email_list:
    print email
print

# Q4 how many email domains are there, and print them out
faculty_df[' domain'] = faculty_df[' email'].apply(find_email_domain)
unique_domain_list = faculty_df[' domain'].unique()

print 'Q4: There are %s unique e-mail domains. They are listed below:' % len(unique_domain_list)
for domain in unique_domain_list:
    print domain

