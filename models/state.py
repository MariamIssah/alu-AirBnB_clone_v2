from models.base_model import BaseModel

class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize the State instance """
        super().__init__(*args, **kwargs)
        if 'name' in kwargs:
            self.name = kwargs['name']
        else:
            self.name = ""
