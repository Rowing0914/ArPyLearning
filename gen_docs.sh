echo "CLEANING DIRECTORY: docs, publish"
rm -rf ./docs/* && rm -rf ./publish/* && mkdir docs publish
echo "INIITIALISE SPHINX"
sphinx-apidoc -F -o ./docs/ ./src/
echo "MODIFY conf.py IN docs"
sed '15 s/^# //' ./docs/conf.py | tee ./docs/temp.py
mv ./docs/temp.py ./docs/conf.py
sed '16 s/^# //' ./docs/conf.py | tee ./docs/temp.py
mv ./docs/temp.py ./docs/conf.py
sed '17 s/^# //' ./docs/conf.py | tee ./docs/temp.py
mv ./docs/temp.py ./docs/conf.py
echo "GENERATE DOCUMENTS"
sphinx-build -a ./docs/ ./publish/
