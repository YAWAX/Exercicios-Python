palavras  = ("Aprender", "Programar", "linguagem", "Python",
"Curso", "gratis", "estudar", "Praticar", "trabalhar", "mercador",
"programador", "futuro")

for c in palavras:
    print(f"\nNa Palavra {c.upper()} temos ", end='')
    for letra in c:
        if letra.lower() in 'aeéêiou':
            print(letra, end=' ')
