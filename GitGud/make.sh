git init ctf
cd ctf
cp ../v1/* .
cp ../v1/.env .
git add .
git commit -m "initial commit"
cp ../v2/* .
cp ../v2/.gitignore .
git add .
git rm .env
git commit -m "quick fix"
