# Actions on Google D.I.Y.

Questo è il materiale che è stato utilizzato per il talk [Actions on Google D.I.Y.](https://www.meetup.com/it-IT/GDG-Pisa/events/261505215/).
___
##### Disclaimer
Questo sorgente è stato costruito con il fine di essere semplice e comprensibile a tutti. Alcune pratiche utilizzate potrebbero essere rischiose in ambiti professionali, utilizzate il codice con cautela.
___

Potete trovare le slides utilizzate per il talk in questo [link](https://docs.google.com/presentation/d/e/2PACX-1vR2vLmZeMmmVxzxrjb5VsQATe0mFNQZPc-QCGBeiB7kHVmiRJYXnkXVKjpIvR1Nelp1sDz116HA06W7/pub).
Nelle slides troverete anche le istruzioni per comprendere quali sono gli strumenti da installare sulla vostra macchina e che serviranno per utilizzare il progetto.


#### Importante
Passi importanti da svolgere prima:

* Generare i certificati per il vostro dominio con Let's Encrypt. DialogFlow richiede un certificato SSL **A**, questo significa che non possono essere usati certificati autogenerati.
* Sostituire il campo `my.awesome.domain` con il vostro dominio che avete appena certificato.
* Sostituire il campo `my.awesome.api` con l'API che deciderete di usare. In caso vogliate testare il progetto con la stessa API che abbiamo utilizzato durante il talk, rimuovere il `#` dalla riga che contiene l'url alla repo del GDG Pisa ed eliminate la riga di sotto.
* È possibile sostituire `my_awesome_endpoint` con uno di vostro gradimento.
* Effettuare il port forwarding alla porta 4043 verso il Raspberry per poter utilizzare il progetto.
	La scelta della porta è arbitraria e può essere modificata.


#### Come lanciare il server
Vi basterà andare nel terminale, collocarvi nella cartella del server ed usare il comando:
```bash
sudo python3 ActionOnGoogle.py
```


### Dubbi?
Per qualsiasi cosa contattaci direttamente su Telegram:
* [@kiaruzza](https://t.me/kiaruzza)
* [@domenicoblanco](https://t.me/domenicoblanco)
