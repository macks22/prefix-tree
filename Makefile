
all: words

words:
	wget https://raw.githubusercontent.com/dwyl/english-words/master/words.txt
	python clean_words.py
