import React from 'react';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import { MonsterCard } from './MonsterCard';

const cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
export type MonsterListProps = {
  onTrainClick: (traintId: string) => void;
  onBattleClick: (monsterId: string) => void;
}
export const MonsterList = ({ onTrainClick, onBattleClick }: MonsterListProps) => {
  return (
    <Container sx={{ py: 8 }} maxWidth="md">
      {/* End hero unit */}
      <Grid container spacing={4}>
        {cards.map((card) => (
          <Grid item key={card} xs={12} sm={6} md={4}>
            <MonsterCard monsterId={card} onTrainClick={onTrainClick} onBattleClick={onBattleClick} />
          </Grid>
        ))}
      </Grid>
    </Container>
  );
}