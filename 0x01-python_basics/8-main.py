#!/usr/bin/python3
common_elements = __import__('8-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Python", "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
