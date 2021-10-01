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

const theme = createTheme();

function App() {
  const [web3, setWeb3] = useState<Web3 | undefined>();
  const [account, setAccount] = useState<string | undefined>('12345566776fgnufgnfrngjjgnjfgnfgjj');

  const onClickLogin = async () => {
    const web3 = await loginWithMetamask();
    setWeb3(web3);
  }

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Header accountNumber={account} onClickLogin={onClickLogin} />
      <Content accountNumber={account} />
    </ThemeProvider>
  );
}
export default App;
