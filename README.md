# FastAPI_Vue_WebSocket_Chat

There is no strict registration in the chat. There is one conversation for all.

## Installation

1. Creating virtual environments:

Use the package manager [pip](https://pypi.org/project/pip/) to install virtual environments.

```bash
sudo pip install virtualenv
```

```bash
cd /you_project
```

```bash
virtualenv venv --python=python3.8
```

2. Activation virtual environments:

```bash
source venv/bin/activate
```

3. Loading the repository:

```bash
git clone https://github.com/Hamersly/FastAPI_Vue_WebSocket_Chat.git
```

```bash
cd /FastAPI_Vue_Socket_Chat
```

4. Installing packages:

```bash
pip install -r requirements.txt
```

5. Run:

```bash
python uvicorn main:app --reload
```
## Important

Specify the required address of WebSocket in the file 'index.html'.
