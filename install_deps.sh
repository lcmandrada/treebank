# stanford parser
sudo apt install default-jdk
cd treebank/stanford
wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-10-05.zip
unzip stanford-corenlp-full-2018-10-05.zip

# pocketsphinx
sudo apt -y install python-augeas3 gcc swig dialog libpulse-dev libasound2-dev

# pydub
sudo apt -y install ffmpeg

# convert
sudo apt -y install imagemagick
# sudo vi /etc/ImageMagick-7/policy.xml
# <policy domain="coder" rights="read | write" pattern="PS" />

# mongodb
sudo apt -y install mongodb
sudo systemctl enable mongodb
sudo systemctl start mongodb

# pip deps
pip install -r requirements.txt

# nltk deps
python download_ntlk_deps.py