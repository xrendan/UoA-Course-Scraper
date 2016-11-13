#!/bin/sh

echo "deleting database file if it exists"
if [ -f course_listings.sqlite ]
    then
        rm course_listings.sqlite
fi

echo "creating databases file"
python create_db.py
python update_db.py
echo "You need to run parser.py to fetch data"
