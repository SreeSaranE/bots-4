def format_zoho_response(response_data):
    """Format the response according to Zoho SalesIQ webhook requirements"""
    
    if not response_data['success']:
        return {
            'message': response_data['response_text'],
            'type': 'text'
        }
    
    # Basic text response
    formatted_response = {
        'message': response_data['response_text'],
        'type': 'text'
    }
    
    # Add quick replies if available
    if 'quick_replies' in response_data:
        formatted_response['suggestions'] = response_data['quick_replies']
    
    # Add attachments if available
    if 'attachments' in response_data:
        formatted_response['attachments'] = response_data['attachments']
    
    return formatted_response