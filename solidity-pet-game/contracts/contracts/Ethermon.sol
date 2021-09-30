// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import '../node_modules/@openzeppelin/contracts/token/ERC721/ERC721.sol';
import '../node_modules/@openzeppelin/contracts/access/Ownable.sol';

contract Ethermon is ERC721, Ownable{

    uint256 tokenIdSeq = 0;

    struct Monster {
        uint256 id;
        uint256 hp;
        uint256 currentHp;

        uint256 attack;
        uint256 defense;
        uint256 speed;

        uint256 level;
        uint256 pointsForSpeeding;

        uint256 lastWork;
    }

    mapping(uint256 => Monster) private _monsters;

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
    }

    function getMonsterById(uint256 tokenId) public view returns (Monster memory) {
        return _monsters[tokenId];
    }

    function mint(uint256 hp, uint256 attack, uint256 defense, uint256 speed) public onlyOwner {
        uint256 id = ++tokenIdSeq;
        
        _monsters[id] = Monster(
            id, 
            hp, 
            hp,//currentHp,
            attack,
            defense,
            speed,
            1,
            0,
            block.timestamp
        );
        _safeMint(msg.sender, id);

        tokenIdSeq++;
    }

    function train(uint256 tokenId) public {
        Monster storage monster = _monsters[tokenId];

        require(monster.lastWork < block.timestamp, 'The monster is already training');

        monster.lastWork = (2^monster.level) + block.timestamp;

        monster.level += 1;
        monster.pointsForSpeeding = monster.level;
    }

    function battle(uint256 attackerId, uint256 defenderId) public {
        Monster storage attacker = _monsters[attackerId];
        Monster storage defender = _monsters[defenderId];

        if (attacker.speed > defender.speed) {
            fight(attacker, defender);
        } else {
            fight(defender, attacker);
        }
    }

    function fight(Monster storage attacker, Monster storage defender) internal {
        for(uint i = 0; i<3; i++) {
            if (attacker.currentHp > 0) {
                strike(attacker, defender);
            }

            if (defender.currentHp > 0) {
                strike(defender, attacker);
            }
        }
    }

    function strike(Monster storage attacker, Monster storage defender) internal {
        uint damage = attacker.attack - defender.defense;
        defender.currentHp =  defender.currentHp - damage;
    }

}  

