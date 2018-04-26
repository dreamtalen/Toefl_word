from six.moves import input
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

	print("----------------------  Usage  ----------------------")
	print("Choose the one which is the synonym of given word.\n")
	print("Enter 1, 2, 3, or 4 to provide your answer, or enter")
	print("ENTER to get result directly if you don't know what")
	print("the given word means.\n")
	print("Enter q to exit.")
	print("-----------------------------------------------------")

	quit_flag = False
	while True:
		if quit_flag:
			break
		pick_one = random.choice(word_list)
		print(">>> " + pick_one)
		choice_list = random.sample(answer_list, 3)
		choice_list.append(word_dict[pick_one])
		random.shuffle(choice_list)
		print(choice_list)

		while True:
			user_answer = input("Answer? >>>")
			if user_answer == 'q':
				quit_flag = True
				break
			if user_answer.isdigit():
				user_answer = int(user_answer)
				if choice_list[user_answer - 1] == word_dict[pick_one]:
					print("[Correct!]")
				else:
					print("[Wrong] Answer is: ", word_dict[pick_one])
					wrong_list.append(pick_one)
				break
			elif not user_answer:
				print("[Wrong] Answer is: ", word_dict[pick_one])
				wrong_list.append(pick_one)
				break
			else:
				user_answer = input(
					"[Warning] Answer should in [1, 2, 3, 4]! Retry >>>")
		print("")

	with open('wrong_note.db', 'a') as f:
		to_write = [w + ' ' + word_dict[w] + '\n' for w in wrong_list]
		f.writelines(to_write)
	print("Wrong answers has been saved in ./wrong_note.db")

if __name__ == '__main__':
	main()
