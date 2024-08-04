import os, datetime
patf = "..\\sky cotl footage 3"
for n, i in enumerate([x for x in os.listdir(patf) if os.path.isfile(f"{patf}\\{x}")]):
	os.system(f"move \"{patf}\\{i}\" \"{i}\"")
	os.system("git add .")
	os.system(f"git commit -m \"{datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")}\"")
	os.system("git push")
	# assert n <= 2
