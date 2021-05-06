import pytest
import os
import inspect
import main
import AwardCertificate
from AwardCertificate import data_processing
import re
from datetime import datetime, timezone

# tests if readmefile exists or not
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

# tests if readmefile exists or not
def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r', encoding="utf-8") for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

# tests if readmefile content are good and readme file formatting
def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

# Check if csv file exists or not
def test_nofile():
    with pytest.raises(ValueError):
        capstone_project.data_processing.csv_to_column("", "name", ",")

# Check if function regex_check is working or not, that means if there is any regular expression in the email, it should return invalid email.
def test_regex():
    assert capstone_project.data_processing.regex_check("s5675th") == "Invalid Email", "Validity check for regular expression is not working"

# Check function check_valid_name. If name is invalid, function will return Invalid Name, otherwise it will return name.
def test_valid_name():
    assert capstone_project.data_processing.check_valid_name("nama69") == "Invalid Name", "Validity check for name is not working"

# Check function check_valid_score. If score is invalid, that means if it's a string, it will return invalid score, otherwise it will return score
def test_valid_score():
    assert capstone_project.data_processing.check_valid_score("sam") == "Invalid Score", "Validity check for score is not working"

# Check check_valid_score. If score is negative, function will return invalid score, otherwise it will return the score.
def test_valid_score_positive():
    assert capstone_project.data_processing.check_valid_score("-2") == "Invalid Score", "Validity check for score is not working"
