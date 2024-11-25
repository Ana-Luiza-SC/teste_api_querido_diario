import requests
from django.shortcuts import render
from django.http import JsonResponse

# Função para buscar dados da API do Querido Diário
def fetch_gazettes(request):
    # ID de Maceió, AL
    territory_id = "2704302"
    # Palavra-chave para busca
    querystring = "licitação"

    # Parâmetros da requisição
    url = (
        f"https://queridodiario.ok.org.br/api/gazettes?"
        f"territory_ids={territory_id}&querystring={querystring}&"
        f"excerpt_size=500&number_of_excerpts=1&size=10" # como eu coloquei size =10, só terá 10 requisições para ver os parametros
    )

    try:
        # Fazer a requisição GET
        response = requests.get(url)
        response.raise_for_status()  # Levantar erro se o status não for 200
        data = response.json()  # Obter resposta JSON

        # Verificar se há dados
        if not data.get("gazettes"):
            return JsonResponse({"message": "Nenhuma gazeta encontrada para Maceió"}, status=404)

        # Retornar dados brutos para depuração
        return JsonResponse(data)

    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)

def exibir_gazettes(request):
    # ID de Maceió, AL
    territory_id = "2704302"
    querystring = "orçamento"

    url = (
        f"https://queridodiario.ok.org.br/api/gazettes?"
        f"territory_ids={territory_id}&querystring={querystring}&"
        f"excerpt_size=500&number_of_excerpts=1&size=50" # já aqui terá 50 requisições
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()


        # Organize os dados para exibição
        gazettes = data.get("gazettes", [])
        dados_organizados = [
            {
                "date": gazette.get("date"),
                "territory_name": gazette.get("territory_name"),
                "state_code": gazette.get("state_code"),
                "text_url": gazette.get("txt_url"),
                "excerpts": gazette.get("excerpts"),
                "url": gazette.get("url"),
            }
            for gazette in gazettes
        ]

        # Passar os dados organizados para o template
        return render(request, "api_test/exibir_gazettes.html", {"dados": dados_organizados})


    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)