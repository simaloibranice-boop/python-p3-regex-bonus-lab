import re

my_pattern = r"^[ \t]*([A-Za-z \t'?!\.,]*day[A-Za-z \t'?!\.,]*[\.?])[ \t]*$"
my_regex = re.compile(my_pattern, re.MULTILINE)
