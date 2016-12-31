
file_name = 'studentdata.txt'


#Using the text file studentdata.txt write a program that prints out the names of
#students that have more than six quiz scores

infile = open(file_name, 'r')
print('Students with more than 6 scores')
for aline in infile:
    items = aline.split()
    if len(items) > 7:
        print(items[0])

infile.close()

infile = open(file_name, 'r')

#average scores
print('Average Scores')
for aline in infile:
    items = aline.split()
    count = 0
    sum = 0
    for score in items:
        if score.isdigit():
            count +=1
            sum = sum + int(score)
    print(str((sum//count)) + ', ' + items[0])


infile.close()

#min/max scores
infile = open(file_name, 'r')
print('Min/Max Scores')
for aline in infile:
    items = aline.split()
    min = items[1]
    max = items[1]
    for score in items:
        if score.isdigit():
            if score > max:
                max = score
            if score < min:
                min = score
    print('Min: ' + str(min) + '  Max: ' + str(max) + ', ' + items[0])


infile.close()

file_name = 'labdata.txt'
infile = open(file_name, 'r')
print("Labdata")
for aline in infile:
    coordinates = aline.split()
    tempX = coordinates[0]
    tempY = coordinates[1]
    plotter = Turtle.turtle()
