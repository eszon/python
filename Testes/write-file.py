# Create and writing on txt files (modo 'w')

file = open('index.html', 'w')
file.write('''
    <!DOCTYPE html>
<html>
  <head>
    <title>Mirror Fashion</title>
    <meta charset="utf-8"/>
  </head>
  <body>
    <h1>Mirror Fashion.</h1>
    <h2>Bem-vindo à Mirror Fashion, sua loja de roupas e acessórios.</h2>
    <ul>
      <li>Confira nossas promoções.</li>
      <li>Receba informações sobre nossos lançamentos por email.</li>
      <li>Navegue por todos nossos produtos em catálogo.</li>
      <li>Compre sem sair de casa.</li>
    </ul>
  </body>
</html>    
    ''')
file.close()

#Read create file

file = open('index.html', 'r')
for line in file:
    line = line.rstrip()
    print(line)
file.close()