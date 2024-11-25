# Teste API Querido Diário 

Este projeto faz parte da iniciativa "Monitoramento de Gastos Públicos", que visa proporcionar uma interface acessível para cidadãos, estudantes e profissionais visualizarem e compreenderem padrões de gastos públicos, fornecedores recorrentes e possíveis irregularidades nas contas dos municípios do estado de Alagoas.

A API de Gazetas é um dos componentes principais deste projeto, sendo utilizada para buscar informações relevantes de publicações oficiais sobre licitações e outros documentos relacionados aos gastos públicos. Para isso, estamos utilizando a API "Querido Diário" (https://queridodiario.ok.org.br), que oferece dados sobre essas publicações.

A API está sendo testada e para ver se ela pode ser integralizada ao projeto de Monitoramento de Gastos Públicos, cujo repositório pode ser acessado aqui: https://github.com/unb-mds/2024-2-Squad06.

## Endpoints

### 1. `/api/licitacoes/`

Este endpoint permite que os usuários acessem informações sobre licitações específicas publicadas nas gazetas oficiais de Maceió (AL). Ele realiza uma busca filtrando as publicações por palavras-chave (como "licitação") e retorna os dados da API do *Querido Diário*, que fornece as gazetas eletrônicas oficiais de diversos municípios.

- **URL**: `http://localhost:8000/api/licitacoes/`
- **Método**: `GET`
- **Descrição**: Retorna as gazetas com informações sobre licitações.
  
### 2. `/api/exibir_gazettes/`

Este endpoint organiza e exibe as gazetas de maneira mais legível e acessível para os usuários. Ele trata as respostas da API do *Querido Diário*, organizando os dados para exibição em formato adequado e retornando informações como a data, o nome do território, o código do estado, entre outras.

- **URL**: `http://localhost:8000/api/exibir_gazettes/`
- **Método**: `GET`
- **Descrição**: Exibe as gazetas organizadas com detalhes úteis para análise.
  
## Como funciona?

1. **Requisição de Gazetas**:
    - A API realiza uma requisição para o serviço *Querido Diário* e recebe um JSON com as gazetas públicas, filtradas pela palavra-chave "licitação".
    - A resposta da API é processada e os dados são organizados para serem apresentados de maneira mais acessível.

2. **Organização dos Dados**:
    - Os dados recebidos incluem informações como a data da publicação, o nome do território, o estado, o link para o texto completo da gazeta e os trechos relevantes.
    - Esses dados são então exibidos de forma clara e organizada, tornando-os mais fáceis de entender para análise.

## Como rodar o projeto?

### Requisitos:
- Python 3.x
- Django

### Passos para iniciar:

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/Ana-Luiza-SC/teste_api_querido_diario
    ```

2. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Rodar o servidor Django**:
    ```bash
    python manage.py runserver
    ```

4. Acesse os endpoints na URL `http://localhost:8000/`.

### Testar os endpoints:

- Acesse `http://localhost:8000/api/licitacoes/` para visualizar as licitações publicadas nas gazetas.
- Acesse `http://localhost:8000/api/exibir_gazettes/` para visualizar as gazetas de forma organizada.

## Contribuições

Contribuições são bem-vindas! Para contribuir com o projeto, siga os passos abaixo:

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nome-da-feature`).
3. Faça suas alterações e commit (`git commit -am 'Adicionando nova feature'`).
4. Faça o push para a branch (`git push origin feature/nome-da-feature`).
5. Envie um pull request.

