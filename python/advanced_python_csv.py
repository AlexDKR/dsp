import pandas as pd
import re

# convert to dataframe
faculty_df = pd.read_csv('faculty.csv')

# Q5 take e-mail list and write to a csv
email_list = faculty_df[' email'].to_csv('emails.csv', index = False)