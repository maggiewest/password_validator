# Password Validator
Password validator program based on [NIST's](https://www.nist.gov/) 2017 [Digital Identity Guidelines](https://pages.nist.gov/800-63-3/).

## Purpose
The [python executable](github.com/maggiewest/password_validator/password_validator.py) takes individual passwords and lists of passwords (newline deliminated) from STDIN and checks if they comply with the 2017 NIST Digital Identity Guidelines. 

Specifically, the program verifies that the passwords: 
**1.** Are at least 8 characters
**2.** Are at most 64 characters
**3.** Consist of ASCII characters
**4.** Are not common passwords

## Usage

The program will print out invalid passwords along with the reason they aren't valid. In order to determine whether a password is "common" or not, the program takes a newline delimited file of weak passwords as an argument and checks if the password appears in that list. [Here](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt) is an example of a weak password list that the program can use to validate passwords against. 

### Installation

#### Prerequisites 
This program is written in Python3, so your machine will need to have Python3 installed to use the password validator.

To check if Python3 is installed on your machine, open a terminal and enter the following: 

```sh
python3 --version
```
If no version of Python3 is found, follow the directions at python.org/downloads to install it.

#### Run
**[Download](https://github.com/maggiewest/password_validator/archive/master.zip)** this repository to your local machine.

Enter the password_validator directory and run the program with a weak password list as a command line argument. 

**Example:**

```sh
cat input_passwords.txt | python3 password_validator.py weak_password_list.txt
mom --> Error: Too short
password1 --> Error: Too common
*nonascii --> Error: Contains non-ASCII characters
```
You can also run the program first and then write passwords as input at the command line. 

### Meta
Written by Maggie West
