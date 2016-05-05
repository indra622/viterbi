#viterbi.py

f = open("train.txt")



pos_count = dict()
pos_list = list()
morpheme_count = list()
observ_list = list()




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

transition_dict = dict()
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

	temp = '' # for previous

	for key in pos_list:
		#print temp


		if temp == '':
			transition_dict["#"] = dict()
			transition_dict["#"][key] = 0
			
		else:
			
			if transition_dict.has_key(temp):
				
				pass
			else:
				
				transition_dict[temp] = dict()

			if transition_dict[temp].has_key(key):
				
				pass
			
			else:

				transition_dict[temp][key] = 0

		temp = key


	temp1 = ''

	for key in pos_list:
		#print temp
		if temp1 == '':
			transition_dict["#"][key] += 1
			
		else:

			transition_dict[temp1][key] += 1

		temp1 = key

	for i in transition_dict:
		for j in transition_dict[i]:
			transition_prob[i] = dict()
			transition_prob[i][j]= float(transition_dict[i][j]) / float(pos_count[i])

print transition_prob

observation_dict = dict()
observation_prob = dict()

for line in train_readlines:
	if line == "\n":
		continue
	
	morphemes = line.split("\t")[1][:-2]

	observation_count = list()

 	for i in morphemes.split("+"):
 		observation_count.append(i)

 	for i in observation_count:

		word = i[:i.rfind("/")]
		pos = i[i.rfind("/")+1:]

		if observation_dict.has_key(word):
			pass
		else:
			observation_dict[word] = dict()

		if observation_dict[word].has_key(pos):
				pass
		else:
			observation_dict[word][pos] = 0
		
	for i in observation_count:

		word = i[:i.rfind("/")]
		pos = i[i.rfind("/")+1:]

		observation_dict[word][pos] += 1

	for i in observation_dict:
		for j in observation_dict[i]:
			observation_prob[i] = dict()
			observation_prob[i][j]= float(observation_dict[i][j]) / float(pos_count[j])

print observation_prob
