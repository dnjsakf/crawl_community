import React, { memo, useEffect, useCallback } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { withRouter } from 'react-router-dom';

import { actionSignCheck } from './../../reducers/auth/sign';

const Checker = memo(( props )=>{
  const dispatch = useDispatch();

  const alreadySigned = localStorage.getItem('signed');
  const { signed, userinfo } = useSelector(( state )=>( state.sign ), []);

  const handleAuthCheck = useCallback(()=>{
    dispatch( actionSignCheck() );
  }, [ signed ]);

  useEffect(()=>{
    handleAuthCheck();
  }, []);

  useEffect(()=>{
    if ( alreadySigned == '1' ){
      console.log('[Checker][alreadySigned]', alreadySigned, signed);
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