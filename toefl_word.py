import random
def main():
	word_list, answer_list, word_dict, wrong_list = [], [], {}, []
	with open('word.db') as f:
		for line in f.readlines():
			line_list = line.strip().split()
			if len(line_list) < 2:
				pass
			else:
				word = line_list[0]
				answer = ' '.join(line_list[1:])
				word_dict[word] = answer
				word_list.append(word)
				answer_list.append(answer)
	flag = 1
	while flag:
		user_input = raw_input('Pick one?')
		if user_input == 'q': flag = 0
		else:
			pick_one = random.choice(word_list)
			print '>>> '+pick_one
			choice_list = random.sample(answer_list, 3)
			choice_list.append(word_dict[pick_one])
			random.shuffle(choice_list)
			print choice_list
			try:
				user_answer = input('>>> Answer?')
			except:
				user_answer = input('>>> Input error, Answer?')
			if choice_list[user_answer-1] == word_dict[pick_one]:
				print 'Correct'
			else:
				print "Wrong, answer is: ", word_dict[pick_one]
				wrong_list.append(pick_one)
	with open('wrong_note.db', 'a') as f:
		to_write = [w + ' ' + word_dict[w] + '\n' for w in wrong_list]
		f.writelines(to_write)

if __name__ == '__main__':
	main()