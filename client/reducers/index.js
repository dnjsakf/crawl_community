import { combineReducers } from 'redux'
import crudReducer from './crud'
import userReducer from './user'

const rootReducer = combineReducers({
  crud: crudReducer
  , user: userReducer
})

export default rootReducer