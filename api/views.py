from django.shortcuts import render
import requests
# Create your views here.

def generate_request(url):
    response = requests.get(url)
    if response.status_code == 200:
      return response.json()

def numero_temporadas(data):
  numeros = []
  for e in data:
    if int(e['season']) not in numeros:
      numeros.append(int(e['season']))

  return numeros


def inicio(request):
  #esta funcion debe entregar todas las temporadas
  URL_bcs = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul'
  URL_bb = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad'

  data_bcs = generate_request(URL_bcs)
  data_bb = generate_request(URL_bb)

  ctx = {
    "temporadas_bcs":numero_temporadas(data_bcs),
    "temporadas_bb":numero_temporadas(data_bb)
  }
  return render(request, 'index.html', ctx)


def show_bb(request, n):
  URL = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad'
  data = generate_request(URL)

  episodes = []
  for e in data:
    if int(e['season']) == n:
      episodes.append(e)

  ctx ={
    'episodes':episodes,
    'numero_temporada':n
  }
  return render(request, 'episodes_bb.html', ctx)

def show_bcs(request, n):
  URL = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul'
  data = generate_request(URL)

  episodes = []
  for e in data:
    if int(e['season']) == n:
      episodes.append(e)

  ctx ={
    'episodes':episodes,
    'numero_temporada':n
  }
  return render(request, 'episodes_bcs.html', ctx)

def show_episode(request, id):
  URL = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes'
  data = generate_request(URL)

  for episode in data:
    if int(episode['episode_id'])==int(id):
      detail = episode

  ctx ={
    'episode':detail
  }
  return render(request, 'detail_episode.html', ctx)


def show_character(request, name):
  URL = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+ name
  data = generate_request(URL)

  URL_quotes = 'https://tarea-1-breaking-bad.herokuapp.com/api/quote?author='+ name
  data_quotes = generate_request(URL_quotes)

  for char in data:
    if char['name']==name:
      detail = char

  quotes = []
  for q in data_quotes:
    if q['author'] == name:
      quotes.append(q)

  bb = [int(i) for i in detail['appearance']]
  bcs = [int(i) for i in detail['better_call_saul_appearance']]

  ctx = {
    'character': detail,
    'bb_appearance':bb,
    'bcs_appearance':bcs,
    'quotes':quotes
  }
  return render(request, 'characters.html', ctx)

def search_results(request):
  if request.method == 'POST': 
    value = request.POST['value'] 
  
  data_characters = []
  
  offset = 0
  while True:
    URL = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+str(value)+'&limit=10&offset='+ str(offset)
    data = generate_request(URL)
    if len(data) == 0:
      break
    else:
      for p in data:
        data_characters.append(p)
      offset += 10
  
  characters = []
  for char in data_characters:
    if value.lower() in char['name'].lower():
        characters.append(char)
  
  
  ctx = {
    'characters':characters
  }
  return render(request, 'show_search.html', ctx)