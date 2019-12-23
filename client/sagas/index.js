import { all, call } from 'redux-saga/effects';
import crud from './crud';
import { sign } from './auth';
import { communities } from './cnts';

export default function* rootSaga(){
  yield all([
    call( crud )
    , call( sign )
    , call( communities )
  ])
}