Input/Output
Learning Objectives
How to open a file
How to write text in a file
How to read the full content of a file
How to read a file line by line
How to move the cursor in a file
How to make sure a file is closed after using it
What is and how to use the with statement
What is JSON
What is serialization
What is deserialization
How to convert a Python data structure to a JSON string
How to convert a JSON string to a Python data structure
Tasks
Read file
Write a function that reads a text file (UTF8) and prints it to stdout:

Prototype: def read_file(filename=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
Solution: 0-read_file.py

$ amonkeyprogrammer@ubuntu:~/0x0B$ cat 0-main.py
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

$ amonkeyprogrammer@ubuntu:~/0x0B$ cat my_file_0.txt
Holberton School offers a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
$ amonkeyprogrammer@ubuntu:~/0x0B$ ./0-main.py
Holberton School offers a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
$ amonkeyprogrammer@ubuntu:~/0x0B$
Number of lines
Write a function that returns the number of lines of a text file:

Prototype: def number_of_lines(filename=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
Solution: 1-number_of_lines.py

$ amonkeyprogrammer@ubuntu:~/0x0B$ cat 1-main.py
#!/usr/bin/python3
number_of_lines = __import__('1-number_of_lines').number_of_lines

filename = "my_file_0.txt"
nb_lines = number_of_lines(filename)
print("{} has {:d} lines".format(filename, nb_lines))

$ amonkeyprogrammer@ubuntu:~/0x0B$ wc -l my_file_0.txt
4 my_file_0.txt
$ amonkeyprogrammer@ubuntu:~/0x0B$ ./1-main.py
my_file_0.txt has 4 lines
$ amonkeyprogrammer@ubuntu:~/0x0B$
Read n lines
Write a function that reads n lines of a text file (UTF8) and prints it to stdout:

Prototype: def read_lines(filename="", nb_lines=0):
Read the entire file if nb_lines is lower or equal to 0 OR greater or equal to the total number of lines of the file
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
Solution: 2-read_lines.py

$ amonkeyprogrammer@ubuntu:~/0x0B$ cat 2-main.py
#!/usr/bin/python3
read_lines = __import__('2-read_lines').read_lines

print("1 line:")
read_lines("my_file_0.txt", 1)
print("--")
print("3 lines:")
read_lines("my_file_0.txt", 3)
print("--")
print("Full content:")
read_lines("my_file_0.txt")

$ amonkeyprogrammer@ubuntu:~/0x0B$ cat my_file_0.txt
Holberton School offers a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
$ amonkeyprogrammer@ubuntu:~/0x0B$ ./2-main.py
1 line:
Holberton School offers a truly innovative approach to education:
--
3 lines:
Holberton School offers a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

--
Full content:
Holberton School offers a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
$ amonkeyprogrammer@ubuntu:~/0x0B$
Write to a file
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

Prototype: def write_file(filename="", text=""):
You must use the with statement
You don’t need to manage file permission exceptions.
Your function should create the file if doesn’t exist.
Your function should overwrite the content of the file if it already exists.
You are not allowed to import any module
Solution: 3-write_file.py

$ amonkeyprogrammer@ubuntu:~/0x0B$ cat 3-main.py
#!/usr/bin/python3
write_file = __import__('3-write_file').write_file

nb_characters = write_file("my_first_file.txt", "Holberton School is so cool!\n")
print(nb_characters)

$ amonkeyprogrammer@ubuntu:~/0x0B$ ./3-main.py
29
$ amonkeyprogrammer@ubuntu:~/0x0B$ cat my_first_file.txt
Holberton School is so cool!
$ amonkeyprogrammer@ubuntu:~/0x0B$
Append to a file
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

Prototype: def append_write(filename="", text=""):
If the file doesn’t exist, it should be created
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
Solution: 4-append_write.py

$ amonkeyprogrammer@ubuntu:~/0x0B$ cat 4-main.py
#!/usr/bin/python3
append_write = __import__('4-append_write').append_write

nb_characters_added = append_write("file_append.txt", "Holberton School is so cool!\n")
print(nb_characters_added)

$ amonkeyprogrammer@ubuntu:~/0x0B$ cat file_append.txt
cat: file_append.txt: No such file or directory
$ amonkeyprogrammer@ubuntu:~/0x0B$ ./4-main.py
29
$ amonkeyprogrammer@ubuntu:~/0x0B$ cat file_append.txt
Holberton School is so cool!
$ amonkeyprogrammer@ubuntu:~/0x0B$ ./4-main.py
29
$ amonkeyprogrammer@ubuntu:~/0x0B$ cat file_append.txt
Holberton School is so cool!
Holberton School is so cool!
$ amonkeyprogrammer@ubuntu:~/0x0B$
To JSON string
Write a function that returns the JSON representation of an object (string):

Prototype: def to_json_string(my_obj):
You don’t need to manage exceptions if the object can’t be serialized.
Solution: 5-to_json_string.py

$ amonkeyprogrammer@ubuntu:~/0x0B$ cat 5-main.py
#!/usr/bin/python3
to_json_string = __import__('5-to_json_string').to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))

try:
    my_set = { 132, 3 }
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

$ amonkeyprogrammer@ubuntu:~/0x0B$ ./5-main.py
[1, 2, 3]
<class 'str'>
{"id": 12, "is_active": true, "name": "John", "info": {"average": 3.14, "age": 36}, "places": ["San Francisco", "Tokyo"]}
<class 'str'>
[TypeError] {3, 132} is not JSON serializable
$ amonkeyprogrammer@ubuntu:~/0x0B$
