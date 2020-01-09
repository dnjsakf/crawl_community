import React, { memo, useEffect, useCallback } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { createSelector } from 'reselect';
import { withRouter } from 'react-router-dom';

import { actionSignCheck } from './../../reducers/auth/sign';


const signSelector = createSelector(
  ( state )=>( state.sign ),
  ( res )=>( res )
);

const AuthChecker = memo(( props )=>{
  const alreadySigned = localStorage.getItem('signed');
  const { history } = props;
  const dispatch = useDispatch();

  const { signed, userinfo } = useSelector( signSelector );

  const handleAuthCheck = useCallback(()=>{
    dispatch( actionSignCheck() );
  }, [ dispatch ]);

  useEffect(()=>{
    handleAuthCheck();
  }, [ history.location.pathname ]);

  useEffect(()=>{
    if ( alreadySigned == '1' ){
      console.log('[AuthChecker][alreadySigned]', alreadySigned, signed);
    }
    return ()=>{
      console.log('[AuthChecker][prev]', alreadySigned, signed);
    }
  }, [ alreadySigned ]);

  useEffect(()=>{
    console.log('[AuthChecker][signed]', signed, userinfo)
    localStorage.setItem('signed', signed);
    if( signed === 1 ){
      localStorage.setItem('userinfo', JSON.stringify( userinfo ));
    }
  }, [ signed ]);

  return (
    <></>
  );
});

export default withRouter(AuthChecker);