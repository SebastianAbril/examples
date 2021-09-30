import React from 'react';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import CardHeader from '@mui/material/CardHeader';
import CatchingPokemonIcon from '@mui/icons-material/CatchingPokemon';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import Avatar from '@mui/material/Avatar';
import ImageIcon from '@mui/icons-material/Image';
import WorkIcon from '@mui/icons-material/Work';
import BeachAccessIcon from '@mui/icons-material/BeachAccess';
import ShieldIcon from '@mui/icons-material/Shield';
import SpeedIcon from '@mui/icons-material/Speed';
import Battery90Icon from '@mui/icons-material/Battery90';
import FaceIcon from '@mui/icons-material/Face';

export type MonsterCardProps = {
  monsterId: number;
}

export const MonsterCard = ({ monsterId }: MonsterCardProps) => {
  return (
    <Card
      sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}
    >
      <CardHeader
        avatar={
          <CatchingPokemonIcon sx={{ mr: 2 }} />
        }
        title={"Monster" + monsterId}
      />
      <CardMedia
        component="img"
        height="194"
        image="https://source.unsplash.com/random"
        alt="random"
      />
      <CardContent sx={{ flexGrow: 1 }}>
        <List sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}>
          <ListItem>
            <ListItemAvatar>
              <Avatar>
                <Battery90Icon />
              </Avatar>
            </ListItemAvatar>
            <ListItemText primary="Hp" secondary="Jan 9, 2014" />
          </ListItem>
          <ListItem>
            <ListItemAvatar>
              <Avatar>
                <WorkIcon />
              </Avatar>
            </ListItemAvatar>
            <ListItemText primary="Attack" secondary="Jan 7, 2014" />
          </ListItem>
          <ListItem>
            <ListItemAvatar>
              <Avatar>
                <ShieldIcon />
              </Avatar>
            </ListItemAvatar>
            <ListItemText primary="Defense" secondary="July 20, 2014" />
          </ListItem>
          <ListItem>
            <ListItemAvatar>
              <Avatar>
                <SpeedIcon />
              </Avatar>
            </ListItemAvatar>
            <ListItemText primary="Speed" secondary="July 20, 2014" />
          </ListItem>
        </List>
      </CardContent>
      <CardActions>
        <Button size="small">View</Button>
        <Button size="small">Edit</Button>
      </CardActions>
    </Card>
  );
}