import gkeepapi, os
import os


dir_path = os.environ['NOTES_PATH'] if 'NOTES_PATH' in os.environ else input('Path to plain text notes to import: ')
username = os.environ['KEEP_USERNAME'] if 'KEEP_USERNAME' in os.environ else input('Google Username: ')
password = os.environ['KEEP_PASSWORD'] if 'KEEP_PASSWORD' in os.environ else input('Google Password: ')

keep = gkeepapi.Keep()
success = keep.login(username,password)

for file in os.listdir(dir_path):
	if os.path.isfile(dir_path + file) and file.endswith('.txt'):
		try:
			with open(dir_path + file, 'r') as mf:
				data=mf.read()
				print('Creating file:', file)
				note = keep.createNote(file.replace('.txt', ''), data)
				keep.sync();
				# TODO: automatically create and import labels from @ and # symbols
				# note.labels.add('imported')
				# keep.sync();
				print('sync')
		except Exception as e:
			print('Error:', str(e), 'file: ', file)
