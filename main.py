from fastapi import FastAPI
from handler import router
hfhhfhf
# Crea un'istanza di FastAPI con specifiche configurazioni per i percorsi di documentazione
app = FastAPI(
    # Imposta il percorso personalizzato per il documento OpenAPI JSON
    # Questo è il documento che descrive formalmente l'intera API.
    openapi_url="/documentation/json",

    # Specifica un URL personalizzato per la documentazione interattiva di Swagger UI.
    # Swagger UI permette di esplorare e testare l'API in un'interfaccia grafica.
    docs_url="/documentation/",

    # Disabilita ReDoc, un'altra interfaccia di documentazione.
    # Impostando questo valore a None, l'endpoint ReDoc non sarà disponibile.
    redoc_url=None
)

# Decoratori per definire una rota
app.include_router(router)







