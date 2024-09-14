from django.shortcuts import render

def index(request):
        return render(request, 'index.html')

def criptografar(request):
    if request.method == 'POST':
        texto = request.POST.get('texto', '')  # Pega o texto enviado no formulário
        criptografado = criptografar_texto(texto)  # Criptografa o texto
        return render(request, 'criptografar.html', {'resultado': criptografado})  # Retorna o resultado
    return render(request, 'criptografar.html')

def descriptografar(request):
    if request.method == 'POST':
        texto = request.POST.get('texto', '')  # Pega o texto criptografado enviado no formulário
        descriptografado = descriptografar_texto(texto)  # Descriptografa o texto
        return render(request, 'descriptografar.html', {'resultado': descriptografado})  # Retorna o resultado descriptografado
    return render(request, 'descriptografar.html')

# Função que realiza a criptografia
def criptografar_texto(texto):
    # Definindo o alfabeto para referência
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Variável que vai armazenar o resultado criptografado
    resultado = ''

    for letra in texto.upper():
        if letra in alfabeto:  # Verifica se a letra faz parte do alfabeto
            indice_atual = alfabeto.index(letra)  # Encontra a posição da letra no alfabeto
            
            if letra in 'AEIOU':  
                novo_indice = (indice_atual + 6) % 26
            else:
                novo_indice = (indice_atual + 6) % 26
            
            # Adiciona a nova letra ao resultado
            resultado += alfabeto[novo_indice]
        else:
            # Se o caractere não for uma letra, adiciona o caractere original (por exemplo, espaços ou pontuações)
            resultado += letra

    return resultado  # Retorna o texto criptografado

# Função que realiza a descriptografia
def descriptografar_texto(texto):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resultado = ''

    for letra in texto.upper():
        if letra in alfabeto:  # Verifica se a letra faz parte do alfabeto
            indice_atual = alfabeto.index(letra)  # Encontra a posição da letra no alfabeto
            
            if letra in 'AEIOU':
                novo_indice = (indice_atual - 6) % 26
            else:
                novo_indice = (indice_atual - 6) % 26
            
            # Adiciona a nova letra ao resultado
            resultado += alfabeto[novo_indice]
        else:
            # Se o caractere não for uma letra, adiciona o caractere original (por exemplo, espaços ou pontuações)
            resultado += letra

    return resultado  # Retorna o texto descriptografado
