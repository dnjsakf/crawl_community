from celery import Celery
from tasks import celeryconfig

class MyCelery(Celery):
    def gen_task_name(self, name, module):
        print( name, module )
        #if module.startswith('tasks.'): # name cutting
        #    module = module[6:]
        print( name, module )
        return super(MyCelery, self).gen_task_name(name, module)

app = MyCelery( 'worker' )
app.config_from_object( celeryconfig )