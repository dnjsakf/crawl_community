import React, { memo, useState, useEffect, useCallback, useRef } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { withRouter } from 'react-router-dom';

import { actionSignCheck } from './../../reducers/auth'

  const Checker = memo(( props )=>{
  const dispatch = useDispatch();

  const alreadySigned = localStorage.getItem('signed');
  const { signed, userinfo } = useSelector(( state )=>( state.auth ), []);

  const handleAuthCheck = useCallback(()=>{
    dispatch( actionSignCheck() );
  }, [ alreadySigned ]);

  useEffect(()=>{
    if ( alreadySigned == '1' ){
      console.log('[Checker][alreadySigned]', alreadySigned, signed);
      handleAuthCheck();
    }
    return ()=>{
      console.log('[Checker][prev]', alreadySigned, signed);
    }
  }, [ alreadySigned ]);

  useEffect(()=>{
    console.log('[Checker][signed]', signed, userinfo)
    localStorage.setItem('signed', signed);
    if( signed === 1 ){
      localStorage.setItem('userinfo', JSON.stringify( userinfo ));
    }
  }, [ signed ]);

  return (
    <></>
  );
});

export default withRouter(Checker);