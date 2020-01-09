import React, { memo, useEffect, useCallback } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { createSelector } from 'reselect';
import { withRouter } from 'react-router-dom';

import { actionGetCommunities } from './../../../reducers/cnts/communities';

/* Conponents */
import MediaCard from './../../Contents/Items/MediaCard';
import GridList from '@material-ui/core/GridList';

import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(theme => ({
  root: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
    overflow: 'hidden',
  },
  gridList: {
    height: '100%',
    margin: 'auto',
  },
}));

const communitiesSelector = createSelector(
  ( state )=>( state.communities ),
  ( _, loaded )=>( loaded ),
  ( communities, loaded )=>({
    success: communities.success
    , communities: communities.data
    , loaded: loaded
  })
);

const Communities = memo(( props )=>{
  const classes = useStyles();
  const dispatch = useDispatch();
  
  const { success, communities, loaded } = useSelector(( state )=>(
    communitiesSelector( state, true )
  ));

  const handleGetCommuities = useCallback((event)=>{
    dispatch(actionGetCommunities());
  }, [ dispatch ]);

  useEffect(()=>{
    handleGetCommuities();
  },[]);

  return (
    <>
      {
        success ?
        ( <div className={classes.root}>
            <GridList className={classes.gridList} cellHeight={160} cols={3}>
            {
              communities.map((data)=>{
                return <MediaCard key={ data._id } {...data} />
              })
            }
            </GridList>
          </div>
        ) : 
        '데이터가 없습니다.'
      }
    </>
  );
});

export default withRouter(Communities);