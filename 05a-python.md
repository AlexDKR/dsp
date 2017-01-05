# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Similarities:
>> They're both sequences.
>> 
>> Differences:
>> Tuples are immutable, while lists are mutable and you can modify order, placement, etc.
>> As a result, mapping, pushing, popping, concatenating, and more can be done with lists.
>> 
>> Tuples will work as keys in dictionaries. Technically, I'm assuming that they both would work.  
>> However, a property of tuples are that they are immutable. By definition and construction, they cannot be modified. This results in predictable and favorable behavior when working with dictionaries.
>> Lists, on the other hand are mutable and could result in unpredictable behavior.
---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Similarities:
>> They're both sequences.
>> 
>> Differences:
>> Lists are mutable allowing for methods like mapping, pushing, popping, concatenating, and more can be done with lists.
>> 
>> Sets can be faster in terms of performance when the sequences have lots of elements.
>> 
>> Lists are based on dynamic arrays and sets are based on hash tables.
>> Hash tables outperform dyanamic arrays when looking for an element when there are lots of elements
>> 
>> see q2_lists_sets.py in python

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's 'lambda' is an operator used to create assignments that behave like functions.
>> 
>> It is used for one-time use, terse functions and complete expressions without creating multiple lines in a method, further away from the executed statement.
>> 

```python
# Q3 Lambda functions
# pull in the faculty dictionary from the advanced file
faculty_dict = {('Yimei', 'Li'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'liy3@email.chop.edu'], ('Hongzhe', 'Li'): [' Ph.D', 'Professor of Biostatistics', 'hongzhe@upenn.edu'], ('Justine', 'Shults'): [' Ph.D.', 'Professor of Biostatistics', 'jshults@mail.med.upenn.edu'], ('Wei', 'Yang'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'weiyang@mail.med.upenn.edu'], ('Matthew', 'Bryan'): [' PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu'], ('Kathleen', 'Propert'): [' Sc.D.', 'Professor of Biostatistics', 'propert@mail.med.upenn.edu'], ('Wensheng', 'Guo'): [' Ph.D', 'Professor of Biostatistics', 'wguo@mail.med.upenn.edu'], ('Phyllis', 'Gimotty'): [' Ph.D', 'Professor of Biostatistics', 'pgimotty@upenn.edu'], ('Jonas', 'Ellenberg'): [' Ph.D.', 'Professor of Biostatistics', 'jellenbe@mail.med.upenn.edu'], ('Wei-Ting', 'Hwang'): [' Ph.D.', 'Associate Professor of Biostatistics', 'whwang@mail.med.upenn.edu'], ('Michelle', 'Ross'): [' PhD', 'Assistant Professor is Biostatistics', 'michross@upenn.edu'], ('Jinbo', 'Chen'): [' Ph.D.', 'Associate Professor of Biostatistics', 'jinboche@upenn.edu'], ('Sharon', 'Xie'): [' Ph.D.', 'Associate Professor of Biostatistics', 'sxie@mail.med.upenn.edu'], ('Jason', 'Roy'): [' Ph.D.', 'Associate Professor of Biostatistics', 'jaroy@mail.med.upenn.edu'], ('Mingyao', 'Li'): [' Ph.D.', 'Associate Professor of Biostatistics', 'mingyao@mail.med.upenn.edu'], ('Yenchih', 'Hsu'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'hsu9@mail.med.upenn.edu'], ('Mary', 'Sammel'): [' Sc.D.', 'Professor of Biostatistics', 'msammel@cceb.med.upenn.edu'], ('Warren', 'Bilker'): ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu'], ('A.', 'Localio'): [' JD MA MPH MS PhD', 'Associate Professor of Biostatistics', 'rlocalio@upenn.edu'], ('Haochang', 'Shou'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'hshou@mail.med.upenn.edu'], ('Rui', 'Xiao'): [' PhD', 'Assistant Professor of Biostatistics', 'rxiao@mail.med.upenn.edu'], ('Benjamin', 'French'): [' PhD', 'Associate Professor of Biostatistics', 'bcfrench@mail.med.upenn.edu'], ('Sarah', 'Ratcliffe'): [' Ph.D.', 'Associate Professor of Biostatistics', 'sratclif@upenn.edu'], ('Rui', 'Feng'): [' Ph.D', 'Assistant Professor of Biostatistics', 'ruifeng@upenn.edu'], ('Dawei', 'Xie'): [' PhD', 'Assistant Professor of Biostatistics', 'dxie@upenn.edu'], ('Pamela', 'Shaw'): [' PhD', 'Assistant Professor of Biostatistics', 'shawp@upenn.edu'], ('Nandita', 'Mitra'): [' Ph.D.', 'Associate Professor of Biostatistics', 'nanditam@mail.med.upenn.edu'], ('Scarlett', 'Bellamy'): [' Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu'], ('Marshall', 'Joffe'): [' MD MPH Ph.D', 'Professor of Biostatistics', 'mjoffe@mail.med.upenn.edu'], ('Susan', 'Ellenberg'): [' Ph.D.', 'Professor of Biostatistics', 'sellenbe@upenn.edu'], ('Knashawn', 'Morales'): [' Sc.D.', 'Associate Professor of Biostatistics', 'knashawn@mail.med.upenn.edu'], ('Alisa', 'Stephens'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'alisaste@mail.med.upenn.edu'], ('Rebecca', 'Hubbard'): [' PhD', 'Associate Professor of Biostatistics', 'rhubb@mail.med.upenn.edu'], ('Mary', 'Putt'): [' PhD ScD', 'Professor of Biostatistics', 'mputt@mail.med.upenn.edu'], ('Andrea', 'Troxel'): [' ScD', 'Professor of Biostatistics', 'atroxel@mail.med.upenn.edu'], ('Russell', 'Shinohara'): ['0', 'Assistant Professor of Biostatistics', 'rshi@mail.med.upenn.edu'], ('J.', 'Landis'): [' B.S.Ed. M.S. Ph.D.', 'Professor of Biostatistics', 'jrlandis@mail.med.upenn.edu']}

# create a unique list of names from the dictionary
last_name_list = []
for name in faculty_dict.keys(): 
    if name[1] not in last_name_list:
        last_name_list.append(name[1])

print 'Last Name List:'
print last_name_list[:4]
print

# sort the last name list by last name
last_name_list = sorted(last_name_list, key=lambda name:name[0])

print 'Sorted Last Name List:'
print last_name_list[:4]
print
```
>> sorted example
>> sorted(key = x: lambda x(?))

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE
>> list comprehensions are a way to manipulate a list in a single line, as opposed to creating multiple lines.
>> 
>> examples with list comprehension
>> 
>> example with map
>> 
>> example with filter
>> 
>> demonstrate set comprehensions
>> 
>> demonstrate dicitonary comprehensions

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> There were 937 days between 01-02-2013 and 07-28-2015.

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> There were 513 days between 12-31-2013 and 05-28-2015.

c.  
```
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
```

>> There were 7850 days between 15-Jan-1994 and 14-Jul-2015.


Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





