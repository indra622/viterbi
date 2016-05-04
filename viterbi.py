#viterbi.py

f = open("train.txt")



pos_count = dict()
pos_list = list()
morpheme_count = list()



train_readlines = f.readlines()
#pos_count
for line in train_readlines:
	if line == "\n":
		continue
	
	morphemes = line.split("\t")[1][:-2]

	

	for i in morphemes.split("+"):
		morpheme_count.append(i)

	for i in morpheme_count:
		pos = i[i.rfind("/")+1:]
		# print pos
		if pos_count.has_key(pos)==False:
			pos_count[pos]=0
		pos_count[pos] += 1


print pos_count

transition_prob = [[0 for col in range(pos_count.keys().size())] for row in range(pos_count.keys().size())]

for line in train_readlines:
	if line == "\n":
		continue
	
	morphemes = line.split("\t")[1][:-2]

	transition_count = list()

 	for i in morphemes.split("+"):
 		transition_count.append(i)

 	for i in transition_count:

		pos_list.append(i[i.rfind("/")+1:])


	for i in range(pos_list.size()):
		if i == 0:
			transition_prob = pos_count[pos_list[i-1]]
		else:
			



		
		



	

		
	for key in morpheme_count:
		i = key.split("/")[1]
		if(pos_count.has_key(i)==False):
			pos_count[i] = 0
		
		pos_count[i] += 1
		
	print pos_count
