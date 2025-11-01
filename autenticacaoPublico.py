import pyrebase

firebase_config = {
    "apiKey": "",            # coloque aqui a sua apiKey
    "authDomain": "",        # coloque aqui o seu authDomain
    "projectId": "",         # coloque aqui o seu projectId
    "storageBucket": "",     # coloque aqui o seu storageBucket
    "messagingSenderId": "", # coloque aqui o seu messagingSenderId
    "appId": "",             # coloque aqui o seu appId
    "measurementId": "",     # coloque aqui o seu measurementId
    "databaseURL": ""        # coloque aqui o seu databaseURL
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def criar_usuario(email: str, senha: str):
    '''Cria usuário no firebase auth (email/senha).'''

    user = auth.create_user_with_email_and_password(email, senha) # senha é salva com o hash criptográfico
    auth.send_email_verification(user["idToken"])                 # é enviado um email com um link de verificação
    return user

def login(email: str, senha: str):
    '''Faz o login e retorna token/id do usuário'''

    user = auth.sign_in_with_email_and_password(email, senha) 
    user = auth.refresh(user["refreshToken"]) #atualiza idToken usando refreshToken 
    return user

def info_da_conta(id_token: str):
    '''Obtém infos da conta a partir do token'''
    return auth.get_account_info(id_token)

def login_ou_signin(email, senha):
    acao = input('(c) criar | (l) login\n').lower().strip()

    if acao == 'c':
        u = criar_usuario(email, senha)
        print('Usuário criado, verifique seu e-mail para confirmação.')
        print(u)
        return 'c'

    elif acao == 'l':
        u = login(email, senha)
        print('Usuário e senha corretos.')
        return 'l'
    
    else:
        print('Ação inválida.')
        return None