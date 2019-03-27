#! /bin/bash

#A
coverage run --source='.' /Users/student/Documents/djangogirls/manage.py test -v2 $1 2>&1 | ansi2html -m > TestResults.html
# -m = surround lines with <span id='line-n'>..</span>

coverage report -m | ansi2html -m > coverage.html
