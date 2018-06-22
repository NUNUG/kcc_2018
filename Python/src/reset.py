from shutil import copyfile

print("This will clean up and reset your work to any step being taught in the class.")
print("Enter the number for the step you want to work on (Example: 1):")
desiredStep = input()

try:
	i = int(desiredStep)
except:
	i = -1

if (i < 0) or (i > 11):
	print(desiredStep + " is not a valid step number.")
else:
	if (i == 0):
		src = "../steps/globaldefense.py"
	else:
		src = "../steps/globaldefense-step" + str(i) + ".py"

	dest = "./globaldefense.py"

	copyfile(src, dest)