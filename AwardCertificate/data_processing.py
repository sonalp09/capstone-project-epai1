# Data processing: This module processes data based on the requirements. Basic data processing are:
# 1. Extracting column from the data
# 2. Checks for regular expression in email id. There should not be any regular expression in email id. 
# 3. Checks for name: Name should consist only alphabets and space, and no specific characters and numbers.
# To be done: Score check: Only numbers
# To be done: Score check: Only integer
# To be done: Score check: Only positive numbers

# Required package to be imported
import csv
import re
import os

def csv_to_column(filename, colname:'string', delimiter = ',') -> 'list':
    '''
    csv_to_column: Reads csv file and converts into a list based on column name.
    Input: 
        filename: Name of the file to be read and processed 
        colname: column name
        delimiter: file delimiter. Mostly ","
    Output: 
        list containing only required column
    '''
    try:
        if os.stat(filename).st_size == 0:
            raise ValueError("File is empty")
        else:
            with open(filename) as f:
                headers = next(csv.reader(f, delimiter=delimiter, skipinitialspace=True))
                headers = [header.strip() for header in headers]
                row_col_name = []
                for row in csv.DictReader(f, fieldnames=headers, 
                                       delimiter=delimiter, skipinitialspace=True):
                    row_col_value = row[colname].strip()
                    row_col_name.append(row_col_value)
            return row_col_name
    except IOError:
        raise ValueError("File not found")
            
# Regex check
def regex_check(email_id:"string") -> "string":
    '''
    regex_check: Checks for regular expression
    input: 
        email_id: email id of a person
    output:
        "email_id" if valid otherwise "Invalid Email"
    '''
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
    if re.search(regex, email_id):
        return email_id
    else:
        return "Invalid Email"

# check for valid names
def check_valid_name(name:"string") -> "string":
    '''
    check_valid_name: checks if name has any non-alphabetical content.
    Input: 
        name: name of a person
    Output:
        name if valid otherwise "invalid name"
    '''
    if all(char.isalpha() or char.isspace() for char in name):
        return name
    else:
        return "Invalid Name"

def check_valid_score(score: 'float'):
    '''
    check_valid_score: checks if score is a number or not.
    Input: 
        score: score
    Output:
        score if valid otherwise "Invalid Score"
    '''
    if score.isnumeric== True:
        if float(score) < 0.0:
            return "Invalid Score" 
        else:
            return float(score)
    else:
        return "Invalid Score"
