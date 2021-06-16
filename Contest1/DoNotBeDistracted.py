## Quantity of days to test.
qtdTests = int(input())

for test in range(qtdTests):
	## For each day, count how many tasks were done.
	tasksOnDay = int(input())
	tasks = input()
	tasksDone = set()
	i = 0
	notDistracted = 0

	while i < tasksOnDay:
		## If the task were already done today, teacher can be suspicious.
		if tasks[i] in tasksDone:
			print("No")
			notDistracted = 1
			break
		if i + 1 < tasksOnDay and tasks[i] == tasks[i+1]:
			i += 1 ## Next task.
		else:
			tasksDone.add(tasks[i])
			i += 1 ## Next task.
				
	## Other wise, teacher CANNOT be suspicious.
	if notDistracted == 0:
		print ("Yes")