import autenticacaoPublico 
import smtplib
import random
import datetime
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

codigo_temporario = {}

def gerar_codigo_verificacao():
    digitos = string.digits
    codigo = ''.join(random.choice(digitos) for i in range(6))
    tempo_expirar = datetime.datetime.now() + datetime.timedelta(minutes=10)
    codigo_temporario[codigo] = tempo_expirar
    return f'Código: {codigo} – NÃO COMPPARTILHAR!\nVálido até {tempo_expirar}'

def verificar_codigo(codigo_inserido):
    if codigo_inserido in codigo_temporario:
        expirar = codigo_temporario[codigo_inserido]
        agora = datetime.datetime.now()
        if agora < expirar:
            print('\n\nVerificação: Sucesso.\n\nBEM VINDO(A)!')
            return True
        else:
            print('\n\nVerificação: Acesso negado – Código expirado.')
            del codigo_temporario[codigo_inserido]
            return False
    else:
        print(f'\n\nVerificação: Acesso negado – Código inválido.')
        return False


def enviar_email_2FA(email):

    server = "smtp.gmail.com"
    port = 587
    username = ""                          # seu email que irá enviar o código
    password = ""                          # sua senha de aplicativo (criada a partir do seu email)
    mail_from = ""                         # seu email que irá enviar o código
    mail_to = email                        # é o email que o usuário inserir no login
    mail_subject = "Código de verificação" # assunto do email
    mail_body = gerar_codigo_verificacao() # conteúdo do email

    mensagem = MIMEMultipart()
    mensagem['From'] = mail_from
    mensagem['To'] = mail_to
    mensagem['Subject'] = mail_subject
    mensagem.attach(MIMEText(mail_body, 'plain'))

    connection = smtplib.SMTP(server, port)
    connection.starttls()
    connection.login(username,password)
    connection.send_message(mensagem)
    connection.quit()

def menu_login_signin(email, senha):
    return autenticacaoPublico.login_ou_signin(email, senha) # roda o código do outro arquivo


print('\n\nBem vindo(a) ao Banco de Tóquio!\n\n')
print('- - - Login/Sign in - - -\n\n')

email = input('E-mail: ').strip()
senha = input('\nSenha: ').strip()
acao = menu_login_signin(email, senha)

# manda o código de verificação de duas etapas para o login
if acao == 'l':
    gerar_codigo_verificacao()
    enviar_email_2FA(email)
    codigo_inserido = input('\n\nInsira o código enviado para o seu email: ').strip()
    verificar_codigo(codigo_inserido)
