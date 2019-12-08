const fs = require('fs');
const path = require('path');
const winston = require('winston');
const winston_daily = require('winston-daily-rotate-file');

const { label, timestamp, combine, printf, json, prettyPrint } = winston.format;
const logHome = path.join( __dirname, '../../logs' );

function replacer(key, value) {
  if (value instanceof Buffer) {
    return value.toString('base64');
  } else if ( value instanceof Error ) {
    return { message: 'error\n'+value.stack };
  } else if ( value instanceof Object ) {
    if( 'message' in value && value.message instanceof Object ){
      return { message: 'json\n'+JSON.stringify( value.message, null, 2 ) }
    }
  }
  return value;
}

const format = combine(
  label({ label: 'heoapi' })
  , timestamp({ format: 'YYYY-MM-DD HH:mm:ss.SSSS' })
  , printf(( info )=>{ 
    const _reInfo = JSON.parse(JSON.stringify( info, replacer ));

    return ` ${ info.timestamp } - ${ info.label } - ${info.level.toUpperCase()} - ${ _reInfo.message } `
  })
);

const options = {
  file: {
    level: 'debug'
    , filename: `${logHome}/client.log`
    // , zippedArchive: true
  },
  file_daily: {
    level: 'debug'
    , filename: `${logHome}/client.log`
    , prepend: true
    , datePattern: 'YYYY-MM-DD'
  },
  console: {
    level: 'debug'
  }
}

const logger = new winston.createLogger({
  level: 'error'
  , format: format
  , colorize: true
  , handleExceptions: true
  , transports: [
    // add transports 
  ]
});

// logger.add( new winston_daily( options.file_daily ) );
// logger.add( new winston.transports.File( options.file ) );

if(process.env.NODE_ENV !== 'production'){
  logger.add(new winston.transports.Console( options.console ));
}

module.exports = logger;