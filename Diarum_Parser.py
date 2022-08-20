import csv
from pathlib import Path

def substring_index(list, substr):
	for i, s in enumerate(list):
		if substr in s:
			return i
	return -1

with open('data.csv', 'w', newline='') as f:
	csv_writer = csv.writer(f)

	csv_writer.writerow(["Content", "Date"])

	path_list = Path('.').glob('Entries/*.txt')

	for path in path_list:
		with open(str(path), 'r') as g:
			lines = g.read().splitlines()
			lines = [x for x in lines if x]
			row = []
			metadata_indices = [substring_index(lines, 'Tags:'), substring_index(lines, 'People:'), substring_index(lines, 'Tracker:')]
			entry_last_line = min([x for x in metadata_indices if x!=-1] + [len(lines)])
			row.append('\n'.join(lines[i] for i in range(1, entry_last_line)))
			row.append(lines[0])
			csv_writer.writerow(row)

