# .travis.yml
config = """
language: python
python:
  - "2.7"
  - "3.7"   
    # Versões do Pypy  
  - "pypy"
  - "pypy3"

# Comando para instalar as dependências
install:
  - pip install -r requirements.txt

stages:
  - name: Test
  - name: Deploy  

# Comando para rodar os testes utilizando o pytest
script: pytest

jobs:
  include:
    - stage: Test
      name: Unit Tests
      script: pytest
    - stage: Deploy
      name: Heroku Deploy
      script: /bin/true
      deploy:
        provider: heroku
        api_key: 
        run: "python3 manage.py migrate"  

"""
