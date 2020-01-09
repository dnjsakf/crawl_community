import React from 'react';

import { withStyles } from '@material-ui/core/styles';

/* Components */
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';


const styles = ( theme )=>({
  tabpanel: {
    flex: 1,
    background: '#eaeff1',
  }
});

export const TabPanel = withStyles(styles)(( props )=>{
  const { classes, children, active, index, ...other } = props;

  return (
    <Typography
      className={ classes.tabpanel }
      component="div"
      role="tabpanel"
      hidden={active !== index}
      id={`wrapped-tabpanel-${index}`}
      aria-labelledby={`wrapped-tab-${index}`}
      {...other}
    >
      { active === index && <Box>{ children }</Box> }
    </Typography>
  );
});

export const HeaderTabPanel = withStyles(styles)(( props )=>{
  const { classes, children, active, index, ...other } = props;

  return (
    <Typography
      component="div"
      role="tabpanel"
      hidden={active !== index}
      id={`wrapped-header-tabpanel-${index}`}
      aria-labelledby={`wrapped-header-tab-${index}`}
      {...other}
    >
      { active === index && <Box>{ children }</Box> }
    </Typography>
  );
});


export const NaviTabPanel = withStyles(styles)(( props )=>{
  const { classes, children, active, index, ...other } = props;

  return (
    <Typography
      component="div"
      role="tabpanel"
      hidden={active !== index}
      id={`wrapped-navi-tabpanel-${index}`}
      aria-labelledby={`wrapped-navi-tab-${index}`}
      {...other}
    >
      { active === index && <Box>{ children }</Box> }
    </Typography>
  );
});

