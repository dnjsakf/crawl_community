import React, { memo, useCallback, useEffect, useRef } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { createSelector } from 'reselect';
import { withRouter, Link } from 'react-router-dom';
import { actionSignIn } from './../../reducers/auth/sign';

/* Components */
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
// import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';

/* Icons */
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import { Copyright } from './../Contents';

const useStyles = makeStyles(theme => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

const signSelector = createSelector(
  ( state )=>( state.sign ),
  ( res )=>({
    signed: res.signed
    , success: res.success
    , userinfo: res.userinfo
    , token: res.token
  })
);

const SignIn = memo(( props )=>{
  const classes = useStyles();
  const dispatch = useDispatch();

  const emailRef = useRef();
  const passwordRef = useRef();

  const { signed, success, userinfo, token } = useSelector( signSelector );
  
  const handleAuthIn = useCallback(( event )=>{ 
    event.preventDefault()
    const userinfo = {
      email: emailRef.current.value
      , password: passwordRef.current.value
    }
    dispatch( actionSignIn( userinfo ) );
  }, [ dispatch ]);

  useEffect(()=>{
    console.log('[SingIn][current]', signed, success );
    if( signed === 1 && success ){
      console.log('redirect to /');
      localStorage.setItem('token', token);
      props.history.push('/');
    }
    return ()=>{
      console.log('[SingIn][prev]', signed, success );
    }
  },[ signed, success, userinfo, token ])

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign in
        </Typography>
        <form className={classes.form} noValidate>
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="email"
            label="Email Address"
            name="email"
            autoComplete="email"
            autoFocus
            inputRef={ emailRef }
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
            inputRef={ passwordRef }
          />
          <FormControlLabel
            control={<Checkbox value="remember" color="primary" />}
            label="Remember me"
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
            onClick={ handleAuthIn }
          >
            Sign In
          </Button>
          <Grid container>
            <Grid item xs>
              <Link to="#" variant="body2">
                Forgot password?
              </Link>
            </Grid>
            <Grid item>
              <Link to="/auth/signup" variant="body2">
                {"Don't have an account? Sign Up"}
              </Link>
            </Grid>
          </Grid>
        </form>
      </div>
      <Box mt={8}>
        <Copyright />
      </Box>
    </Container>
  );
});

export default withRouter(SignIn);