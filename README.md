## Title
## Contact Book Software

## Description
A python based software that provides ability to a user to store their contact information digitally on it's own system. the software also provide features
like add new contact, update previous contact, delete contact details, searching a contact from list of contacts and sorting. i made this software to rewind my skills regarding to the SQL and DBMS.

## Installation
1. **Install Python and MySQL** : Ensure that you have installed mysql and python in your system
2. **Changing database details**: when you download the files of this software you will be get a file `database_details.py`.
                 In this file you need to change these details according to your database that you have created on your system:
<br><br>`file: database_details.py`
   ```
   class DatabaseDetails:
      def __init__(self):
          self.host='localhost'               #change it according your host name 
          self.user='root'                    #change it according your host username
          self.password='admin123'            #change these  passwords according yours 
          self.database='raw'                 #change the name of database 
   ```

3. **table**: In the next step you need to to open and run the file 'table.py' that help to create all required tables.

4. **Change Images paths**: In the file `phone.py`, update the paths of the image files to ensure the application displays the interface correctly and maintains a better visual appearance. You need to modify the image paths at the `line numbers: 17`.

## How to use
1. Run the `phone.py ` file in a your system.
2. for inserting new contact fill the all details carefully and click on add button.
3. same as you can perform more operations like update, delete, and search.
## Contact
- **Email:** pradhanmeena7778@gmail.com  
- **Phone:** +91 6376244866
