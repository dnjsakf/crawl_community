export const defaultActive = 'develop.management';

const cateoriges = [{
  cate: {
    id: 'develop'
    , label: 'Develop'
  }
  , children: [{
      cate: {
        id: 'develop.authentication'
        , label: 'Authentication'
      }
      , icon: 'PeopleIcon'
    }
    , {
      cate: {
        id: 'develop.management'
        , label: 'Management'
      }
      , icon: 'SettingsIcon'
    }
  ]
}];

export const default_category = {
  active: cateoriges[0].children[0].cate.id
  , label: cateoriges[0].children[0].cate.label
}

export default cateoriges;