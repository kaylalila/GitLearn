from die import Die
import pygal

die = Die()
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frenquencies = []
for value in range(1, die.num_sides + 1):
    frequancy = results.count(value)
    frenquencies.append(frequancy)
print(frenquencies)

hist = pygal.Bar()
hist_title = "Results of rolling a D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Numbers"
hist.y_title = "Frequency"
hist.add('D6', frenquencies)
hist.render_to_file('die_visual.svg')

