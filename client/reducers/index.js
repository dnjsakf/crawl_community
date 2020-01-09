import { combineReducers } from 'redux';
import crudReducer from './crud';
import { signReducer } from './auth';
import { tabsReducer, menusReducer } from './event';
import { communitiesReducer, usersReducer } from './cnts';

const rootReducer = combineReducers({
  sign: signReducer
  , communities: communitiesReducer
  , tabs: tabsReducer
  , menus: menusReducer
  , users: usersReducer
});

export default rootReducer;