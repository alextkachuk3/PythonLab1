from metro import Metro
from metro_line import MetroLine

test = Metro()

test.add_line(MetroLine("l1", 'blue'))
test.add_line(MetroLine("l3", 'green'))
test.add_line(MetroLine("l2", 'red'))

# test.delete_line(3)

test.update_color("l3", 'pink')
print('end')