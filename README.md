# Vertaal woorden naar klanken
de input van dit script is een csv file bestaande uit 1 kolom met een titel en vervolgens een serie woorden die vertaald moeten worden. Als output krijgen we een csv file genaamd 'translation.csv' van 2 kolommen, woorden en vertaling.

## How to run
in de folder is een task.bat file aanwezig, door dubbel op deze te klikken wordt het script automatisch uitgeoefend. Hier is het wel belangrijk dat het input bestand altijd dezelfde naam heeft namelijk **words.csv**.
<sp>
Een alternatieve manier om het script uit te voeren is door een cmd venster handmatig te openen en te navigeren naar de huidige map met het commando cd. Dan kan het script uitgevoerd worden via het volgende commando:

    python main.py
het script zal daarna vragen voor de naam van het input bestand en zal daarna vertalen indien het bestand bestaat.

## What does it do
Het vertalen gebeurt stap per stap. Eerst worden woorden vertaald naar een tijdelijke versie en ten slotte worden ze na de gevraagde codering vertaalt.  De vertaling gebeurt als volgt per woord in de lijst.
We kijken eerst of er 3- en/of 2-tekenklanken aanwezig zijn en vervangen deze. Vervolgens gaan we zoeken naar doffe klinkers om te vervangen. 
Daarna gaan we alle resterende klinkers, enkel en dubbel vervangen. 
We controleren voor de 'sch' en 'ch' en vertalen deze en vervolgens voor de dubbele medeklinkers. Ten slotte gaan we de resterende medelklinkers nog vervangen.