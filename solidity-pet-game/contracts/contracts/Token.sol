// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import '../node_modules/@openzeppelin/contracts/token/ERC721/ERC721.sol';
import '../node_modules/@openzeppelin/contracts/access/Ownable.sol';

contract Token is ERC721, Ownable{

    uint256 tokenIdSeq = 0;

    struct Pet {
        uint8 damage;
        uint8 magic;
        uint256 lastMeal;
        uint256 endurance;
    }

    mapping(uint256 => Pet) private _tokenDetails;

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
    }

    function getTokenDetails(uint256 tokenId) public view returns (Pet memory) {
        return _tokenDetails[tokenId];
    }

    function mint(uint8 damage, uint8 magic, uint256 endurance) public onlyOwner {
        _tokenDetails[tokenIdSeq] = Pet(damage, magic, block.timestamp, endurance);
        _safeMint(msg.sender, tokenIdSeq);

        tokenIdSeq++;
    }

    function feed(uint256 tokenId) public {
        Pet storage pet = _tokenDetails[tokenId];

        require(pet.lastMeal + pet.endurance > block.timestamp, 'The Pet is dead');

        pet.lastMeal = block.timestamp;
    }

    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override {
        Pet storage pet = _tokenDetails[tokenId];
        require(pet.lastMeal + pet.endurance > block.timestamp, 'The Pet is dead');
    }
}