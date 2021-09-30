import React from 'react';
import Box from '@mui/material/Box';
import { MonsterList } from "./MonsterList";
import { GameDescription } from './GameDescription';

export type ContentProps = {
    accountNumber?: string;
}
export const Content = ({accountNumber}: ContentProps) => {
    return (
        <main>
            <Box
            sx={{
                bgcolor: 'background.paper',
                pb: 6,
            }}
            >
                {!accountNumber &&  <GameDescription />}
                {accountNumber &&  <MonsterList />}
            </Box>
      </main>
    );
}