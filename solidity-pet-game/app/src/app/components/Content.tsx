import React, { useState } from 'react';
import Box from '@mui/material/Box';
import { MonsterList } from "./MonsterList";
import { GameDescription } from './GameDescription';
import Fab from '@mui/material/Fab';
import AddIcon from '@mui/icons-material/Add';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle'
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

export type ContentProps = {
    accountNumber?: string;
}

export const Content = ({ accountNumber }: ContentProps) => {
    return (
        <main>
            <Box
                sx={{
                    bgcolor: 'background.paper',
                    pb: 6,
                }}
            >
                {!accountNumber && <GameDescription />}
                {accountNumber && <AuthenticatedArea />}
            </Box>
        </main>
    );
}

const AuthenticatedArea = () => {
    const [openBattleDialog, setOpenBattleDialog] = useState<boolean>(false);
    const [attackerId, setAttackerId] = useState<string| undefined>();
    const showBattleDialog = () => setOpenBattleDialog(true);
    const handleClose = () => setOpenBattleDialog(false);

    const onTrainClick = (monsterId: string) => { };
    const onBattleClick = (monsterId: string) => { 
        setAttackerId(monsterId);
        setOpenBattleDialog(true);
    };

    return (
        <>
            <MonsterList onTrainClick={onTrainClick} onBattleClick={onBattleClick} />
            <Fab variant="extended" color="primary" aria-label="add" sx={{ position: 'fixed', bottom: 16, right: 16 }}>
                <AddIcon sx={{ mr: 1 }} />
                Mint
            </Fab>
            <BattleDialog open={openBattleDialog} attackerId={attackerId} handleClose={handleClose} />
        </>
    );
};


export type BattleDialogProps = {
    open: boolean;
    attackerId: string| undefined;
    handleClose: () => void;
};

const BattleDialog = ({ open, attackerId, handleClose }: BattleDialogProps) => {
    const [defenderId, setDefenderId] = useState<string>('');
    return (
        <Dialog open={open} onClose={handleClose}>
            <DialogTitle>Battle</DialogTitle>
            <DialogContent>
                <DialogContentText>
                    Attacker: Monster {attackerId}
                </DialogContentText>
                <TextField
                    autoFocus
                    margin="dense"
                    id="name"
                    label="Defender: Monster Id"
                    type="text"
                    fullWidth
                    variant="standard"
                    value={defenderId}
                    onChange={(e) => setDefenderId(e.target.value)}
                />
            </DialogContent>
            <DialogActions>
                <Button onClick={handleClose}>Cancel</Button>
                <Button onClick={handleClose} color="error" >Atack</Button>
            </DialogActions>
        </Dialog>

    );
}