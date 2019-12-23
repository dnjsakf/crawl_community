import { all, call, put, fork, takeLatest } from 'redux-saga/effects'
import { SELECT, SELECT_SUCCESS, SELECT_FAILURE } from '../reducers/crud'
import { INSERT, INSERT_SUCCESS, INSERT_FAILURE } from '../reducers/crud'

import axios from './../utils/axios'

function requestWithAxios( options ){
  console.log( '[saga] request', options );
  return axios( options );
}

function* handleSelect( action ){
  try {
    const response = yield call( requestWithAxios, action.payload );
    console.log( '[saga] handleSelect', response )
    yield put({
      type: SELECT_SUCCESS
      , payload: response
    });
  } catch ( error ){
    console.error( '[saga] handleSelect', error );
    yield put({
      type: SELECT_FAILURE
    });
  }
}
function* handleInsert( action ){
  try {
    const response = yield call( requestWithAxios, action.payload );
    console.log( '[saga] handleInsert', response )
    yield put({
      type: SELECT
      , payload: response.data
    });
    // yield put({
    //   type: INSERT_SUCCESS
    //   , payload: response
    // });
  } catch ( error ){
    console.error( '[saga] handleInsert', error );
    yield put({
      type: INSERT_FAILURE
    });
  }
}

function* watchSelect(){
  yield takeLatest( SELECT, handleSelect );
}
function* watchInsert(){
  yield takeLatest( INSERT, handleInsert );
}

// Create Generator function
export default function* crudSaga(){
  yield all([
    fork( watchSelect )
    , fork( watchInsert )
  ]);
}