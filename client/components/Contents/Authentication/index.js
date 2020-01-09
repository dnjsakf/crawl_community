import React, { memo, useCallback } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { createSelector } from 'reselect';
import { actionChangeTabsHeader } from './../../../reducers/event/tabs';

import { HeaderTabPanel } from './../../Contents/Tabs/TabPanels';
import Users from './Users';
import { withStyles } from '@material-ui/core/styles';

import AppBar from '@material-ui/core/AppBar';
import Tab from '@material-ui/core/Tab';
import Tabs from '@material-ui/core/Tabs';

function a11yProps(index) {
  return {
    'id': `header-tab-${index}`,
    'aria-controls': `header-tabpanel-${index}`,
  };
}

const styles = ( theme )=>({
  main: {
    padding: theme.spacing(2, 2),
  },
});

const headerTabsSelector = createSelector(
  ( state )=>( state.tabs.header ),
  ( res )=>({
    activeTab: res.active
  })
);

const Authentication = memo(( props )=>{
  const { classes, ...other } = props;
  const dispatch = useDispatch();

  const { activeTab } = useSelector( headerTabsSelector );

  const handleChangeTab = useCallback(( event, newValue )=>{
    dispatch(actionChangeTabsHeader( newValue ));
  }, [ dispatch ]);

  return (
    <React.Fragment>
      <AppBar
        component="div"
        color="primary"
        position="static"
        elevation={0}
      >
        <Tabs
          className={ classes.tabs } 
          color="primary"
          onChange={ handleChangeTab } 
          value={ activeTab }
        >
          <Tab textColor="inherit" label="Users" {...a11yProps(0)}/>
          <Tab textColor="inherit" label="Sign-in method" {...a11yProps(1)} />
          <Tab textColor="inherit" label="Templates" {...a11yProps(2)}/>
          <Tab textColor="inherit" label="Usage" {...a11yProps(3)}/>
        </Tabs>
      </AppBar>
      <main className={ classes.main }>
        <HeaderTabPanel active={ activeTab } index={ 0 } >
          <Users />
        </HeaderTabPanel>
        <HeaderTabPanel active={ activeTab } index={ 1 } >
          Sign-in method
        </HeaderTabPanel>
        <HeaderTabPanel active={ activeTab } index={ 2 } >
          Templates
        </HeaderTabPanel>
        <HeaderTabPanel active={ activeTab } index={ 3 } >
          Usage
        </HeaderTabPanel>
      </main>
    </React.Fragment>
  );
});

export default withStyles(styles)(Authentication);