#!/bin/bash

pip install -r requirements.txt

# Build CSS
cd theme/static_src
npm install
npm run build
cd ../..

python manage.py collectstatic --noinput
