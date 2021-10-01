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
import TagFacesIcon from '@mui/icons-material/TagFaces';

export type MonsterCardProps = {
  monsterId: string;
  onTrainClick: (traintId: string) => void;
  onBattleClick: (monsterId: string) => void;
}

export const MonsterCard = ({ monsterId, onBattleClick, onTrainClick }: MonsterCardProps) => {
  
  const handleOnBattleClick = () => onBattleClick(monsterId);
  const handleOnTrainClick = () => onTrainClick(monsterId);
  
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
        <List dense={true} sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}>
          <ListItem>
            <ListItemAvatar>
              <Battery90Icon />
            </ListItemAvatar>
            <ListItemText primary="Hp: 40/100" />
          </ListItem>
          <ListItem>
            <ListItemAvatar>
              <TagFacesIcon />
            </ListItemAvatar>
            <ListItemText primary="Level: 1" />
          </ListItem>
          <ListItem>
            <ListItemAvatar>
              <WorkIcon />
            </ListItemAvatar>
            <ListItemText primary="Attack: 49" />
          </ListItem>
          <ListItem>
            <ListItemAvatar>
              <ShieldIcon />
            </ListItemAvatar>
            <ListItemText primary="Defense: 40" />
          </ListItem>
          <ListItem>
            <ListItemAvatar>
              <SpeedIcon />
            </ListItemAvatar>
            <ListItemText primary="Speed: 30" />
          </ListItem>
        </List>
      </CardContent>
      <CardActions>
        <Button variant="contained" sx={{width:'100%'}} onClick={handleOnTrainClick}>Train</Button>
        <Button variant="contained" color="error" sx={{width:'100%'}} onClick={handleOnBattleClick}>Battle</Button>
      </CardActions>
    </Card>
  );
}