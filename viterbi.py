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

	#start pos
	if pos_count.has_key("#")==False:
			pos_count["#"]=0

	pos_count["#"] +=1
	# print 'd'


print pos_count

transition_prob = dict()

# for transition probability
for line in train_readlines:
	if line == "\n":
		continue
	
	morphemes = line.split("\t")[1][:-2]

	transition_count = list()

 	for i in morphemes.split("+"):
 		transition_count.append(i)

 	for i in transition_count:

		pos_list.append(i[i.rfind("/")+1:])

	temp = 0 # for previous

	for key in pos_list:
		#print temp
		if temp == 0:
			transition_prob["#"] = dict()
			transition_prob["#"][key] = pos_count[key] / (pos_count["#"] * len(pos_count.keys()))
			
		else:
			transition_prob[temp] = dict()
			transition_prob[temp][key] = pos_count[key] / (pos_count[temp] * len(pos_count.keys()))

		temp = key


# for observation probability

# for line in train_readlines:
# 	if line == "\n":
# 		continue

# 	morphemes = line.split("\t")[1][:-2]

# 	observation_count = list()

#  	for i in morphemes.split("+"):
#  		observation_count.append(i)

#  	for i in observation_count:
