import os
import sys
# sys.path.append(os.getcwd())
sys.path.append('./')

from fastapi import FastAPI
from .config.logging_config import setup_logging
from .api import dock, update

# Initialize FastAPI app
app = FastAPI()

# Setup logging
setup_logging()

# Include the routers
app.include_router(dock.router, prefix="/dock", tags=["dock"])
app.include_router(update.router, prefix="/update", tags=["update"])


# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
