export const CHANGE_TABS_HEADER = 'event/tabs/CHANGE_TABS_HEADER';

export const actionChangeTabsHeader = (payload)=>({ type: CHANGE_TABS_HEADER, payload: payload });

const initState = {
  header: {
    value: 0
  }
}

const tabsReducer = ( state=initState, action )=>{
  switch( action.type ){
    case CHANGE_TABS_HEADER:
      return {
        ...state
        , header: { value: action.payload }
      }
    default:
      return state;
  }
}

export default tabsReducer;