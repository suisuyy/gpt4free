export PY_VERSIION='3.10.4'  #set py version,gpt4free need python <3.11 currently

sudo apt update; sudo apt install -y build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

sudo apt install -y htop aria2

curl https://pyenv.run | bash

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile

. ~/.bash_profile

pyenv install $PY_VERSIION
pyenv versions
pyenv global $PY_VERSIION
python --version

pip install -r requirements.txt
 pip install -r interference/requirements.txt

python3 -m interference.app















