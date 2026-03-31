# Ambiente virtual = Suponha que temos uma biblioteca de um banco de dados instalada na versao 3.0 e usada em um projeto. Depois, vamos trabalhar em um outro projeto, que tambem precisa de um banco de dados, e dessa vez a biblioteca está na versao 4.0 com novas funcionalidades e modos de usar. Se essa biblioteca estiver instalada diretamente na máquina, o projeto antigo na versão anterior pode acabar com um erro, pois pode não existir funções que foram usadas pra versão anterior. E para resolver isso, usamos ambientes virtuais. Para criar um novo ambiente virtual, digitamos no terminal, ou cmd, o seguinte codigo, 'py -m venv venv', isto apenas para criar esse ambiente. Para ativar, nós vamos digitar o seguinte comando 'venv\Scripts\activate' direto no prompt de comando. Caso esteja usando o powershell, use o comando '.\venv\Scripts\activate'

# Bibliotecas Globais: Estao no pc e funcionam para todos os projetos

# Bibliotecas Locais: Funcionam apenas pro projeto em especifico, toda biblioteca instalada dentro do venv será usada apenas para o projeto em específico

# Para desativar o ambiente virtual, basta digitar o comando 'deactivate' 


# Junto do python, vem instalado um carinha chamado 'pip', que é um gerenciador de pacotes, ele vai gerir as bibliotecas internas dentro do seu programa.

# Para instalar uma biblioteca com o pip utilizamos o comando no terminal 'pip install 'nome da biblioteca''
# Para desinstalar, basta utilizar 'pip uninstall 'nome da biblioteca''
# Utilize o site 'pypi.org' para encontrar novas bibliotecas

