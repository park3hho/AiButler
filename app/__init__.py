from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from app.stimuli.routers.v1.channeling import router as external_stimuli
from app.brain.routers.v1.accept_textual_stimuli import router as accept_external_stimuli
app = FastAPI(
    default_response_class=ORJSONResponse
)

app.include_router(external_stimuli)
app.include_router(accept_external_stimuli)