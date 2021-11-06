
try:
   fhand = open('mailbox.txt')
except:
   print('File cannot be opened')
   exit()

lines=fhand.readlines()
new_list=[]
bibon=open('output.txt', 'w')
for line in lines:
   ind=line.find('[')
   en_ind=line.find(']')
   if line.startswith('Received: from') and 'unix' not in line[ind:en_ind]:
      word=line[ind+1:en_ind]
      if word not in new_list:
         new_list.append(word)
         new_list.sort()
for item in new_list:
   print(item)
   bibon.write(item)
   bibon.write('\n')
fhand.close()
               
