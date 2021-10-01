import React from 'react';
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
    const [openBattleDialog, setOpenBattleDialog] = React.useState<boolean>(false);
    const showBattleDialog = () => setOpenBattleDialog(true);
    const handleClose = () => setOpenBattleDialog(false);

    const onTrainClick = (traintId: string) => { };
    const onBattleClick = (monsterId: string) => { 
        setOpenBattleDialog(true);
    };

    return (
        <>
            <MonsterList onTrainClick={onTrainClick} onBattleClick={onBattleClick} />
            <Fab variant="extended" color="primary" aria-label="add" sx={{ position: 'fixed', bottom: 16, right: 16 }}>
                <AddIcon sx={{ mr: 1 }} />
                Mint
            </Fab>
            <BattleDialog open={openBattleDialog} handleClose={handleClose} />
        </>
    );
};


export type BattleDialogProps = {
    open: boolean;
    handleClose: () => void;
};

const BattleDialog = ({ open, handleClose }: BattleDialogProps) => {
    return (

        <Dialog open={open} onClose={handleClose}>
            <DialogTitle>Subscribe</DialogTitle>
            <DialogContent>
                <DialogContentText>
                    To subscribe to this website, please enter your email address here. We
                    will send updates occasionally.
                </DialogContentText>
                <TextField
                    autoFocus
                    margin="dense"
                    id="name"
                    label="Email Address"
                    type="email"
                    fullWidth
                    variant="standard"
                />
            </DialogContent>
            <DialogActions>
                <Button onClick={handleClose}>Cancel</Button>
                <Button onClick={handleClose}>Subscribe</Button>
            </DialogActions>
        </Dialog>

    );
}