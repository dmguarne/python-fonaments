
## Descripció:

Una eina OSINT lleugera que monitoritzi la situació geopolítica al Sàhara Occidental i retorni informes. La informació que monitoritza l'afegeix a un timeline. Els informes es poden  fer a mida: filtrats per font, per període de dates, per paraula clau.

## Comportament:

- El programa extreu tituals i textos de les fonts.
- Desa cada contingut en el fitxer de la seva font.
- Desa els titulars en el timeline.
- L'usuari pot generar:
    - Un informe amb titulars i, opcionalment, continguts, agrupats per font, per a un període específic, font o paraula clau.
    - Un timeline amb els titulars (citant font), ordenats cronològicament, per a un període específic.

## Arguments:

- Executar cerca (actualitza el contingut de tots els fitxers per a la data actual)
- Generar informe (període, fonts, paraules clau)
- Generar timeline (període)

## Arquitectura:

sàhara_monitor/
├── main.py
├── connectors/
│   ├── rss.py
│   ├── scraping.py
│   └── api.py
├── eines/
│   ├── timeline.py
│   ├── informe.py
│   └── utils.py
└── dades/
    ├── fonts/
    │   └── [font].json
    └── magatzem/
        └── magatzem.json
    └── sortides/
        └── [informes i timelines generats]


## Fonts:

Organismes internacionals:
- ONU: MINURSO [scraping]
- Informes del Secretari General i Resolucions del Consell de Seguretat [RSS]
- Parlament Europeu [Open Data API]
Organismes governamentals:
- Ministerio de Asuntos Exteriores [scraping]
ONG:
- Amnistia Internacional [scraping]
- Human Rights Watch [RSS]
Premsa:
- Sahara Press Service [scraping]
- Marroc World News [scraping]
- Algérie Press Service [scraping]
- Al Jazeera [scraping]
XXSS:
- Twitter [API per developers]
Altres:
- ACLED (Armed Conflict Location & Event Data) [API]