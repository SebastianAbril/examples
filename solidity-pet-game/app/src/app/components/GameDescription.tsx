import React from 'react';
import Container from '@mui/material/Container';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import CatchingPokemonIcon from '@mui/icons-material/CatchingPokemon';

export const GameDescription = () => {
  return (
    <Container maxWidth="sm" sx={{ marginTop: 10 }}>
      <Typography
        component="h1"
        variant="h2"
        align="center"
        color="text.primary"
        gutterBottom
      >
        Ethermon
      </Typography>
      <Typography variant="h5" align="center" color="text.secondary" paragraph>
        Simple eth monster game Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis aliquet arcu ac felis sagittis, et viverra est vestibulum. Mauris justo velit, euismod ut lacus a, interdum mattis mauris. Suspendisse consequat nibh ac nisl lobortis, ut pulvinar lorem lobortis. Quisque nec nunc auctor, pellentesque turpis quis, dignissim quam. Nullam enim libero, bibendum dapibus eros id, cursus porta mi. Mauris malesuada scelerisque suscipit. Curabitur ac eros ornare, cursus ligula eu, vestibulum ante. Maecenas facilisis porta sapien. Praesent lobortis ac ante non vehicula.
      </Typography>
    </Container>
  );
}