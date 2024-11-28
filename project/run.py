from app import create_app
import ssl
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = create_app()

if __name__ == '__main__':
    try:
        # SSL Configuration
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        ssl_context.load_cert_chain('cert.pem', 'key.pem')
        
        # Run the Flask app with HTTPS
        logger.info("Starting server on https://0.0.0.0:443")
        app.run(host='0.0.0.0', port=443, ssl_context=ssl_context)
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        raise