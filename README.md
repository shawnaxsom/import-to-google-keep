# Import Text Notes to Google Keep

## Usage

Install gkeepapi using the requirements.txt:

```
pip install -r requirements.txt
```

Run the app:

```
python import-to-google-keep.py
```

The app will prompt you for Google Keep (Google) credentials and folder path of the text files.

You can also use environment variables, though entering passwords on the command line isn't best practice:

```
KEEP_USERNAME=username KEEP_PASSWORD=password NOTES_PATH= '/Users/shawnaxsom/Dropbox/note-taking/notes/' python import-to-google-keep.py
```

