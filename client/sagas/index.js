import { all, call } from 'redux-saga/effects'
import crud from './crud'
import user from './user'
import auth from './auth'

export default function* rootSaga(){
  yield all([
    call( crud )
    , call( user )
    , call( auth )
  ])
}