# Homework 1
## Create a simple calculator that performs arithmetic operations: addition, subtraction, multiplication, and division
### If you're experiencing issues, make sure that your script has executable permissions. You can use the chmod command to assign execution permissions:
#### chmod +x calculator.py
### If you are having an error:
#### /usr/bin/env: ‘python3\r’: No such file or directory
#### /usr/bin/env: use -[v]S to pass options in shebang lines

#### This error occurs due to the presence of a carriage return (CR, '\r') character in your shebang, which is not recognized by the operating system. To fix this error, you need to remove the carriage return character from the shebang.
#### You can use the dos2unix utility to remove the carriage return characters from the script file. If you don't have this utility installed on your system, you'll need to install it. Here's how you can do it:

#### Install dos2unix on Linux using the following command:

#### sudo apt-get install dos2unix
#### If you're using a different Linux distribution, use the corresponding package installation command for your system.

#### Run dos2unix to remove the carriage return characters from the script file:

#### dos2unix calculator.py
#### This command will overwrite the calculator.py file, removing the carriage return characters.

#### Now you can re-run your script, and the carriage return error should be resolved:
#### ./calculator.py
