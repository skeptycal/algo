import sys
import fileinput



sys.stdout.writelines(line.replace('\r', '\n') for line in fileinput.input(mode='rU'))"
