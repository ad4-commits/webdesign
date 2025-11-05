#!/bin/bash
echo "Building static site..."
cd src

# Generate the site
if python3 main.py; then
    echo ""
    echo "✓ Site generated successfully!"
    echo ""
    echo "Starting web server on http://localhost:8888"
    echo "Press Ctrl+C to stop the server"
    echo ""
    
    # Go to public directory and start server
    cd ../public
    python3 -m http.server 8888
else
    echo "✗ Site generation failed!"
    exit 1
fi
