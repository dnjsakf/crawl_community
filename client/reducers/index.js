import { combineReducers } from 'redux'
import crudReducer from './crud'
import userReducer from './user'
import authReducer from './auth'

const rootReducer = combineReducers({
  crud: crudReducer
  , user: userReducer
  , auth: authReducer
})

export default rootReducer