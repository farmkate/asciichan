#ex15.py

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input ("> ")

txt_again = open(file_again)

print txt_again.read()


#create a test file at command prompt
# echo "Test file thing" > ex15_sample.txt
# cat ex15_sample.txt /displays contents of file/


#to change the contents of a txt file
# vim test.txt
