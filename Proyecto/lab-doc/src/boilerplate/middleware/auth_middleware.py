class AuthMiddleware:
    def __init__(self, token, expiration_time, refresh_token):
        self.token = token
        self.expiration_time = expiration_time
        self.refresh_token = refresh_token

    def authenticate_request(self, request):
        """
        Verifica que la solicitud entrante esté autenticada 
        utilizando el token proporcionado. Si el token no es válido o ha expirado,
        devuelve un error o solicita un nuevo token.
        """
        pass

    def get_user_from_token(self, token):
        """
        Extrae la información del usuario a partir del token JWT.
        Utiliza el token proporcionado para obtener los datos del usuario autenticado.
        """
        pass

    def refresh_token(self, token):
        """
        Renueva el token JWT si el token actual ha expirado. 
        Utiliza el refresh token para generar uno nuevo.
        """
        pass

