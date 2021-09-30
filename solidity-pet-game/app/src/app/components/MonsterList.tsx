import React from 'react';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import { MonsterCard } from './MonsterCard';

const cards = [1, 2, 3, 4, 5, 6, 7, 8, 9];

export const MonsterList = () => {
    return (
        <Container sx={{ py: 8 }} maxWidth="md">
        {/* End hero unit */}
        <Grid container spacing={4}>
          {cards.map((card) => (
            <Grid item key={card} xs={12} sm={6} md={4}>
              <MonsterCard monsterId={card} />
            </Grid>
          ))}
        </Grid>
      </Container>
    );
}