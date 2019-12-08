import os
import logging
import logging.config
import json

conf = os.path.join( os.path.dirname( __file__ ), 'logger.conf.json' )

with open( conf, 'rt' ) as f:
    config = json.load( f )
    logging.config.dictConfig( config )

logger = logging.getLogger('MongoDB')