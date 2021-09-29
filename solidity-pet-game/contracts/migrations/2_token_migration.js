const Migrations = artifacts.require("Token");

module.exports = function (deployer) {
  deployer.deploy(Migrations, 'NTF PET GAME', 'NFPG');
};
