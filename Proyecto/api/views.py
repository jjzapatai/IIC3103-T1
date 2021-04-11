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






    
