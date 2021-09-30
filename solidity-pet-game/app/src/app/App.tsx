import React, { useState } from 'react';
import CssBaseline from "@mui/material/CssBaseline";
import Typography from "@mui/material/Typography";
import Box from '@mui/material/Box';
import Link from '@mui/material/Link';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { loginWithMetamask } from '../core/loginWithMetamask';
import Web3 from 'web3';
import { Header } from './components/Header';
import { Content } from './components/Content';

function Copyright() {
    return (
      <Typography variant="body2" color="text.secondary" align="center">
        {'Copyright © '}
        <Link color="inherit" href="https://material-ui.com/">
          Your Website
        </Link>{' '}
        {new Date().getFullYear()}
        {'.'}
      </Typography>
    );
  }
  

  
  const theme = createTheme();
  
function App() {
  const [web3, setWeb3] = useState<Web3|undefined>();

  const onClickLogin = async () => {
    const web3 = await loginWithMetamask();
    setWeb3(web3);
  }
  

    return (
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Header accountNumber="1244" onClickLogin={onClickLogin}/>
        <Content accountNumber="1244"/>
        {/* Footer */}
        <Box sx={{ bgcolor: 'background.paper', p: 6 }} component="footer">
          <Typography variant="h6" align="center" gutterBottom>
            Footer
          </Typography>
          <Typography
            variant="subtitle1"
            align="center"
            color="text.secondary"
            component="p"
          >
            Something here to give the footer a purpose!
          </Typography>
          <Copyright />
        </Box>
        {/* End footer */}
      </ThemeProvider>
    );
}
export default App;
