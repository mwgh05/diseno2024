class RoleMiddleware:
    def __init__(self, required_role, roles_list):
        self.required_role = required_role
        self.roles_list = roles_list

    def check_role(self, request, required_role):
        """
        Verifica si el rol del usuario que realiza la solicitud 
        cumple con el rol requerido para acceder al recurso. Si el rol no coincide, 
        deniega el acceso.
        """
        pass

    def restrict_to_roles(self, roles):
        """
        Restringe el acceso a un recurso a los usuarios que 
        pertenezcan a los roles indicados. Verifica que el rol del usuario 
        esté dentro de la lista de roles permitidos.
        """
        pass

