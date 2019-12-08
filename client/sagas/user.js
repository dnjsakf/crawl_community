import { all, call, put, fork, takeLatest } from 'redux-saga/effects'
import { INSERT_USER, INSERT_USER_SUCCESS, INSERT_USER_FAILURE } from '../reducers/user'
import { UPDATE_USER, UPDATE_USER_SUCCESS, UPDATE_USER_FAILURE } from '../reducers/user'
import { DELETE_USER, DELETE_USER_SUCCESS, DELETE_USER_FAILURE } from '../reducers/user'
import { SELECT_USER, SELECT_USER_SUCCESS, SELECT_USER_FAILURE } from '../reducers/user'

import axios from 'axios'
import { SELECT_SUCCESS, SELECT_FAILURE } from '../reducers/crud'

function requestSignIn( userinfo ){
  console.log( '[saga][user] requestSignIn', userinfo );
  return axios({
    method: 'POST'
    , baseURL: 'http://localhost:3000'
    , headers: {
      'Access-Control-Allow-Origin': '*'
      , 'Access-Control-Allow-Methods': 'POST'
    }
    , url: '/auth/signin'
    , data: {
      userinfo: userinfo
    }
  });
}

function requestSignUp( userinfo ){
  console.log( '[saga][user] requestSignUp', userinfo );
  return axios({
    method: 'POST'
    , baseURL: 'http://localhost:3000'
    , headers: {
      'Access-Control-Allow-Origin': '*'
      , 'Access-Control-Allow-Methods': 'POST'
    }
    , url: '/auth/signup'
    , data: {
      userinfo: userinfo
    }
  });
}

function* handleSelect( action ){
  try {
    const response = yield call( requestSignIn, action.payload );
    console.log('[saga][user] handleSelect', response);
    yield put({
      type: SELECT_SUCCESS
      , payload: response.data
    });
  } catch ( error ){
    yield put({
      type: SELECT_FAILURE
      , payload: error
    })
  } 
}

function* handleInsert( action ){
  try {
    const response = yield call( requestSignUp, action.payload )
    console.log('[saga][user] handleInsert', response);
    yield put({
      type: INSERT_USER_SUCCESS
      , payload: response.data
    });
  } catch ( error ){
    yield put({
      type: INSERT_USER_FAILURE
      , payload: error
    });
  }
}

function* watchSelect(){
  yield takeLatest( SELECT_USER, handleSelect );
}
function* watchInsert(){
  yield takeLatest( INSERT_USER, handleInsert );
}

export default function* userSaga(){
  yield all([
    fork( watchSelect )
    , fork( watchInsert )
  ])
}