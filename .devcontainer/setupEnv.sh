#!/bin/sh

echo "Pull latest code for the current branch"
git fetch
git pull

set -e

echo "Setting up Backend..."
cd ./backend
pip install -r requirements.txt
cd ../

echo "Setting up Frontend..."
cd ./frontend
npm install
cd ../

echo "Setup complete! 🎉"
