import sys
pf = open('/home/priyanshu/Documents/config/alacritty.yml','r')
sp = pf.read()
oso = '/home/priyanshu/Documents/cp/output.txt'
sys.stdout = open(oso , 'w')
