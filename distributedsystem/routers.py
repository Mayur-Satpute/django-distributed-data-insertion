class ModelRouter:

    def read(self, model, **hints):
        if model.__name__ == "User":
            return "usersdb"
        if model.__name__ == "Product":
            return "productsdb"
        if model.__name__ == "Order":
            return "ordersdb"
        
        return None
    
    def write(self, model, **hints):
        return self.read(model)
    

    def migrate(self, db, app_label, model_name=None, **hints):
        if model_name == "user":
            return db == "usersdb"
        if model_name == "product":
            return db == "productsdb"
        if model_name == "order":
            return db == "ordersdb"
        return False