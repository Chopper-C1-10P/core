echo "Pulling from remote..."
git pull origin master
echo "Updating requirements.txt..."
pipreqs --force
echo "Running main.py..."
python3 K-2SO/main.py
