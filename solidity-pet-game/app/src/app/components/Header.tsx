import React from 'react';
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Button from '@mui/material/Button';
import CatchingPokemonIcon from '@mui/icons-material/CatchingPokemon';

export type HeaderProps = {
    accountNumber?: string;
    onClickLogin: () => void;
};

export const Header = ({accountNumber, onClickLogin}: HeaderProps) => {
    return (
        <AppBar position="relative">
        <Toolbar>
          <CatchingPokemonIcon sx={{ mr: 2 }} />
          <Typography variant="h6" color="inherit" component="div" sx={{ flexGrow: 1 }}>
            Ethermon
          </Typography>
          {!accountNumber && <Button color="inherit" onClick={onClickLogin}>Login</Button>}
          {accountNumber && <Typography variant="h6" color="inherit">{accountNumber}</Typography>}
        </Toolbar>
      </AppBar>
    );
}
