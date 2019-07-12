import requests
import json
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

# Impostiamo l'endpoint da utilizzare con Dialogflow
@app.route('/my_awesome_endpoint', methods=['POST'])

def send_response():
	# Riceviamo il JSON da parsare, la presenza del force=True richiede che la richiesta trasmetta un JSON
	req = request.get_json(force=True)
	suggestionchip = ["Chiedi ancora", "Esci"]
	ResponseFromServer = obtaininfofromserver()

	res = {
		"fulfillmentText": "Ciao! Il nostro prossimo evento sarà "+ResponseFromServer["event"]+" giorno "+ResponseFromServer["date"]+" alle "+ResponseFromServer["starttime"]+" presso il "+ResponseFromServer["place"],
		"fulfillmentMessages": [{
			"card": {
				"title": ResponseFromServer["event"],
				"subtitle": ResponseFromServer["description"],
				"imageUri": ResponseFromServer["image"],
				"buttons": [{
					"text": "🎟️ Ottieni i biglietti",
					"postback": ResponseFromServer["url"]
				}]
			}
		}],
		"payload": {
			"google": {
			  	"expectUserResponse": True,
			 	"richResponse": {
					"items": [
						{
							"simpleResponse": {
								"textToSpeech": "Ciao! Il nostro prossimo evento sarà "+ResponseFromServer["event"]+" giorno "+ResponseFromServer["date"]+" alle "+ResponseFromServer["starttime"]+" presso il "+ResponseFromServer["place"],
						}
						}, {
							"basicCard": {
								"title": ResponseFromServer["event"],
								"formattedText":ResponseFromServer["description"],
								"subtitle": str(ResponseFromServer["starttime"])+" - "+ResponseFromServer["endtime"],
								"image": {
									"url": ResponseFromServer["image"],
									"accessibilityText": "Immagine dell'evento"
								},
								"buttons": [{
									"title": "🎟️ Ottieni i biglietti",
									"openUrlAction": {
										"url": ResponseFromServer["url"]
									}
								}],
							}
						}
					],
					"linkOutSuggestion": {
						"destinationName": "🗺️ Indicazioni",
						"url": ResponseFromServer["maps"]
					},
					"suggestions": [
						{
							"title": suggestionchip[0]
						},
						{
							"title": suggestionchip[1]
						}
					]
				}
				
			}
		}
	}

	return make_response(jsonify(res))

# Funzione per ottenere le informazioni
def obtaininfofromserver():
	# JSON utilizzato durante l'evento (in caso si vogliano fare dei test)
	#url = "https://raw.githubusercontent.com/gdgpisa/actions-on-google-diy/master/API.json"
	url = "my.awesome.api"

	response = requests.request("GET", url)
	response = response.json()

	return response


if __name__ == '__main__':
	context = ('/etc/letsencrypt/live/my.awesome.domain/fullchain.pem','/etc/letsencrypt/live/my.awesome.domain/privkey.pem')

	PORT = 4043
	app.run(
		debug=True,
		port=PORT,
		host='0.0.0.0',
		ssl_context=context
	)
