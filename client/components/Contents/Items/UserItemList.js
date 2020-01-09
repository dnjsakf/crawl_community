import React from 'react';

import { withStyles } from '@material-ui/core/styles';

import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemSecondaryAction from '@material-ui/core/ListItemSecondaryAction';
import ListItemText from '@material-ui/core/ListItemText';
import IconButton from '@material-ui/core/IconButton';

import FolderIcon from '@material-ui/icons/Folder';
import DeleteIcon from '@material-ui/icons/Delete';

const style = theme => ({
  root: {
    flexGrow: 1,
    maxWidth: 752,
  },
  demo: {
    backgroundColor: theme.palette.background.paper,
  },
  title: {
    margin: theme.spacing(4, 0, 2),
  },
});

const UserItemList = ( props )=>{
  const { classes, data } = props;

  const [ dense, setDense ] = React.useState(true);
  const [ secondary, setSecondary ] = React.useState(true);

  return (
    <>
      <div className={classes.demo}>
        <List dense={ dense }>
        {
          data.map(( item )=>(
            <ListItem key={ item._id }>
              <ListItemIcon>
                <FolderIcon />
              </ListItemIcon>
              <ListItemText
                primary={ item.email }
                secondary={ secondary ? ( <span><a>{ item.username }</a><a>{ item.regDate }</a></span> ) : null }
              />
              <ListItemSecondaryAction>
                <IconButton 
                  edge="end" 
                  aria-label="delete"
                >
                  <DeleteIcon />
                </IconButton>
              </ListItemSecondaryAction>
            </ListItem>
          ))
        }
        </List>
      </div>
    </>
  );
};

export default withStyles(style)(UserItemList);