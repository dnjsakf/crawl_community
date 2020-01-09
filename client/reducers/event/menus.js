import { createAction, handleActions } from 'redux-actions';
import { default_category } from './../../components/Common/Menus/NavigartorMenu';

export const CHANGE_NAVI_MENU = 'event/menus/CHANGE_NAVI_MENU';

export const actionChangeNaviMenu = createAction( CHANGE_NAVI_MENU );

const initState = {
  navigator: {
    index: 0
    , ...default_category
  }
}

const menusReducer = handleActions({
  /** CHANGE_NAVI_MENU **/
  [CHANGE_NAVI_MENU]: ( state, action )=>({
    ...state
    , navigator: {
      index: action.payload.index
      , active: action.payload.active
      , label: action.payload.label
    }
  })
}, initState );

export default menusReducer;