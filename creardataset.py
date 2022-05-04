from random import randint

file = open("dataset.csv", "w")
file.write("Peso")

for i in range(100):
  num = randint(100,200)
  file.write("\n{}".format(num))

file.close()