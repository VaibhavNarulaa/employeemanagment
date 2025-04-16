from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from usermanagment import model
from usermanagment.database import engine
from usermanagment.user import router as user_router 
from usermanagment.manager import router as manager_router 
import os 

# Add CORS middleware to allow requests from the frontend (adjust origin as needed


model.Base.metadata.create_all(bind=engine)

app=FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # or specify your frontend URL like "http://localhost:3000"
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# frontend_path = os.path.join(os.path.dirname(__file__),  'frontend','subfolder', )

# # Serve static files (JavaScript, CSS) from the frontend folder
# app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# # Serve index.html when accessing the root URL (GET /)
# @app.get("/")
# def read_index():
#     return FileResponse(os.path.join(frontend_path, "index.html"))

# @app.get("/dashboard")
# def read_dashboard():
#     return FileResponse(os.path.join(frontend_path, "dashboard.html"))

# @app.get("/login.html")
# def read_login():
#     return FileResponse(os.path.join(frontend_path, "login.html"))

app.include_router(user_router)
app.include_router(manager_router)