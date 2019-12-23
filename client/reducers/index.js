import { combineReducers } from 'redux';
import crudReducer from './crud';
import { signReducer } from './auth';
import { tabsReducer } from './event';
import { communitiesReducer } from './cnts';

const rootReducer = combineReducers({
  crud: crudReducer
  , sign: signReducer
  , communities: communitiesReducer
  , tabs: tabsReducer
});

export default rootReducer;