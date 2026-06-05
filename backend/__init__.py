from fastapi import FastAPI

def create_app():
    """Create and configure the FastAPI application"""
    app = FastAPI(
        title="Document Translation Benchmark Platform",
        description="API for translating English PDFs to Vietnamese",
        version="1.0.0"
    )
    
    # Import and include routers here if we create separate routers
    
    return app