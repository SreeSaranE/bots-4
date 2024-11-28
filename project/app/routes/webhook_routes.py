from flask import Blueprint, request, jsonify, current_app
from ..services.chat_service import ChatService
from ..utils.response_formatter import format_zoho_response
from functools import wraps
import logging

webhook_bp = Blueprint('webhook', __name__)
logger = logging.getLogger(__name__)

def verify_zoho_webhook(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_token = request.headers.get('X-ZohoSalesIQ-Auth-Token')
        if not auth_token or auth_token != current_app.config['ZOHO_SALESIQ_AUTH_TOKEN']:
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated_function

@webhook_bp.route('/webhook', methods=['POST'])
@verify_zoho_webhook
def handle_webhook():
    try:
        data = request.json
        logger.info(f"Received webhook data: {data}")
        
        if not data or 'message' not in data:
            return jsonify({'error': 'Invalid request data'}), 400
            
        chat_service = ChatService(current_app.config)
        
        message_content = data.get('message', {}).get('content', '')
        visitor_data = {
            'visitor_id': data.get('visitor', {}).get('id'),
            'name': data.get('visitor', {}).get('name', 'Guest'),
            'email': data.get('visitor', {}).get('email'),
            'department': data.get('department', {}).get('name'),
            'chat_id': data.get('chat', {}).get('id')
        }
        
        response = chat_service.process_message(message_content, visitor_data)
        formatted_response = format_zoho_response(response)
        
        logger.info(f"Sending response: {formatted_response}")
        return jsonify(formatted_response), 200
        
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}", exc_info=True)
        return jsonify({'error': 'Internal server error'}), 500