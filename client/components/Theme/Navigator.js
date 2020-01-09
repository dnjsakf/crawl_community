import React, { memo, useState, useCallback, useEffect } from 'react';
import { useSelector, useDispatch, useStore } from 'react-redux';
import { createSelector } from 'reselect';
import { actionChangeNaviMenu } from './../../reducers/event/menus';

import { withRouter, Link } from 'react-router-dom';

import categories from './../Common/Menus/NavigartorMenu';

import PropTypes from 'prop-types';
import clsx from 'clsx';

import { withStyles } from '@material-ui/core/styles';

/* Components */
import Divider from '@material-ui/core/Divider';
import Drawer from '@material-ui/core/Drawer';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';

/* Icons */
import HomeIcon from '@material-ui/icons/Home';

import RednerIcons from './../Common/RenderIcons';

const styles = ( theme )=>({
  categoryHeader: {
    paddingTop: theme.spacing(2),
    paddingBottom: theme.spacing(2),
  },
  categoryHeaderPrimary: {
    color: theme.palette.common.white,
  },
  item: {
    paddingTop: 1,
    paddingBottom: 1,
    color: 'rgba(255, 255, 255, 0.7)',
    '&:hover,&:focus': {
      backgroundColor: 'rgba(255, 255, 255, 0.08)',
    },
  },
  itemCategory: {
    backgroundColor: '#232f3e',
    boxShadow: '0 -1px 0 #404854 inset',
    paddingTop: theme.spacing(2),
    paddingBottom: theme.spacing(2),
  },
  firebase: {
    fontSize: 24,
    color: theme.palette.common.white,
  },
  itemActiveItem: {
    color: '#4fc3f7',
  },
  itemPrimary: {
    fontSize: 'inherit',
  },
  itemIcon: {
    minWidth: 'auto',
    marginRight: theme.spacing(2),
  },
  divider: {
    marginTop: theme.spacing(2),
  },
});

function makeMenu({ classes, cate, icon, children }){
  const isTopMenu = cate.id.indexOf('.') === -1;
  return children.map((  )=>(
    <ListItem 
      key={ cCcate.id }
      className={classes.categoryHeader}
    >
      { icon && <ListItemIcon className={classes.itemIcon}>{ icon }</ListItemIcon> }
      <ListItemText
        classes={{
          primary: classes.categoryHeaderPrimary,
        }}
      >
        { cate.label }
      </ListItemText>
    </ListItem>
  ));
}

const navigatorSelector = createSelector(
  ( state )=>( state.menus.navigator ),
  ( res )=>({
    activeNaviIndex: res.index
    , activeNaviId: res.active
    , activeNaviLabel: res.label
  })
);

const Navigator = memo(( props )=>{
  const { classes, staticContext, ...other } = props;
  const dispatch = useDispatch();

  const { activeNaviIndex, activeNaviId } = useSelector( navigatorSelector );

  const handleChangeNaviMenu = useCallback( ( index, current, label )=>( event )=>{
    dispatch(actionChangeNaviMenu({
      index: index
      , active: current 
      , label: label
    }));
  }, [ dispatch ] );

  useEffect(()=>{
    console.log( '[Navigator][activeNavi][current]', activeNaviIndex, activeNaviId );
    return ()=>{
      console.log( '[Navigator][activeNavi][prev]', activeNaviIndex, activeNaviId );
    }
  }, [ activeNaviIndex, activeNaviId ]);

  return (
    <Drawer variant="permanent" {...other} >
      <List disablePadding>
        <ListItem className={clsx(classes.firebase, classes.item, classes.itemCategory)}>
          <Link to="/" variant="body2">
            Paperbase
          </Link>
        </ListItem>
        <ListItem className={clsx(classes.item, classes.itemCategory)}>
          <ListItemIcon className={classes.itemIcon}>
            <HomeIcon />
          </ListItemIcon>
          <ListItemText
            classes={{
              primary: classes.itemPrimary,
            }}
          >
            Project Overview
          </ListItemText>
        </ListItem>
        {categories.map(({ cate, children }, pIndex) => (
          <React.Fragment key={ cate.id }>
            <ListItem className={ classes.categoryHeader }>
              <ListItemText
                classes={{
                  primary: classes.categoryHeaderPrimary,
                }}
              >
                { cate.label }
              </ListItemText>
            </ListItem>
            {children.map(({ cate: cCcate, icon }, index) => {
              const isActive = activeNaviId ? cCcate.id === activeNaviId : index === 0;
              
              return (
                <ListItem
                  key={ cCcate.id }
                  button
                  className={clsx( classes.item, isActive && classes.itemActiveItem )}
                  onClick={ handleChangeNaviMenu( index, cCcate.id, cCcate.label ) }
                >
                  { icon && <ListItemIcon className={ classes.itemIcon }>{ RednerIcons( icon ) }</ListItemIcon> }
                  <ListItemText
                    classes={{
                      primary: classes.itemPrimary,
                    }}
                  >
                    { cCcate.label } 
                  </ListItemText>
                </ListItem>
              )
            })}
            <Divider className={ classes.divider } />
          </React.Fragment>
        ))}
      </List>
    </Drawer>
  );
});

Navigator.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withRouter(withStyles(styles)(Navigator));