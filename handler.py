from typing import Dict, Any

class RequestHandler:
    """
    A class to handle incoming requests and generate responses.
    """

    def __init__(self, default_response: str) -> None:
        """
        Initialize the RequestHandler with a default response.
        """
        self.default_response = default_response

    def handle_request(self, request: Dict[str, Any]) -> str:
        """
        Process the incoming request and return a response.
        
        Args:
            request (Dict[str, Any]): The incoming request data.
        
        Returns:
            str: The response for the request.
        """
        if 'action' in request:
            return self.process_action(request['action'])
        return self.default_response

    def process_action(self, action: str) -> str:
        """
        Process the action specified in the request.
        
        Args:
            action (str): The action to process.
        
        Returns:
            str: The result of the action processing.
        """
        if action == 'greet':
            return 'Hello, User!'
        elif action == 'farewell':
            return 'Goodbye, User!'
        return 'Unknown action.'

# Example usage:
if __name__ == '__main__':
    handler = RequestHandler('No action performed.')
    print(handler.handle_request({'action': 'greet'}))
    print(handler.handle_request({'action': 'unknown'}))