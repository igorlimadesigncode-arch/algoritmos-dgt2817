# Microatividade 6: Funções com argumentos

def loginUsuario(perfil):
    # Converte para minúsculas para garantir a comparação correta independente de como foi digitado
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Testes
loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')