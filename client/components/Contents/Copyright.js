import React from 'react';

/* Components */
import Typography from '@material-ui/core/Typography';
import Link from '@material-ui/core/Link';

const Copyright = ()=>{
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link to="/" color="inherit">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
};

export default Copyright;