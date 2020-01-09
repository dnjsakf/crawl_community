import React from 'react';

/* Icons */
import PeopleIcon from '@material-ui/icons/People';
import DnsRoundedIcon from '@material-ui/icons/DnsRounded';
import PermMediaOutlinedIcon from '@material-ui/icons/PhotoSizeSelectActual';
import PublicIcon from '@material-ui/icons/Public';
import SettingsEthernetIcon from '@material-ui/icons/SettingsEthernet';
import SettingsInputComponentIcon from '@material-ui/icons/SettingsInputComponent';
import TimerIcon from '@material-ui/icons/Timer';
import SettingsIcon from '@material-ui/icons/Settings';
import PhonelinkSetupIcon from '@material-ui/icons/PhonelinkSetup';

const Icons = {
  'PeopleIcon': <PeopleIcon />
  , 'DnsRoundedIcon': <DnsRoundedIcon />
  , 'PermMediaOutlinedIcon': <PermMediaOutlinedIcon />
  , 'PublicIcon': <PublicIcon />
  , 'SettingsEthernetIcon': <SettingsEthernetIcon />
  , 'SettingsInputComponentIcon': <SettingsInputComponentIcon />
  , 'TimerIcon': <TimerIcon />
  , 'SettingsIcon': <SettingsIcon />
  , 'PhonelinkSetupIcon': <PhonelinkSetupIcon />
}

export default ( iconId )=>{
  return Icons[iconId];
}