rm -rf install
mkdir install
pip install -r requirements.txt -t ./install/

cp *.py ./install/
cp *.json ./install/
cd install
