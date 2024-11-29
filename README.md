Pytest e Selenium: Automação de Testes Web

Este repositório contém uma atividade acadêmica desenvolvida para a disciplina de testes, ministrada pelo professor Érico Borgonove, visando a obtenção de nota parcial no 4º semestre.

Descrição
O projeto demonstra a integração entre o framework de testes Pytest e a ferramenta de automação Selenium para a realização de testes automatizados em aplicações web. Através de exemplos práticos, são abordadas técnicas de automação de testes de interface, incluindo navegação em páginas, interação com elementos e validação de resultados.

🚀 Começando
Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte Implantação para saber como implantar o projeto.

📋 Pré-requisitos
Antes de executar os testes, certifique-se de que as seguintes ferramentas estão instaladas em seu ambiente:

Python 3.x: Linguagem de programação utilizada para desenvolver os testes.
pip: Gerenciador de pacotes do Python.
Selenium: Biblioteca para automação de navegadores web.
Pytest: Framework para escrita e execução de testes.
Além disso, é necessário o driver correspondente ao navegador que será utilizado nos testes (por exemplo, ChromeDriver para o Google Chrome).

🔧 Instalação
Clone este repositório em seu ambiente local:


git clone https://github.com/Felipe01001/Pytest-And-Selenium.git
Instale as dependências necessárias utilizando o pip:


pip install -r requirements.txt


🌐 APIs Requerendo Chave de Acesso
Alguns testes interagem com APIs externas que exigem uma chave de acesso (API Key). Para cada uma das APIs abaixo, adicione suas respectivas chaves no arquivo de configuração ou como variáveis de ambiente:

NASA API:
Acesse a chave da NASA aqui e cole no arquivo de configuração.
Chave da API: MEY3OkcNh5Yfi4tTQVT3gsfnYcz8THvzpUqCh9t7

Receita Federal API:
Para acessar dados da Receita Federal, solicite uma chave através do portal oficial e adicione-a ao projeto.
Chave da API: efd7dfcdf8f629707f496d9ffecdb1a4557e04408f4421f63b9090965265ef2d

PMDB API:
Obtenha a chave de acesso na plataforma PMDB e configure no projeto.
Chave da API: a97bd91ab42ded2e603828674bccfa6f

⚙️ Executando os Testes
Para rodar os testes, utilize o comando:

pytest
Este comando executará todos os testes definidos no projeto.

📦 Estrutura do Projeto
A estrutura do projeto é organizada da seguinte forma:

Pytest-And-Selenium/
├── ambiente/
├── py-selenium/
├── py-test/
├── .gitignore
└── requirements.txt
ambiente/: Contém arquivos relacionados à configuração do ambiente de testes.
py-selenium/: Contém scripts e módulos específicos para a automação com Selenium.
py-test/: Contém os testes escritos utilizando o Pytest.
.gitignore: Arquivo que especifica quais arquivos ou pastas devem ser ignorados pelo Git.
requirements.txt: Arquivo que lista as dependências do projeto.

🔩 Analisando os Testes de Ponta a Ponta
Os testes de ponta a ponta são realizados para garantir que o fluxo completo de interação com a interface de usuário esteja funcionando corretamente. Isso inclui:

Navegação entre páginas.
Interação com formulários e botões.
Validação de resultados.
Esses testes são importantes para garantir que o sistema se comporta como esperado.

⌨️ Testes de Estilo de Codificação
Os testes de estilo de codificação verificam a conformidade com padrões de código estabelecidos, como o PEP 8 para Python. Eles ajudam a garantir que o código seja legível e mantenha a consistência do projeto.



✒️ Autores
Felipe Santos - Trabalho Inicial - felipesantos
Érico Borgonove - Orientador - ericoborgonove


📄 Licença
Não possui licença.

🎁 Expressões de Gratidão

⌨ com ❤️ por Felipe Santos 😊

