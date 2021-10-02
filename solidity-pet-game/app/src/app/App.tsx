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
import { loadEthermonContract } from '../core/loadEthermonContract';
import { getAccount } from '../core/getAccount';
import { Contract } from 'web3-eth-contract';

const theme = createTheme();

function App() {
  const [web3, setWeb3] = useState<Web3 | undefined>();
  const [ethermonContract, setEthermonContract] = useState<Contract|undefined>();
  const [accountNumber, setAccountNumber] = useState<string | undefined>();

  const onClickLogin = async () => {
    const web3 = await loginWithMetamask();
    const ethermonContract  = await loadEthermonContract(web3);
    const accountNumber = await getAccount(web3);

    setWeb3(web3);
    setEthermonContract(ethermonContract);
    setAccountNumber(accountNumber);
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Header accountNumber={accountNumber} onClickLogin={onClickLogin} />
      <Content accountNumber={accountNumber} />
    </ThemeProvider>
  );
}
export default App;
