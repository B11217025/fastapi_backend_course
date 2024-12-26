from fastapi import FastAPI
from .database import Base, engine
from .routers import router

# Initialize FastAPI
app = FastAPI()

# Initialize
#Base.metadata.create_all(bind=engine)

#Reister Router
app.include_router(router=router, prefix="/api", tags=["todos"])
