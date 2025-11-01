# Autenticação Multifator
Aqui está um pequeno programinha que eu desenvolvi em uma atividade de\
estudos com a faculdade. Achei bem interessante e prazerozs de fazer.

Resolvi tornar público pois é algo que eu acho importante para se ter
conhecimento.

## Como funciona?
No terminal, o sistema pedirá para inserir **e-mail e senha**, e em seguida perguntará\
se você deseja **criar uma conta** ou **fazer login**.

- Ao **criar a conta**, você receberá um e-mail (se o endereço for válido)com um **link de**\
**verificação**. Ao clicar nele, sua conta será ativada.
- Ao **fazer login**, o programa enviará um **código de verificação (2FA)** para o seu e-mail.\
Insira o código no terminal e, se estiver válido, o acesso será liberado.

O sistema utiliza o **Firebase Authentication** (plataforma do Google) para controlar os\
usuários cadastrados e autenticações.

No arquivo ```autenticacaoPublico.py```, você pode inserir suas **chaves de API** obtidas\
no console do Firebase para conectar seu projeto.

Além disso, é necessário **criar uma senha de app** nas configurações da sua conta Gmail\
para que o envio do código de autenticação por e-mail funcione corretamente.

O código está todo **documentado**, e contém comentários explicativos para orientar\
o que deve ser configurado ou alterado.

## Requisitos para o programa funcionar:
**Versão do python:**\
```Python 3.11 ou superior```

**Criar um ambiente virtual:**\
```python3 -m venv .venv```

**Ativar pelo MacOS/Linux:**\
```source .venv/bin/activate```

**Ativar pelo Windows powershell:**\
```.\.venv\Scripts\Activate.ps1```

**Instalar dependências:**\
```pip install -r requirements.txt```\
```pip install pyrebase4 python-dotenv```

## Configurações necessárias:
1. **Crie um projeto** no **Firebase**
- Vá em **Authentication → Sign-in method** e ative **Email/Password.**
- Em **Configurações do Projeto → Geral**, copie as chaves:\
apiKey, authDomain, projectId, storageBucket, messagingSenderId,\
appId, measurementId, databaseURL.
2. **Edite o arquivo** ```autenticacaoPublico.py``` e insira essas chaves no dicionário\
firebase_config.
3. **Crie uma senha de app do Gmail**
- Vá em **Gerenciar Conta Google → Segurança → Senhas de app**.
- Essa senha será usada nas variáveis username e password no arquivo\
```autenticacaoBancoDeToquio.py.```
