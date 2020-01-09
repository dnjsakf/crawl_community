import { createAction, handleActions } from 'redux-actions';

export const CHANGE_TABS_HEADER = 'event/tabs/CHANGE_TABS_HEADER';

export const actionChangeTabsHeader = createAction( CHANGE_TABS_HEADER );

const initState = {
  header: {
    active: 0
  }
}

const tabsReducer = handleActions({
  /** CHANGE_TABS_HEADER **/
  [CHANGE_TABS_HEADER]: ( state, action )=>({
    ...state
    , header: { 
      active: action.payload
    }
  })
}, initState );

export default tabsReducer;