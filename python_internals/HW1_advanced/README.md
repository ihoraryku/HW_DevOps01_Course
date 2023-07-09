# Homework 2
## Generate a random password consisting of a combination of uppercase letters, lowercase letters, numbers, and special characters. Ensure that the generated password meets the following criteria:
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one number
- Contains at least one special character (e.g., !, @, #, $, %, etc.)
- Display the generated password to the user.

### If you're experiencing issues, make sure that your script has executable permissions. You can use the chmod command to assign execution permissions:
```
chmod +x calculator.py
```
### If you are having an error, like:
```
/usr/bin/env: ‘python3\r’: No such file or directory
/usr/bin/env: use -[v]S to pass options in shebang lines
```

#### This error occurs due to the presence of a carriage return (CR, '\r') character in your shebang, which is not recognized by the operating system. To fix this error, you need to remove the carriage return character from the shebang.
#### You can use the dos2unix utility to remove the carriage return characters from the script file. If you don't have this utility installed on your system, you'll need to install it. Here's how you can do it:

#### Install dos2unix on Linux using the following command:

```
sudo apt-get install dos2unix
```
#### If you're using a different Linux distribution, use the corresponding package installation command for your system.

#### Run dos2unix to remove the carriage return characters from the script file:

```
dos2unix password_generator.py
```
#### This command will overwrite the `password_generator.py` file, removing the carriage return characters.

#### Now you can re-run your script, and the carriage return error should be resolved:
```
./password_generator.py
```
#### To run the script you need to install the `pyperclip` package, use the command:
```
pip install pyperclip
```
or
```
pip install -r requirements.txt
```

