# README - Instructions to Use

Details:
# **Generating the necessary packages to run the API - Requirements**
- To generate the file with the requirements.txt type at the prompt: 
```
pip freeze > requirements.txt
```
Source: 'https://dicasdepython.com.br/como-criar-uma-virtual-env-e-um-arquivo-de-requirementstxt-no-python/#:~:text=Para%20criarmos%20o%20arquivo%20requirements,as%20versões%20que%20foram%20utilizadas.'

# **Installing the necessary packages to run the API - Requirements**
To install all packages contained in the requirements.txt file, type at the prompt: 
```
pip install -r requirements.txt
```
Source: 'https://dicasdepython.com.br/como-criar-uma-virtual-env-e-um-arquivo-de-requirementstxt-no-python/#:~:text=Para%20criarmos%20o%20arquivo%20requirements,as%20versões%20que%20foram%20utilizadas.'

# **Enabling the Virtual Env Virtual Environment**
- Type at the prompt: 
```
python3 -m venv venv
```
- Run the file 'activate' which is in the directory 
```
venv/bin/activate (#if on Linux).
```
- In Windows, the command is a little different, being necessary to execute the file activate.bat, that way the command to activate the venv on windows it would be venv\Scripts\activate.bat
- Once activated, it will indicate that the venv is activated.
- To disable, type at the prompt:
```
deactivate
```

# **Structure and organization of files in Flask and Flask-Admin**
Source: 'https://huogerac.hashnode.dev/estrutura-e-organizacao-de-pastas-em-projetos-flask'

