#!/bin/sh

./create_db.sh

python parser.py
python parsePrograms.py
python dependencyFinder.py

echo "rebuilt"
