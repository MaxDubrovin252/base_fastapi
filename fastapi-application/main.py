from fastapi import FastAPI
from api import router
import uvicorn
from core.config import settings

app = FastAPI()

app.include_router(router=router,prefix=settings.api.prefix)

if __name__=="__main__":
    uvicorn.run("main:app",reload=True)
