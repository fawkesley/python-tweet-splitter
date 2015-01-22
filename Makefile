.PHONY: test
test:
	nosetests
	flake8 --exclude='./tweetsplitter/__init__.py' .
