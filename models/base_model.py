import uuid
from datetime import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)  # Add this line for new instances
        else:
            # Handle missing 'updated_at' or 'created_at'
            kwargs['updated_at'] = datetime.strptime(kwargs.get('updated_at',
                                                                datetime.now()
                                                                ),
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs.get('created_at',
                                                                datetime.now()
                                                                ),
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            # Use pop() to safely remove '__class__'
            kwargs.pop('__class__', None)

            # Use update() to efficiently update multiple attributes
            self.__dict__.update(kwargs)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['id'] = obj_dict.get('id', None)
        return obj_dict

    def reload(self):
        storage.reload()
