cat .env | xargs -I {} export {}

python main.py