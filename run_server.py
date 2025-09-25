#!/usr/bin/env python3
"""
Simple startup script for Railway deployment
This bypasses any Railway auto-detection issues
"""

import os
import sys

def main():
    # Set default port
    port = 8000
    
    # Try to get port from environment
    try:
        port_env = os.environ.get('PORT')
        if port_env:
            port = int(port_env)
        print(f"Using port: {port}")
    except (ValueError, TypeError) as e:
        print(f"Port error: {e}, using default port 8000")
        port = 8000
    
    # Import and run
    try:
        print("Starting uvicorn server...")
        import uvicorn
        from main import app
        
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=port,
            log_level="info",
            access_log=True
        )
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
