from flask import Flask, jsonify, abort, make_response
from evento import Evento
from evento_online import EventoOnline


app = Flask(__name__)

ev_online = EventoOnline('Live de python')
ev2_online = EventoOnline('Curso de ract')
ev3 = Evento('Curso SQL', 'Belo Horizonte')
eventos = [ev_online, ev2_online, ev3]


@app.route("/")
def index():
    return "<h1>Flask configurado com sucesso!!!!</h1>"


@app.route("/api/eventos/")
def listar_eventos():
    evento_dict = []
    for ev in eventos:
        evento_dict.append(ev.__dict__)
    return jsonify(evento_dict)


@app.errorhandler(404)
def nao_encontrado(erro):
    return (jsonify(erro=str(erro)), 404)


@app.route("/api/eventos/<int:id>/")
def detalhar_evento(id):
    for ev in eventos:
        if ev.id == id:
            return jsonify(ev.__dict__)
    abort(404, 'Evento não encontrado')
