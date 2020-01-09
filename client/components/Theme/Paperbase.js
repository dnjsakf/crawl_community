import React, { memo, useState, useCallback, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { createSelector } from 'reselect';
import { withRouter } from 'react-router-dom';
import PropTypes from 'prop-types';

import { createMuiTheme, ThemeProvider, withStyles } from '@material-ui/core/styles';

/* Components */
import CssBaseline from '@material-ui/core/CssBaseline';
import Hidden from '@material-ui/core/Hidden';

import Navigator from './Navigator';
import { Authentication, Management, Copyright } from '../Contents';
import Header from './Header';
import { TabPanel } from './../Contents/Tabs/TabPanels';

let theme = createMuiTheme({
  palette: {
    primary: {
      light: '#63ccff',
      main: '#009be5',
      dark: '#006db3',
    },
  },
  typography: {
    h5: {
      fontWeight: 500,
      fontSize: 26,
      letterSpacing: 0.5,
    },
  },
  shape: {
    borderRadius: 8,
  },
  props: {
    MuiTab: {
      disableRipple: true,
    },
  },
  mixins: {
    toolbar: {
      minHeight: 48,
    },
  },
});

theme = {
  ...theme,
  overrides: {
    MuiDrawer: {
      paper: {
        backgroundColor: '#18202c',
      },
    },
    MuiButton: {
      label: {
        textTransform: 'none',
      },
      contained: {
        boxShadow: 'none',
        '&:active': {
          boxShadow: 'none',
        },
      },
    },
    MuiTabs: {
      root: {
        marginLeft: theme.spacing(1),
      },
      indicator: {
        height: 3,
        borderTopLeftRadius: 3,
        borderTopRightRadius: 3,
        backgroundColor: theme.palette.common.white,
      },
    },
    MuiTab: {
      root: {
        textTransform: 'none',
        margin: '0 16px',
        minWidth: 0,
        padding: 0,
        [theme.breakpoints.up('md')]: {
          padding: 0,
          minWidth: 0,
        },
      },
    },
    MuiIconButton: {
      root: {
        padding: theme.spacing(1),
      },
    },
    MuiTooltip: {
      tooltip: {
        borderRadius: 4,
      },
    },
    MuiDivider: {
      root: {
        backgroundColor: '#404854',
      },
    },
    MuiListItemText: {
      primary: {
        fontWeight: theme.typography.fontWeightMedium,
      },
    },
    MuiListItemIcon: {
      root: {
        color: 'inherit',
        marginRight: 0,
        '& svg': {
          fontSize: 20,
        },
      },
    },
    MuiAvatar: {
      root: {
        width: 32,
        height: 32,
      },
    },
  },
};

const drawerWidth = 256;

const styles = {
  root: {
    display: 'flex',
    minHeight: '100vh',
  },
  drawer: {
    [theme.breakpoints.up('sm')]: {
      width: drawerWidth,
      flexShrink: 0,
    },
  },
  app: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
  },
  main: {
    flex: 1,
    padding: theme.spacing(2, 2),
    background: '#eaeff1',
  },
  footer: {
    padding: theme.spacing(2),
    background: '#eaeff1',
  },
  tabs: {
    backgroundColor: theme.palette.primary.main, 
    color: theme.palette.common.white,
  }
};

const navigatorSelector = createSelector(
  ( state )=>( state.menus.navigator ),
  ( res )=>({
    activeNaviIndex: res.index
    , activeNaviId: res.active
    , activeNaviLabel: res.label
  })
);

const Paperbase = memo(( props )=>{
  const { classes } = props;

  const [ mobileOpen, setMobileOpen ] = useState( false );

  const { activeNaviIndex, activeNaviId, activeNaviLabel } = useSelector( navigatorSelector );

  const handleDrawerToggle = useCallback(()=>{
    setMobileOpen(!mobileOpen);
  }, []);

  useEffect(()=>{
    console.log( '[Paperbase][activeNavi][current]', activeNaviIndex, activeNaviId, activeNaviLabel );
    return ()=>{
      console.log( '[Paperbase][activeNavi][prev]', activeNaviIndex, activeNaviId, activeNaviLabel );
    }
  }, [ activeNaviIndex, activeNaviId, activeNaviLabel ]);

  useEffect(()=>{
    console.log( '[Paperbase][mobileOpen][current]', mobileOpen );
    return ()=>{
      console.log( '[Paperbase][mobileOpen][prev]', mobileOpen );
    }
  }, [ mobileOpen ]);

  return (
    <ThemeProvider theme={ theme }>
      <div className={ classes.root }>
        <CssBaseline />
        {/* Navigator */}
        <nav className={ classes.drawer }>
          <Hidden smUp implementation="js">
            <Navigator
              PaperProps={{ style: { width: drawerWidth } }}
              variant="temporary"
              open={ mobileOpen }
              onClose={ handleDrawerToggle }
            />
          </Hidden>
          <Hidden xsDown implementation="css">
            <Navigator 
              PaperProps={{ style: { width: drawerWidth } }} 
            />
          </Hidden>
        </nav>
        {/* Contents */}
        <div className={ classes.app }>
          <Header 
            onDrawerToggle={ handleDrawerToggle }
            activeNaviLabel={ activeNaviLabel }
          />
          <React.Fragment>
            <TabPanel active={ activeNaviIndex } index={ 0 }>
              <Authentication />
            </TabPanel>
            <TabPanel active={ activeNaviIndex } index={ 1 }>
              <Management />
            </TabPanel>
          </React.Fragment>

          <footer className={ classes.footer }>
            <Copyright />
          </footer>
        </div>
      </div>
    </ThemeProvider>
  );
});

Paperbase.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withRouter(withStyles(styles)(Paperbase));