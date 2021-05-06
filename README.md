# Capstone Project 

**Objective:** Build an application which sends an "Award of excellence" certificate with attachment and appropriate content. 

**Prerequisites:** We have files:
1. A csv file containing name, email, score
2. A txt file where email content is written
3. A jpg file containing image of empty certificate.

### Steps to solve this:
#### 1. Data Processing:
1. Read a csv file
2. Extract single columns in lists
3. For column Name, processing such as check for valid name, conversion to proper are done.
4. For column email, regex check was done.
5. For column score, validity checks such as only positive numbers should be allowed.

#### 2. Image Processing:
1. Read a jpg image
2. Identify the coordinates to write name, course name, date and signature are done.
3. Writing on the image.
4. Once writing is done, certificates were created.
5. All certificates are custom as per the name and stored in a folder.
6. If certificates were already present, files were not created

#### 3. Send email:
1. check connection. If connection is there, then only send the email
2. Create email content, subject, body. 
3. Connect to the server and send email.

#### Package:
We have created a package for this purpose, Award Certificate and it has following files:
1. __ init__.py file.
2. data_processing.py module.
3. image_processing.py module.
4. send_email.py module.

data_processing.py module has following functions:
csv_to_column: Reads csv file and converts into a list based on column name.
 Input: 
        filename: Name of the file to be read and processed 
        colname: column name
        delimiter: file delimiter. Mostly ","
    Output: 
        list containing only required column


regex_check: Checks for regular expression
    input: 
        email_id: email id of a person
    output:
        "email_id" if valid otherwise "Invalid Email"


check_valid_name: checks if name has any non-alphabetical content.
    Input: 
        name: name of a person
    Output:
        name if valid otherwise "invalid name"

check_valid_score: checks if score is a number or not.
    Input: 
        score: score
    Output:
        score if valid otherwise "Invalid Score"


image_processing.py module has following functions:
create_certi: 
    Input:
        read_path: path from where image needs to be read
        write_path: path where image will be stored
        name: name to write on the image
    Output: 
        Ready image after writing based on the requirement

send_email.py module has following functions:
check_connection: It's a closure and checks whether internet connection is there or not.
    Input:
        a function
    Output:
        Inner function
inner1 function: prints connected in green when connection is there, otherwise prints status code is not 200 in red.

send_email: this function sends email to desired email address
    Input:
        filepath: path of the attachment file to be taken
        name: name of the receiver
        receiver_email: receiver's email address
        score: receiver's score in the course.

test.py file: test cases

# tests if readmefile exists or not
test_readme_exists():

# tests if readmefile exists or not
test_readme_contents():

# tests if readmefile content are good and readme file formatting
test_readme_file_for_formatting():

# Check if csv file exists or not
test_nofile():

# Check if function regex_check is working or not, that means if there is any regular expression in the email, it should return invalid email.
test_regex():

# Check function check_valid_name. If name is invalid, function will return Invalid Name, otherwise it will return name.
test_valid_name():

# Check function check_valid_score. If score is invalid, that means if it's a string, it will return invalid score, otherwise it will return score
test_valid_score():

# Check check_valid_score. If score is negative, function will return invalid score, otherwise it will return the score.
test_valid_score_positive():
